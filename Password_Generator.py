import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', ';',]
numbers = [1,2,3,4,5,6,7,8,9,0]
password = []
print("Welcome to PyPassword Generator")
n_letters = int(input("How many letters would you like in you password\n"))
n_symbols = int(input("How many symbols would you like\n"))
n_numbers = int(input("How many numbers would you like\n"))

for n in range(0,n_letters):
    ran_char = random.choice(letters)
    password += ran_char
    

for n in range(0,n_symbols):
    ran_char = random.choice(symbols)
    password += ran_char    

for n in range(0,n_numbers):
    ran_char = str(random.choice(numbers))
    password += ran_char

print(random.shuffle(password))
finalPass = ""
for n in password:
    finalPass += n

print(f"Your password is: {finalPass}")