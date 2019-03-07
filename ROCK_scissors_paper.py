print("ROCK...")
print("SCISSORS")
print("PAPPER")
player1=input("please enter your input of player1 : ")
player2=input("please enter your input of player2 : ")

if player1=="ROCK" and player2=="scissors":
    print("player1 wins:)")
elif player1=="scissors" and player2=="paper": 
    print("Player1 wins!!")
elif player1=="paper" and player2=="scissors":
    print("yayy player2 wins")
elif player1=="ROCK" and player2=="paper":
    print("yay!! player1 wins again")
elif player1=="scissors" and player2=="ROCK":
    print("player2 wins:)")
elif   player1=="paper" and player2=="scissors":
    print("player2 wins :)")
elif   player1=="paper" and player2=="ROCK":
    print("yay!!! player2 wins again")
else:
    print("Both are same,play again!!")