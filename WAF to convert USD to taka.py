from fractions import Fraction

usd_val = Fraction(input("enter the amount of USD: "))
amount = Fraction(input("enter the value of taka: "))

def convreter(usd_val, amount):
    taka = usd_val * amount
    print(usd_val, "USD =", taka, "Taka")

convreter(usd_val, amount)
