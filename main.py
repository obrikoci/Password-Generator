import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many latters do you want in your password?\n"))
for letter in range(nr_letters):
  password.append(random.choice(letters))
  if nr_letters == 0:
    break
nr_numbers = int(input("How many numbers would you like in your passowrd?\n"))
for number in range(nr_numbers):
  password.append(random.choice(numbers))
  if nr_numbers == 0:
    break
nr_symbols = int(input("How many symbols would you like in your password?\n"))
for symbol in range(nr_symbols):
  password.append(random.choice(symbols))
  if nr_symbols == 0:
    break
random.shuffle(password)
new_password = "".join(password)
print (f"Here is your password: {new_password}")

