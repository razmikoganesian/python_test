import dis

from test.support import use_resources


users = [
    {"id": 1, "total": 200, "coupon": "p2121" },
    {"id": 2, "total": 404, "coupon": "p2122" },
    {"id": 3, "total": 500, "coupon": "p2123" }
]

discounts = {
    "p2121": (0.3,0),
    "p2122": (0.5,0),
    "p2123": (0.1,10)
}

for user in users: 
    percent, fixed = discounts.get(user["coupon"], (0,0)) # default value
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and next time will has got a discount {discount}")

