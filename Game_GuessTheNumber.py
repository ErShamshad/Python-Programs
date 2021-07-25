n=21
s=3

while(True):
   
    print("Guess the number\n""You attemt left is", s)
    if s==0:
        print("Game over!!")
        break
    k=int(input("\nEnter your numer:"))
    if k<n:
        print("Try again!\n Your number is lesser than the exact number!")
        s=s-1
        continue
    
    if k>n:
     print("Try again!\n Your number is greater than the exact number!")
     s=s-1
     continue
    if k==n:
        print("Congratulations!! You won the game!!!")
        break
