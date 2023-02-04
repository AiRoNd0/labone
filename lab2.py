#seidakhmetov abylaikhan
#01.06.2003 IT computer science lab 7:50 func
#komment moment
var_1 = int(input("Введите число: "))
agregator = []
for i in range(1, var_1+1):
    print(i, sep=" ", end=" ")
    if i < var_1:
        print("+", sep=" ", end=" ")
    agregator.append(i)
    
    
    

print("=", sum(agregator))