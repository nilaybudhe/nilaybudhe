student= {}

while True:
   print("\n Menu")
   print("1.Add New student information")
   print("2.Update exiting student Grade")
   print("3.Display All Student Name and Grade")
   print("4. Exit")

   choice= input ("Enter the number from Menu:  ")
   if choice == "1":
      name = input ("Enter the name: ")
      grade = input ("Enter the Grade: ")
      student[name]= grade
      print(f"{name} added successfully")
   elif choice == "2":
        name = input ("Enter the student name to update the grade : ")
        if name in student :
            grade = input ("Enter the new Grade for student : ")
            student[name] = grade
            print(f"{name} Grade is updated")
        else:
            print("Student information not found")
   elif choice =="3":  
        if student :
            print ("\n Display All student information :" )
            for name, grade in student.items():
                print (f"{name}: {grade}")
        else:
            print("Student information not found in database")
   elif choice == "4":
        print("Enter the choice from 1-3, Thank you !")
        break
   else:
        print("Invalid choice")