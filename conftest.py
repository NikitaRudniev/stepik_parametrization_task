import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Select language from the list: ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-cn")


@pytest.fixture(scope="function")
def browser(request):
    selected_language = request.config.getoption("language")
    opts = Options()
    opts.add_experimental_option('prefs', {'intl.accept_languages': selected_language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=opts)
    yield browser
    print("\nquit browser..")
    browser.quit()