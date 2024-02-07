import time

while True:
    print("\33[31m")
    print("""

 $$$$$$\            $$\                     $$\            $$\                         
$$  __$$\           $$ |                    $$ |           $$ |                        
$$ /  \__| $$$$$$\  $$ | $$$$$$$\ $$\   $$\ $$ | $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  
$$ |       \____$$\ $$ |$$  _____|$$ |  $$ |$$ | \____$$\\_$$  _|  $$  __$$\ $$  __$$\ 
$$ |       $$$$$$$ |$$ |$$ /      $$ |  $$ |$$ | $$$$$$$ | $$ |    $$ /  $$ |$$ |  \__|
$$ |  $$\ $$  __$$ |$$ |$$ |      $$ |  $$ |$$ |$$  __$$ | $$ |$$\ $$ |  $$ |$$ |      
\$$$$$$  |\$$$$$$$ |$$ |\$$$$$$$\ \$$$$$$  |$$ |\$$$$$$$ | \$$$$  |\$$$$$$  |$$ |      
 \______/  \_______|\__| \_______| \______/ \__| \_______|  \____/  \______/ \__|      
                                                                                       
    """)
    print("Welcome to my calculator")
    print("1 - Addition \n2 - Subtraction \n3 - Multiplication \n4 - Division \n5 - Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print("Solution:", result)
    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print("Solution:", result)
    elif choice == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print("Solution:", result)
    elif choice == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("Division by zero is not possible")
        else:
            result = num1 / num2
            print("Solution:", result)
    elif choice == "5":
        print("Goodbye!")
        time.sleep(1)
        break
    else:
        print("Invalid input. Please choose one of the given options.")
