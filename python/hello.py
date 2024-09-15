x=(input("enter your name : "))
y=int(input("enter your favorite number1: "))
z=int(input("enter your favorite number2: "))
i=int(input("enter your favorite number3: "))
numbers=[y,z,i]
print(f"Hello {x},Let's explore the numbers you entered.\n{numbers}")
for num in numbers:
    if num % 2 == 0:
        print(f"the number {num} is even.")
    else:
        print(f"the number {num} is odd.")            
for number1 in numbers:
    number=int(number1)
    square=number**2
    print(f"the number {number1} and it's square is {square}.")