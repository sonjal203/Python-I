def usd_to_eur(usd_amount):
    exchange_rate = 0.85  # 1 USD is equal to 0.85 EUR
    eur_amount = usd_amount * exchange_rate
    return eur_amount
def eur_to_usd(eur_amount):
    exchange_rate = 1.18  # 1 EUR is equal to 1.18 USD
    usd_amount = eur_amount * exchange_rate
    return usd_amount

# Test the functions
usd_amount = 100
eur_amount = usd_to_eur(usd_amount)
print(f"{usd_amount} USD is equal to {eur_amount} EUR")

eur_amount = 80
usd_amount = eur_to_usd(eur_amount)
print(f"{eur_amount} EUR is equal to {usd_amount} USD")