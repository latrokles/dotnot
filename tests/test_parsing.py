import pytest

from dotnot import Parser, ScanError


def test_parses_multiple_strings():
    values = Parser().parse_source("'this is string one' 'this is string two'")

    assert len(values) == 2
    assert values[0] == 'this is string one'
    assert values[1] == 'this is string two'


def test_parses_multiline_strings():
    values = Parser().parse_source("'this is a string\nwith two lines'")

    assert len(values) == 1
    assert values[0] == 'this is a string\nwith two lines'


def test_parses_integers():
    assert Parser().parse_source("1_000\n10") == [1000, 10]


def test_parses_floats():
    assert Parser().parse_source("0.50\n1_000.34") == [0.5, 1000.34]


def test_parses_words():
    assert Parser().parse_source("t f nil") == ['t', 'f', 'nil']


def test_raises_scan_error_on_unterminated_strings():
    with pytest.raises(ScanError):
        Parser().parse_source("'this is a bad string")
