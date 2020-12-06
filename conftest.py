import pytest
from fixture.application import Application
import datetime
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture

'''Предварительно запустить локальный сервер "XAMPP Control Panel" '''
fixture = None
target = None

"""Вспомогательная функция, занимается загрузкой"""
def load_config(file):
    global target
    if target is None:
        '''Загрузка конфигурации с кешированием'''
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        '''Здесь может падать, так как ищет target.json в другой папке, для этого надо указать папку проекта в Edit Configuration, Working directory
        Или надо запускать из консоли из папки проекта, а не тестов'''
        with open(config_file) as f:
            target = json.load(f)
    return target


"""Инициализатор фикстуры"""
@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture


"""Фикстура для работы с базой данных MySQL"""
@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"], password=db_config["password"])

    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


'''Фикстура остановки'''
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")

"""Передаётся парсер командной строки
Доступ передаётся через объект request
Доступ передаётся через объект request"""
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    """При store_true автоматически опция False если отсутствует и True если есть"""
    parser.addoption("--check_ui", action="store_true")


"""Динамическое связывание тестовой функции с данными,
через объект metafunc можно получить информацию о тестовой функции"""
def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:  # Пробегаем по всем параметрам
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])  # Обрезаем первые 5 символов
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])  # Используем данные, чтобы параметризовать функцию
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


'''Выясняем абсолютный путь до проекта и подклеиваем к нему нужный путь до файла'''
def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        """Читаем и перекодируем обратно в исходный формат в виде объекто Python"""
        return jsonpickle.decode(f.read())




