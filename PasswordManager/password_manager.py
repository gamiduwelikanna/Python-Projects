main_pwd = input("What is the main password? ")


def view():
    pass

def add():
    pass

while True:
    mode = input("Would you like to view and existing password or add a new password? (view/add) or type 'q' to exit: ").lower()

    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode.")
        continue
whdkqwhdk