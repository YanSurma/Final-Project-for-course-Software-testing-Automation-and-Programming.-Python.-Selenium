import pytest


@pytest.fixture()
def set_up():
    print('Start test')
    yield
    print('Finish test')


# Данная фикстура будет отрабатываться для всех тестов, что хранится в нашем файле с тестами (в нашем модуле)
@pytest.fixture(scope="module")
def set_group():
    print('Enter system')
    yield
    print('Exit system')
