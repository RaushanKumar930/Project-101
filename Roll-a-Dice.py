import random
response = "y"

def dice(no):
    if no == 1: 
        print("[     ]")
        print("[  0  ]")
        print("[     ]")

    if no == 2: 
        print("[    0]")
        print("[     ]")
        print("[0    ]")

    if no == 3: 
        print("[    0]")
        print("[  0  ]")
        print("[0    ]")

    if no == 4: 
        print("[0   0]")
        print("[     ]")
        print("[0   0]")

    if no == 5: 
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")

    if no == 6: 
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")

while response == 'y': 
    response = input("Press 'y' to roll a dice and 'n' to exit: ")
    if response == "y": 
        no = random.randint(1,6)
        dice(no)
    else: 
        print("Thank You!")
