from utils import slugify, truncate


def test_slugify_basic():
    assert slugify("Hello World!") == "hello-world"


def test_slugify_special_chars():
    assert slugify("Python 3.x is great!") == "python-3x-is-great"


def test_truncate_short():
    assert truncate("Hi", 10) == "Hi"


def test_truncate_long():
    assert truncate("Long text here", 4) == "Long..."
