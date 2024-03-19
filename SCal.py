def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    if b == 0:
        print("float division by zero")
        return None
    else:
        return a / b

def multiplication(a, b):
    return a * b

def power(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    else:
        return a % b

def reset():
    print("0$")
    return None

def select_op(choice, a, b):
    if choice == "#":
        
        return -1
    elif choice == "+":
        
        return addition(a, b)
    elif choice == "-":
       
        return subtraction(a, b)
    elif choice == "*":
        
        return multiplication(a, b)
    elif choice == "/":
       
        return division(a, b)
    elif choice == "^":
       
        return power(a, b)
    elif choice == "%":
       
        return remainder(a, b)
    else:
        print("Unrecognized operation")
        return None

def get_number_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
         
            return None
        except EOFError:
            print("Input interrupted, please try again.")
            return None

# Main loop
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    
    if choice == "#":
        
        print("Done. Terminating")
        break
    elif choice == "$":
        reset()
  
    else:
        try:
            a = get_number_input("Enter first number: ")
            
            if a is None:
                print("0$")
                continue
            print(int(a))
            b = get_number_input("Enter second number: ")
            
            if b is None:
                print("0$")
                continue
            print(int(b))
           
            result = select_op(choice, a, b)
            print(a,choice,b,"=",result)
        except ValueError as e:
            print("Error:", e)
