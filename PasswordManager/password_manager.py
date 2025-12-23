computer_password = "hello123"

main_pwd = input("What is the main password? ")

if main_pwd!= computer_password:
    print("Incorrect password. Access denied.")
    exit()

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            
def add():
    name = input("Enter the user name: ")
    pwd = input("Enter the password: ")

    with open('passwords.txt','a') as f:
        f.write(name + '|' + pwd + '\n')
        print("Password added successfully.")

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
