# Kirjoita postinumerot-moduulin testit tähän tiedostoon
from postinumerot import get_postal_numbers


def test_find_korvatunturi():
    assert get_postal_numbers('KORVATUNTURI') == '99999'