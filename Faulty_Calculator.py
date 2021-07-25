print("This is a Calculation program in which you can perform\n 1.addition\n 2.subtraction\n 3.multiplication\n 4.division ")
x=input("Which operation you want to do?")
if x=="subtraction":
    y=int(input("Enter 1st number:"))
    z=int(input("Enter second number:"))
    print("Result=",y-z)    
elif x=="addition":
     y=int(input("Enter 1st number:"))
     z=int(input("Enter second number:"))
     if y==56 and z==9:
          print("Result=77")
     else:
             print("Result=",y+z)
elif x=="multiplication":
     y=int(input("Enter 1st number:"))
     z=int(input("Enter second number:"))
     if y==45 and z==3:
         print("Result=555")
     else:
       print("Result=",y*z)
elif x=="division":
     y=int(input("Enter 1st number:"))
     z=int(input("Enter second number:"))
     if y==56 and z==6:
       print("Result=4") 
     else:
        print("Result=",y/z)








