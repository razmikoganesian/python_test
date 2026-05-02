market_menu = {"ukrop": 20,
             "chanah" : 45,
             "hinkal" : 60
             }
try:
    market_menu['luk']
except KeyError:
    print("Luk didn't found on market")


