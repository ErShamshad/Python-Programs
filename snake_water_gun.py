
import random
i=0
j=0
while (True):
    if i<4:
        list=["snake","water","gun"]
        choice=random.choice(list)
        a=input("Enter the choice\n1.snake, 2.water or 3.gun\nEnter:")
        if choice =="snake" and a=="snake":
            print("Match tied.")
            print("The system choice was also 'snake'.")
            i=i+1 
        elif choice=="snake"and a=="water":
            print("You lost.")
            print("The system choice was 'snake'.")
            i=i+1 
        elif choice=="snake"and a=="gun":
            print("Congratulations!! You won!")
            print("The system choice was 'snake'.")
            i=i+1
            j=j+1
        elif choice=="water"and a=="water":
            print("Match Tied! ") 
            print("The system choice was also 'water'.")
            i=i+1 
        elif choice=="water"and a=="snake":
            print("Congratulations!! You Won!")
            print("The system choice was 'water'")
            i=i+1
            j=j+1
        elif choice=="Water"and a=="gun":
            print("You lost.")
            print("The system choice was'water'. ")
            i=i+1
        elif choice=="gun"and a=="gun":
            print("Match Tied.")
            print("The system choice was'gun'. ")
            i=i+1
        elif choice=="gun"and a=="snake":
            print("You lost.")
            print("The system choice was'gun'. ")
            i=i+1
        elif choice=="gun"and a=="water":
            print("Congratulations!! You Won!")
            print("The system choice was'gun'. ")
            i=i+1
            j=j+1
        else:
            print("Invalid respose.") 
            i=i+1      
    else:
        print("Your total winning out of 4 is :",j)  
        break
                        

