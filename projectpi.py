import string
def main():
    print("Thank you for using Project PI:")
    print("A coding project made by @u.perceus_adalian")
    print("")
    try:
        while True:
            response = int(input("Select an Operation Type [1 = Add, 2 = Subtract, 3 = Multiply, 4 = Divide]: "))
            if response < 1 or response > 4:
                print("Invalid integer, please try again.")
                continue
            try: 
                x = int(input("Operand 1 = "))
                y = int(input("Operant 2 = "))

                if response == 1:
                    print(x," + ",y," = ",x+y)
                    continue
                if response == 2:
                    print(x," - ",y," = ",x-y)
                    continue
                if response == 3:
                    print(x," * ",y," = ",x*y)
                    continue
                if response == 4:
                    print(x," / ",y," = ",x/y)
                    continue
            except ValueError:
                print("Operand is a String. Please Try Again.")
                continue
    except ValueError:
        print("Operation Type is a String. Please Try Again.") 
main()

