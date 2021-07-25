print("Health Management System")
a=int(input("Enter 1 for Harry, 2 for Hammad,3 for Rohan\nEnter:"))
if a==1:
   b=int(input("What you wanna do?\nEnter 1 to log and 2 to retieve\nEnter:"))
   if b==1:
       c=int(input("Enter 1 for Diet and 2 for Exercise\nEnter: "))
       if c==1:
           value=input("Type here:\n")
           with open("HarryDiet.txt","a") as f:
               f.write(value)
               print("Successfully written")
       else:
           value=input("Type here\n:")
           with open("HarryExercise.txt","a") as f:
               f.write(value)
               print("Successfully written")
   else:
        c=int(input("Enter 1 for Diet and 2 for Exercise\nEnter: "))
        if c==1:
         with open("HarryDiet.txt") as f:
             for item in f:
                 print(item)

             
        else:
             with open("HarryExercise.txt","r") as f:
                for item in f:
                    print(item)
elif a==2:
   b=int(input("What you wanna do?\nEnter 1 to log and 2 to retieve\nEnter:"))
   if b==1:
       c=int(input("Enter 1 for Diet and 2 for Exercise\nEnter: "))
       if c==1:
           value=input("Type here:\n")
           with open("HammadDiet.txt","a") as f:
               f.write(value)
               print("Successfully written")
       else:
           value=input("Type here\n:")
           with open("HammadExercise.txt","a") as f:
               f.write(value)
               print("Successfully written")
   else:
        c=int(input("Enter 1 for Diet and 2 for Exercise\nEnter: "))
        if c==1:
         with open("HammadDiet.txt","r") as f:
             for item in f:
                 print(item)
        else:
            with open("HammadExercise.txt","r") as f:
                for item in f:
                    print(item)
elif a==3:
    b=int(input("What you wanna do?\nEnter 1 to log and 2 to retieve\nEnter:"))
    if b==1:
       c=int(input("Enter 1 for Diet and 2 for Exercise\nEnter: "))
       if c==1:
           value=input("Type here\n")
           with open("RohanDiet.txt","a") as f:
               f.write(value)
               print("Successfully written")
       else:
           value=input("Type here\n")
           with open("RohanExercise.txt","a") as f:
               f.write(value)
               print("Successfully written")
    else:  
         c=int(input("Enter 1 for Diet and 2 for Exercise\nEnter: "))
         if c==1:
          with open("RohanDiet.txt","r") as f:
             for item in f:
                 print(item) 
         else:
            with open("RohanExercise.txt","r") as f:
                for item in f:
                    print(item) 
else:
    print("Invalid Resonse")

  