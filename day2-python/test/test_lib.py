from lib import Range, parse_input


def test_parse_input():
    example = "11-22,95-115,998-1012"
    expected = [Range(11, 22), Range(95, 115), Range(998, 1012)]
    assert parse_input(example) == expected
