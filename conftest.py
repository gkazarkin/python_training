import pytest
from fixture.application import Application
import datetime
import json
import os.path

# Предварительно запустить локальный сервер "XAMPP Control Panel"
fixture = None
target = None

'''Инициализатор фикстуры'''
@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        # 1- выясняем абсолютный путь до проекта и подклеиваем к нему нужный путь
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        # Здесь может падать, так как ищет target.json в другой папке, для этого надо указать папку проекта в Edit Configuration, Working directory
        # Или надо запускать из консоли из папки проекта, а не тестов
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["baseUrl"])
    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture

# Фикстура остановки
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):  # Передаётся парсер командной строки
    parser.addoption("--browser", action="store", default="chrome")  # Доступ передаётся через объект request
    parser.addoption("--target", action="store", default="target.json")  # Доступ передаётся через объект request



