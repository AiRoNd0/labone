

string = input("Enter a string: ")
lower_count = 0
upper_count = 0
for char in string:
    if char.islower():
        lower_count += 1
    elif char.isupper():
        upper_count += 1

if lower_count >= upper_count:
    print(string.lower())
else:
    print(string.upper())
