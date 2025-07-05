import pytest
import rejestracja

def test_format_tekst():
    assert rejestracja.format_tekst("adam") == "Adam"
    assert rejestracja.format_tekst("ADAM") == "Adam"
    assert rejestracja.format_tekst("AdaM") == "Adam"
    assert rejestracja.format_tekst("ada123") is None

def test_format_nrtel():
    assert rejestracja.format_nrtel("123456789") is True
    assert rejestracja.format_nrtel("12345678") is False
    assert rejestracja.format_nrtel("123456789a") is False

def test_format_email():
    assert rejestracja.format_email("student123") == "student123@uczelnia.pl"
    assert rejestracja.format_email("student_123") is None
    assert rejestracja.format_email("student 123") is None

def test_format_miasto():
    assert rejestracja.format_miasto("Warszawa") == "Warszawa"
    assert rejestracja.format_miasto("nowy sącz") == "Nowy Sącz"
    assert rejestracja.format_miasto("Łódź-Śródmieście") == "Łódź-Śródmieście"
    assert rejestracja.format_miasto("Bydgoszcz123") is None

def test_format_ulica():
    assert rejestracja.format_ulica("Mickiewicza") == "Mickiewicza"
    assert rejestracja.format_ulica("Jana Pawła II") == "Jana Pawła Ii"
    assert rejestracja.format_ulica("ul. Wolności") is None

def test_format_nrdom():
    assert rejestracja.format_nrdom("10") == "10"
    assert rejestracja.format_nrdom("1a") is None

def test_format_haslo():
    assert rejestracja.format_haslo("abc123") is True
    assert rejestracja.format_haslo("abc") is False
    assert rejestracja.format_haslo("123") is False
    assert rejestracja.format_haslo("!@#") is False