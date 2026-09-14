studs = {} #ts stands for students not actual studs

while True:
    print("___ATTENDANCE MON SYSTEM___")
    print("1. Add student")
    print("2. Mark attendance")
    print("3. View attendance")
    print("4. Exit")
    print("____________________________")

    try:
        choice = int(input("Enter choice: "))  #the choice mentioned in multiple args

        if choice == 1:
            name = input("Enter Student name: ")

            if name == "":   #stops user from entering a no name idk
                print("Name can't be empty")
            elif name in studs:
                print(name, "is already here.") #stops user from entering the same name
            else:
                studs[name] = "Not marked"
                print("Student added.")
                
        elif choice == 2:
            name = input("Enter student name: ")
            
            if name in studs:   #checks if student exists
                status = input("Present or Absent: ").lower()

                if status == "present":     #marks student present if present is typed
                    studs[name] = "Present"
                elif status == "absent":   #same here vruv
                    studs[name] = "Absnet"
                else:
                    print("Invalid")
            else:
                print("Student not found") #shows when student aint present?

        elif choice == 3:
            if not studs:  #if there's nothing in the studs dict, this code runs
                print("No students")
            else:            
                for name, status in studs.items(): #but if there is, it prints the name and status if absent/presnet
                    print(name, "-", status)

        elif choice == 4:
            break

    except ValueError:
        print("Invalid choice")
        continue