import pytest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, result', [(1,1), (2,4), (3,9)] )
def test_several_numbers(number: int, result: int):
    assert number ** 2 == result

@pytest.mark.parametrize('os', ['macos', 'windows', 'linux,', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiolication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0