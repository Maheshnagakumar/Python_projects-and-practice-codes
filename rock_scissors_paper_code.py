print("ROCK...")
print("SCISSORS")
print("PAPPER")
player1=input("please enter your input of player1 : ")
player2=input("please enter your input of player2 : ")

if player1==player2:
    print("huh !! It's tie")
elif player1=="paper":
    if player2=="scissors":
        print("player2 wins!!")
    elif player2=="rock":
        print("player1 wins")
elif player1=="scissors":
    if player2=="rock":
        print("player2 wins !!!")
    elif player2=="paper":
        print("player1 wins")
elif player1=="rock":
    if player2=="scissors":
        print("player1 wins")
    elif player2=="paper":
        print("player2 wins")
else:
    print("Please enter your input") 
	
	