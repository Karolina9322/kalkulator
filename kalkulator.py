
import logging
logging.basicConfig(level=logging.DEBUG)

BPurple="\033[1;35m" 
end = "\033[0m"

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def calculator():

    """
    Prosty kalkulator zwracający wynik działania wybranego przez użytkownika:
    1 - Dodawanie, 2 - Odejmowanie, 3 - Mnożenie, 4 - Dzielenie
    Po wybraniu rodzaju działania, użytkownik jest proszony o podanie składników działania.
    Następnie obliczany jest wynik działania z dokładnością do 2 miejsc po przecinku.
    """

    action = input(f"""Podaj działanie, posługując się odpowiednią liczbą: {BPurple}1{end} Dodawanie, {BPurple}2{end} Odejmowanie, {BPurple}3{end} Mnożenie, {BPurple}4{end} Dzielenie: """)

    a = float(input(f"Podaj składnik 1: "))
    b = float(input(f"Podaj składnik 2: "))

    if __name__ == "__main__":
        if action == '1':
            logging.info = input(f"Dodaję: {a} i {b}")
            add(a,b)
            print(f"Wynik to: {(add(a,b)):.2f}")
            exit()
        elif action == '2':
            logging.info = input(f"Odejmuję: {a} od {b}")
            subtract(a,b)
            print(f"Wynik to: {subtract(a,b):.2f}")
            exit()
        elif action == '3':
            logging.info = input(f"Mnożę: {a} i {b}")
            multiply(a,b)
            print(f"Wynik to: {multiply(a,b):.2f}")
            exit()
        elif action == '4':
            logging.info = input(f"Dzielę: {a} przez {b}")
            divide(a,b)
            print(f"Wynik to: {divide(a,b):.2f}")
            exit()     

print(calculator())
