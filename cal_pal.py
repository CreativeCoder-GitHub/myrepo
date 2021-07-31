def calc(c_type, num1, num2):
    if c_type == "a":
        print(num1 + num2)
    elif c_type == "s":
        print(num1 - num2)
    elif c_type == "m":
        print(num1 * num2)
    elif c_type == "d":
        print(num1 / num2)
    elif c_type == "md":
        print(num1 % num2)
    elif c_type == "fd":
        print(num1 // num2)

print("""a. addition
s. subtraction
m. multiplication
d. division
fd. quotient
md. remainder""")
calc(input("Enter the type of calculation: "), int(input("First number: ")), int(input("Second number: ")))
