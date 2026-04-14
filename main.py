balance = 5000
items = {"apple": 1, "banana": 1, "orange": 1, "grapes": 3, "watermelon": 7,
    "bread": 3, "bagel": 2, "croissant": 3, "muffin": 2, "donut": 1,
    "milk": 3, "cheese": 4, "yogurt": 2, "butter": 3, "eggs": 4,
    "chicken": 8, "beef": 10, "pork": 7, "fish": 9, "shrimp": 12,
    "rice": 2, "pasta": 2, "cereal": 4, "oatmeal": 3, "flour": 2,
    "soda": 2, "juice": 3, "water bottle": 1, "coffee": 5, "tea": 4,
    "chips": 2, "crackers": 2, "cookies": 3, "candy": 1, "chocolate": 2,

    # Household
    "toilet paper": 5, "paper towels": 4, "soap": 2, "shampoo": 4,
    "conditioner": 4, "toothpaste": 3, "toothbrush": 2, "detergent": 6,
    "sponges": 2, "trash bags": 4, "light bulb": 2, "batteries": 5,
    "cleaning spray": 4, "dish soap": 3, "laundry pods": 7,

    # Tools
    "hammer": 10, "screwdriver": 6, "wrench": 8, "pliers": 7,
    "drill": 40, "nails": 3, "screws": 3, "tape measure": 5,
    "saw": 15, "flashlight": 8, "toolbox": 25,

    # Clothing
    "t-shirt": 10, "jeans": 25, "jacket": 40, "socks": 5, "shoes": 30,
    "hat": 8, "scarf": 7, "gloves": 6, "belt": 10, "hoodie": 25,

    # Electronics
    "phone charger": 12, "headphones": 20, "earbuds": 15,
    "keyboard": 25, "mouse": 15, "monitor": 120, "flash drive": 10,
    "power strip": 12, "webcam": 30, "speaker": 35,

    # Gaming
    "controller": 50, "game disc": 30, "gaming mouse": 40,
    "gaming keyboard": 60, "gaming headset": 70,

    # Office Supplies
    "notebook": 3, "pen": 1, "pencil": 1, "marker": 2, "highlighter": 2,
    "stapler": 6, "tape": 2, "glue": 2, "folder": 1, "binder": 4,

    # Miscellaneous
    "umbrella": 10, "wallet": 15, "backpack": 25, "water bottle": 8,
    "sunglasses": 12, "keychain": 3, "blanket": 20, "pillow": 15,
    "candle": 5, "notepad": 2, "deck of cards": 4, "board game": 20,

    # Luxury / High‑End
    "smartphone": 600, "laptop": 900, "tablet": 300,
    "smartwatch": 200, "camera": 500, "tv": 400,}


while balance > 0:
    print(f"Your balance is ${balance}")
    purchase = input("What will you purchase?: ").lower()


    if purchase not in items:
        print("That item doesn't exist.")
        print(f"Your balance is ${balance}")
        continue

    price = items[purchase]

    if balance >= price:
        balance -= price
        print(f"You purchased {purchase} for ${price}")
        print(f"Your new balance is ${balance}")
    else:
        print(f"You can't afford that")
        print(f"Your balance is ${balance}")


