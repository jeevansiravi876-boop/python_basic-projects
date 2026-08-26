import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','@','#','$','%','^','&','*','+','-']

print("Welcome to the password generator !")

nr_letters = int(input("how many letters would you like in your password?\n"))
nr_symbols = int(input(f"how many symbols would you like?\n"))
nr_numbers = int(input(f"how many numbers would you like\n"))

choice = str(input("for password easy to crack by hackers press e\nor for tougher one to crack by hackers press h : "))
if choice == "e":
    #easy way
    password = ""

    for char in range (0,nr_letters):
        random_char = random.choice(letters)
        password += random_char

    for list in range(0,nr_symbols):
        random_symbol = random.choice(symbols)
        password += random_symbol
    
    for int in range(0,nr_numbers):
        random_no = random.choice(numbers)
        password += random_no

    print(password)

else:
# hard way {suffle of everything}

    password_list = []

    for char in range (1,nr_letters+1):
        password_list.append(random.choice(letters))

    for list in range(1,nr_symbols+1):
        password_list.append(random.choice(symbols))

    for int in range(1,nr_numbers+1):
        password_list.append(random.choice(numbers))

    print("characters used in your password are:")
    print(password_list)
    random.shuffle(password_list)
    print(password_list)

#converting list to string again to get desire result till now we have done work in backend now frontend
  
    password =""
    for char in password_list:
        password += char

    print(f"your password is : {password}")
