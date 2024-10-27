# DB Viewer

### Зависимости 
  - Python 3.12 (для самостоятельной сборки или запуска без компиляции)
  - PostgreSQL 16 (таблицы берутся из public схемы указанной БД)

### Как установить собранное приложение
1) Скачать DBViewer-v.0.0.1.zip из Releases
2) Запустить DBViewer.exe

### Как собрать приложение самостоятельно
1) Клонировать репозиторий и настроить окружение
```
git clone https://github.com/wnkbll/fastapi-backend.git
cd fastapi-backend
python -m venv venv
venv/Scripts/activate.ps1
pip install -r requirements.txt
```
2) Скомпилировать приложение с помощью `nuitka`
```
nuitka --standalone --windows-console-mode=disable --plugin-enable=pyside6 src/main.py
```
3) Запустить `main.exe` из `main.dust`
