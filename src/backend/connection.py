import psycopg.errors
from psycopg import Connection

from src.backend.types import Column, Difference


class DatabaseConnection:
    def __init__(self):
        self.postgres_dsn = ""

        self.types_to_db: dict[str, str] = {
            "Integer": "integer",
            "Float": "numeric",
            "Text": "text",
            "Datetime": "timestamp with time zone",
        }

        self.types_from_db: dict[str, str] = {
            "integer": "Integer",
            "numeric": "Float",
            "text": "Text",
            "timestamp with time zone": "Datetime",
        }

    def set_connection(self, user: str, password: str, host: str, port: str, name: str) -> None:
        self.postgres_dsn = f"postgresql://{user}:{password}@{host}:{port}/{name}"
        conn = Connection.connect(self.postgres_dsn)
        conn.close()

    def get_tables(self) -> list[str]:
        with Connection.connect(self.postgres_dsn) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT table_name FROM information_schema.tables 
                    WHERE table_schema NOT IN ('information_schema','pg_catalog')
                """)

                return [table[0] for table in cursor.fetchall()]

    def get_fields(self, table_name: str) -> list[Column]:
        schema = "public"

        primary_key_query = (
            f"SELECT C.COLUMN_NAME FROM information_schema.table_constraints AS pk INNER JOIN "
            f"information_schema.KEY_COLUMN_USAGE AS C ON C.TABLE_NAME = pk.TABLE_NAME AND "
            f"C.CONSTRAINT_NAME = pk.CONSTRAINT_NAME AND C.TABLE_SCHEMA = pk.TABLE_SCHEMA WHERE "
            f"pk.TABLE_NAME = '{table_name}' AND pk.TABLE_SCHEMA = '{schema}' AND pk.CONSTRAINT_TYPE "
            f"= 'PRIMARY KEY';"
        )
        fields_query = (
            f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}';"
        )

        with Connection.connect(self.postgres_dsn) as conn:
            with conn.cursor() as cursor:
                cursor.execute(primary_key_query)

                primary_keys: list[str] = []
                for elem in cursor.fetchall():
                    primary_keys.append(elem[0])

                cursor.execute(fields_query)
                fields_raw = cursor.fetchall()

                fields: list[Column] = []
                for field_raw in fields_raw:
                    fields.append(
                        Column(
                            name=field_raw[0],
                            type_=self.types_from_db[field_raw[1]],
                            is_primary_key=True if field_raw[0] in primary_keys else False
                        ),
                    )

            return fields

    def create_table(self, table_name: str, fields: list[Column]) -> None:
        if table_name in self.get_tables():
            return None

        primary_keys: list[str] = []

        query = f"CREATE TABLE {table_name} ("

        for index, field in enumerate(fields):
            if index != len(fields) - 1:
                query += f"{field.name} {self.types_to_db[field.type_]},"
            else:
                query += f"{field.name} {self.types_to_db[field.type_]}"

            if field.is_primary_key:
                primary_keys.append(field.name)

        query += ");"

        with Connection.connect(self.postgres_dsn) as conn:
            with conn.cursor() as cursor:
                if len(primary_keys) > 0:
                    add_primary_keys_query = (
                        f"ALTER TABLE {table_name} ADD PRIMARY KEY ({", ".join(primary_keys)});"
                    )
                    cursor.execute(add_primary_keys_query)

                cursor.execute(query)

                conn.commit()

    def update_table(self, table_name: str, table_name_updated: str, differences: list[Difference]) -> None:
        if table_name not in self.get_tables():
            return None

        with (Connection.connect(self.postgres_dsn) as conn):
            with conn.cursor() as cursor:
                if table_name != table_name_updated:
                    rename_table_query = f"ALTER TABLE {table_name} RENAME TO {table_name_updated};"
                    cursor.execute(rename_table_query)

                current_primary_keys: list[str] = []
                updated_primary_keys: list[str] = []
                for difference in differences:
                    if difference.current is None:
                        add_column_query = (
                            f"ALTER TABLE {table_name_updated} ADD {difference.updated.name} "
                            f"{self.types_to_db[difference.updated.type_]}"
                        )
                        cursor.execute(add_column_query)

                        if difference.updated.is_primary_key:
                            updated_primary_keys.append(difference.updated.name)

                        continue

                    if difference.updated is None:
                        drop_column_query = (
                            f"ALTER TABLE {table_name_updated} DROP {difference.current.name};"
                        )
                        cursor.execute(drop_column_query)

                        continue

                    if difference.current.name != difference.updated.name:
                        rename_column_query = (
                            f"ALTER TABLE {table_name_updated} RENAME COLUMN {difference.current.name} TO "
                            f"{difference.updated.name};"
                        )
                        cursor.execute(rename_column_query)

                    if difference.current.type_ != difference.updated.type_:
                        change_column_type_query = (
                            f"ALTER TABLE {table_name_updated} ALTER COLUMN {difference.updated.name} TYPE "
                            f"{self.types_to_db[difference.updated.type_]};"
                        )
                        try:
                            cursor.execute(change_column_type_query)
                        except psycopg.errors.DatatypeMismatch:
                            raise ValueError(
                                f"Impossible to convert {difference.current.type_} to {difference.updated.type_}")

                    if difference.current.is_primary_key:
                        current_primary_keys.append(difference.current.name)

                    if difference.updated.is_primary_key:
                        updated_primary_keys.append(difference.updated.name)

                if current_primary_keys != updated_primary_keys:
                    drop_primary_keys_query = (
                        f"ALTER TABLE {table_name_updated} DROP CONSTRAINT {table_name_updated}_pkey"
                    )
                    primary_keys = ", ".join(updated_primary_keys)
                    add_primary_keys_query = (
                        f"ALTER TABLE {table_name_updated} ADD PRIMARY KEY ({primary_keys});"
                    )
                    if len(current_primary_keys) > 0:
                        cursor.execute(drop_primary_keys_query)
                    if len(updated_primary_keys) > 0:
                        cursor.execute(add_primary_keys_query)

                conn.commit()

    def delete_table(self, table_name: str) -> None:
        query = f"DROP TABLE {table_name}"

        with Connection.connect(self.postgres_dsn) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
