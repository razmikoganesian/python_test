# DICTIONARY
tea_prices_eur = {"Masala tea": 40,
                  "Lemon tea": 15,
                  "Ice tea": 10
                  }



tea_prices_usd = {tea:price * 0.88 for tea, price in tea_prices_eur.items()}
print(tea_prices_usd)