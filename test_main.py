"""Unit tests for goodhello module."""


from goodhello import bye, greet, hello


def test_hello_returns_none():
    """Verify hello returns None."""
    assert hello() is None


def test_bye_returns_none():
    """Verify bye returns None."""
    assert bye() is None


def test_greet_returns_none():
    """Verify greet returns None."""
    assert greet() is None


def test_hello_prints_expected_text(capsys):
    """Verify hello returns correct message."""
    hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, DevOps learner!"


def test_bye_prints_expected_text(capsys):
    """Verify bye returns correct message."""
    bye()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Goodbye!"
