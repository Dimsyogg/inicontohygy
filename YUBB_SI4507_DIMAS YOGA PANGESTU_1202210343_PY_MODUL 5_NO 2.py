set = {}

while True:
    print("====MENU====")
    print("1. Register a new Resident \n2. Check the Address of Resident \n0. Exit")
    try:
        menu = int(input("Choose a Menu : "))

        if menu == 1:
            print("---Register a new Resident---")
            name = input("Input name of the Resident that you want to add : ")
            address = input("Input address of the Resident that you want to add : ")
            print ("Success, data has been added to database")
            set[name] = address

        elif menu == 2:
            print("---Check the Address of Resident---")
            name = input("Input name of the Resident that you want to check : ")
            print (f"address of the resident named {name} located in : ",set[name])
            break

        elif menu == 0:
            print ("Program has ended")
            break

    except ValueError:
        print("Input Menu should be Integer")
        break

    except KeyError:
        print("The Resident no registered yet")
        break

    finally:
        print()