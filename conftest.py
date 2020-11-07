import pytest
from fixture.application import Application

# inicializator fixtyri
@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    # ykazanie na to, kak razrushit fixtyry
    request.addfinalizer(fixture.destroy)
    return fixture
