import string
import random

characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_pass():
    password_lenght = int(input('How long do you want the password?: '))
    
    random.shuffle(characters)

    password = []

    for x in range(password_lenght):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)


option = input("Do you want to generate a password? (Yes/No): ")


if option == 'Yes':
    generate_pass()
elif option == 'No':
    print('Program ended')
    quit()
else: 
    print("Invalid input, should be Yes or No")
    quit()