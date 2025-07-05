import math
import random

# Program obsługuję rejestrację studenta na stronie uczelni
# Wymaga podania prawidłowych danych
# Przy próbie podawania niepoprawnych znaków wyswietla błąd wraz z jego treścią
# W przypadku nazw własnych automatycznie zwiększa pierwszą literę
# W przypadku takich danych jak numer telefonu czy numer domu przyjmie tylko wartości liczbowe
# W przypadku podawania nazwy do e-maila automatycznie dopisuje domenę "@uczelnia.pl"
# Hasło wymaga podania przynajmniej 1 litery, cyfry oraz znaku specjalnego
# W przeciwnym razie wyświetli błąd
# Student potwierdza hasło, które musi się zgadzać z tym wcześniej podanym
# Dodatkowo program losuje dla studenta "numer albumu" z przedziału liczb 6-cyfrowych

#Kolory
COLOR_RESET = '\033[0m'
COLOR_RED = '\033[91m'
COLOR_BLUE = '\033[94m'
COLOR_GREEN = '\033[92m'

znaki_specjalne = "!@#$%^&*()<>-_=+"

def format_tekst(imie):
    return imie.capitalize() if imie.isalpha() else None

def format_tekst(nazwisko):
    return nazwisko.capitalize() if nazwisko.isalpha() else None

def format_nrtel(telefon):
    return telefon.isdigit() and len(telefon) == 9

def format_email(email):
    return email + "@uczelnia.pl" if email.isalnum() else None

def format_miasto(miasto):
    return miasto.title() if all(j.isalpha() or j in " -" for j in miasto) else None

def format_ulica(ulica):
    return ulica.title() if all(j.isalpha() or j in " -" for j in ulica) else None

def format_nrdom(nrdom):
    return nrdom if nrdom.isdigit() else None

def format_haslo(haslo):
    czy_litery = any(i.isalpha() for i in haslo)
    czy_cyfry = any(i.isdigit() for i in haslo)
#    czy_znaki_spec = any(znaki_specjalne) in haslo
#    return czy_litery and czy_cyfry and czy_znaki_spec
#    return czy_litery and czy_cyfry and if any(i in dane["Hasło"] for i in znaki_specjalne)
    return czy_litery and czy_cyfry

def rejestracja():
    dane = {}
    znaki_specjalne = "!@#$%^&*()<>-_=+"

    while True:
        imie = input("Podaj imię: ")
        dane["Imię"] = format_tekst(imie)
        if dane["Imię"]:
            break
        print(COLOR_RED+"Błąd: Imię powinno zawierać tylko litery!"+COLOR_RESET)

    while True:
        nazwisko = input("Podaj nazwisko: ")
        dane["Nazwisko"] = format_tekst(nazwisko)
        if dane["Nazwisko"]:
            break
        print(COLOR_RED+"Błąd: Nazwisko powinno zawierać tylko litery!"+COLOR_RESET)

    while True:
        telefon = input("Podaj numer telefonu: ")
        if format_nrtel(telefon):
            dane["Numer telefonu"] = telefon
            break
        print(COLOR_RED+"Błąd: Numer telefonu powinien się składać z 9 cyfr!"+COLOR_RESET)

    while True:
        email = input("Podaj nazwę dla Twojego wewnętrznego adresu e-mail: ")
        dane["Adres e-mail"] = format_email(email)
        if dane["Adres e-mail"]:
            break
        print(COLOR_RED+"Błąd: Adres e-mail powinien zawierać tylko litery i cyfry!"+COLOR_RESET)

    while True:
        miasto = input("Podaj miasto: ")
        dane["Miasto"] = format_miasto(miasto)
        if dane["Miasto"]:
            break
        print(COLOR_RED+'Błąd: Nazwy miast mogą składać się z liter, spacji oraz znaku "-"!'+COLOR_RESET)

    while True:
        ulica = input("Podaj nazwę ulicy: ")
        dane["Ulica"] = format_ulica(ulica)
        if dane["Ulica"]:
            break
        print(COLOR_RED+'Błąd: Nazwy ulic mogą składać się z liter, spacji oraz znaku "-"!'+COLOR_RESET)

    while True:
        nrdom = input("Podaj numer domu: ")
        dane["Numer domu"] = format_nrdom(nrdom)
        if dane["Numer domu"]:
            break
        print(COLOR_RED+"Błąd: Numer domu może składać się tylko i wyłącznie z cyfr!"+COLOR_RESET)

    while True:
        haslo = input("Podaj hasło: ")
        dane["Hasło"] = haslo
#        if dane["Hasło"]:
        if dane["Hasło"] and any(j in dane["Hasło"] for j in znaki_specjalne):
            break
        print(COLOR_RED+"Błąd: Hasło musi zawierać co najmniej jedną literę, cyfrę i znak specjalny!"+COLOR_RESET)

    while True:
        potwierdz_haslo = input("Potwierdź hasło: ")
        if potwierdz_haslo == dane["Hasło"]:
            break
        print(COLOR_RED+"Błąd: Podane hasła nie są identyczne!"+COLOR_RESET)

    print(COLOR_BLUE+30*"="+COLOR_RESET)
    print(COLOR_GREEN+"Student został zarejestrowany"+COLOR_RESET)
    print(COLOR_BLUE+30*"="+COLOR_RESET)
    print("Twoje dane:")
    for a, b in dane.items():
        print(f"{a}: {b}")

    album_poczatek = 100000
    album_koniec = 999999

    print("Twój numer albumu: "+str(random.randrange(album_poczatek,album_koniec)))

#rejestracja()




