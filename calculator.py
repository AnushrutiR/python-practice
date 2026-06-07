n1=float(input("Enter first number:"))
n2=float(input("Enter second number:"))
def add():
    a=n1+n2
    print(a)
    print("Numbers added successfully")
def subtract():
    s=n1-n2
    print(s)
    print("Numbers subtracted successfully")
def multiply():
    m=n1*n2
    print(m)
    print("Numbers multiplied successfully")
def division():
    d=n1/n2
    print(d)
    print("Numbers divided successfully")
while True:
     print("\n1. Add numbers")
     print("2. Subtract numbers")
     print("3. Multiply numbers")
     print("4. Divide numbers")
     print("5. Quit")
     choice=input("Enter your choice:")
     if choice == "1":
          add()
     elif choice == "2":
          subtract()
     elif choice == "3":
          multiply()
     elif choice=="4":
          division()
     else:
          break
