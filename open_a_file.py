

employee_file = open("employees1.txt", "a")
print(employee_file.readable())
#print(employee_file.read())
employee_file.write(input("\nEnter some text"))
employee_file.close()