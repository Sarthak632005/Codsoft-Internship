import math


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."
    
def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def log(x, base=10):
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))


history = []

def add_to_history(expression, result):
    history.append(f"{expression} = {result}")

def show_history():
    if history:
        print("Calculation History:")
        for record in history:
            print(record)
    else:
        print("No history available.")

def clear_history():
    global history
    history = []
    print("History cleared.")

def save_session(filename="calculator_session.txt"):
    with open(filename, 'w') as file:
        for item in history:
            file.write(f"{item}\n")
    print(f"Session saved to {filename}")

def load_session(filename="calculator_session.txt"):
    try:
        with open(filename, 'r') as file:
            loaded_history = file.readlines()
            for item in loaded_history:
                history.append(item.strip())
        print(f"Session loaded from {loaded_history}")
    except FileNotFoundError:
        print(f"File {filename} not found.")




def calc ():
    print ("Which operation do you want to perform.\nInput the number of operation")

    print("\n1. Addition","2. Substraction".rjust(30))
    print("3. Multiplication","4. Division".rjust(20))
    print("5. Powere/Raised To","6. Logarithmic".rjust(21))
    print("7. SquareRoot ","8. Factorial".rjust(24))
    print("9. Sine ()" , "10. Cosine ()".rjust(29))
    print("11. Show History", "12. Clear History".rjust(27))
    print("13. Save Session", "14. Load Session".rjust(27))


    while True:
        a = int (input ("\nwhich operation :- "))

        if a in (7,8,9,10):
            b= float(input("Enter the number: "))

            if a == 7:
                print ("Square Root of" , b, "=",sqrt (b))
                x=sqrt (b)
                add_to_history(f"Square root of {b}", x)
            elif a == 8:
                print ( b,"!", "=",factorial (b))
                x=factorial (b)
                add_to_history(f"{b}!", x)
            elif a == 9:
                print ("Sin" , b , "=",sine (b))
                x=sine (b)
                add_to_history(f"Sine{b} ", x)
            elif a == 10:
                print ("Cos" , b, "=",sine (b))
                x=cosine (b)
                add_to_history(f"Cos {b}", x)

        else:
            pass

        if a in (1,2,3,4,5,6):
            b = float(input("Enter first number: "))
            c = float(input("Enter second number: "))

            if a == 1:
                print (b,"+",c,"=",add (b,c))
                x=add (b,c)
                add_to_history(f"{b} + {c}", x)
            elif a == 2:
                print (b,"-",c,"=",subtract(b,c))
                x=subtract (b,c)
                add_to_history(f"{b} - {c}", x)
            elif a == 3:
                print (b,"X",c,"=",multiply(b,c))
                x=multiply (b,c)
                add_to_history(f"{b} X {c}", x)
            elif a == 4:
                print (b,"/",c,"=",divide(b,c))
                x=divide (b,c)
                add_to_history(f"{b} / {c}", x)
            elif a == 5:
                print (b,"^",c,"=",power(b,c))
                x=power (b,c)
                add_to_history(f"{b} ^ {c}", x)
            elif a == 6:
                print ("Log of", b ,"of base", c ,"=",(b,c))
                x=log (b,c)
                add_to_history(f"{b} Log {c}", x)

        elif a == 11:
            show_history()
        elif a == 12:
            clear_history()
        elif a == 13:
            save_session()
        elif a == 14:
            load_session()

        else :
            print ("invalid operation")

        reuse = input("Do you want to perform another calculation or see/delete History? (yes/no): ")
        if reuse.lower() != 'yes':
            break

calc ()
    
