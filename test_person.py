# test_person.py
import pytest
from person import Person

def test_categorize_age():
    person = Person()
    assert person.categorize_age(-1) == "Edad Invalida"
    assert person.categorize_age(0) == "Bebé"
    assert person.categorize_age(12) == "Niño"
    assert person.categorize_age(13) == "Puberto"
    assert person.categorize_age(19) == "Adolecente"
    assert person.categorize_age(20) == "Adulto joven"
    assert person.categorize_age(64) == "Adult"
    assert person.categorize_age(65) == "Adulto de la tercer edad"
