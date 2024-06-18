#Write a program that copies the contents of one text file to another.

user_input = input("Enter a string: ")
with open("C:/Users/Dell/Downloads/IGDTUW ph &Ml/Ass. Q5.txt", "w") as file:
    file.write(user_input)

print("The string has been written to output.txt")

with open("C:/Users/Dell/Downloads/IGDTUW ph &Ml/Ass. Q5.txt", "r") as file:

    content = file.read()
print(content)