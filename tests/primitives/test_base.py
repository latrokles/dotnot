from dotnot.primitives import Symbol, fmt


def test_fmt():
    assert fmt(None)  == 'nil'
    assert fmt(True)  == 't'
    assert fmt(False) == 'f'
    assert fmt(3.14)  == '3.14'
    assert fmt('h')   == "'h'"
    assert fmt((1, 2)) == 'tuple{ 1 2 }'
    assert fmt([1, 2]) == 'list{ 1 2 }'
    assert fmt({'a': 1}) == "hashtable{ 'a' 1 }"
    assert fmt(Symbol.make('foo')) == '#foo'
