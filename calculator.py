## Creating a Calculator:-

while True: ## looping forever (Notice it)

    option = input ("enter 'add', 'subtract', 'divide', 'multiply', 'power', 'quit'")

    if option == 'quit':

        break

    elif option == "add":

        a = int(input("enter a number 1:-"))

        b = int(input("enter  a number 2:-"))
        print ( a + b )

    elif option == "subtract":

        a = int(input("enter a number 1:-"))

        b = int(input("enter a number 2:-"))

        print ( a-b )

    elif option == "divide":

        a = int(input("enter a number 1:-"))

        b = int(input("enter a number 2:-"))

        print ( a/b )

    elif option == "multiply":

        a = int(input("enter a number 1:-"))

        b = int(input("enter a number 2:-"))

        print ( a*b )

    elif option == "power":

        a = int(input("enter a number 1:-"))

        b = int(input("enter a number 2:-"))

        print ( a**b )

    else:

        print ("invalid key")
        

print ("i'm out of calculator")





