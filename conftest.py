import pytest
from fixture.application import Application
import datetime

# Предварительно запустить локальный сервер "XAMPP Control Panel"
fixture = None

# Инициализатор фикстуры
@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login(username="admin", password="secret")
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
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")  # Доступ передаётся через объект request



