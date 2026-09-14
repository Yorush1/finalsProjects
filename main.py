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

            if name == "":               #stops user from entering a no name idk
                print("Name can't be empty")
            elif name in studs:
                print(name, "is already here.")
            else:
                studs[name] = "Not marked"
                print("Student added.")
                
        elif choice == 2:
            name = input("Enter student name: ")
            
            if name in studs:
                stats = input("Present or Absent: ").lower()

                if stats == "present":
                    studs[name] = "Present"
                elif stats == "absent":
                    studs[name] = "Absnet"
                else:
                    print("Invalid")
            else:
                print("Student not found") #shows when student aint present?

        elif choice == 3:
            if not studs:
                print("No students")
            else:
                for name, stats in studs.items():
                    print(name, "-", stats)

        elif choice == 4:
            break

    except ValueError:
        print("Invalid choice")
        continue