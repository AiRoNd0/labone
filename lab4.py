#seidakhmetov abylaikhan
#01.06.2003 IT computer science lab 7:50 func
#komment moment


# text = "Hello, World!"

# # 1. len()
# print("длина:", len(text))

# # 2. upper()
# print("капсом:", text.upper())

# # 3. lower()
# print("мелкими:", text.lower())

# # 4. count()
# print("сколько в тексте букв 'l':", text.count('l'))

# # 5. replace()
# print("поменять 'Hello' на 'Hi':", text.replace('Hello', 'Hi'))

# # 6. split()
# print("метод сплит:", text.split('r'))

# # 7. strip()
# text_with_whitespace = "   Hello, World!   "
# print("лишить пробелов:", text_with_whitespace.strip())

# # 8. startswith()
# print("метод Startswith на 'Hello':", text.startswith('Hello'))

# # 9. endswith()
# print("метод Ends with '!':", text.endswith('!'))

# # 10. find()
# print("индекс 'r' находится:", text.find('r'))






# students = []

# while True:
#     student = input("Напишите имя студента и его класс через запятую (в случае окончания введите q): ")
#     if student == 'q':
#         break
#     name, grade = student.split(',')
#     students.append((name, int(grade)))
    
# students.sort(key=lambda x: x[1])

# for student in students:
#     print("Имя: {} Его класс: {}".format(student[0], student[1]))





# string = input("Введите слово или предложение: ")
# lower_count = 0
# upper_count = 0
# for char in string:
#     if char.islower():
#         lower_count += 1
#     elif char.isupper():
#         upper_count += 1

# if lower_count >= upper_count:
#     print(string.lower())
# else:
#     print(string.upper())







while True:
    first_num = input("Enter the first number: ")
    second_num = input("Enter the second number: ")
    if first_num.isdigit() and second_num.isdigit():
        print("The sum of the numbers is:", int(first_num) + int(second_num))
        break
    else:
        print("Incorrect input, please enter a valid number.")
