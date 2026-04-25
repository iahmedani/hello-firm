import pytest

from hello_firm import greet


def test_greet_returns_hello_world():
    # FR-1, FR-2, AC-1
    assert greet("World") == "Hello, World"


def test_greet_raises_typeerror_on_int():
    # FR-3, AC-2
    with pytest.raises(TypeError):
        greet(42)


def test_greet_raises_typeerror_on_none():
    # spec edge case: None
    with pytest.raises(TypeError):
        greet(None)
