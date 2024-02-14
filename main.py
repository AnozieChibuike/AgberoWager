from unratedwriting import typewrite
from uuid import uuid4
from models.user import User
from create import create_user
from games.dice import Dice
from games.dice import roll


# user = create_user()
# user.balance += 2000
computer = User(username="Computer", age=0, country="Nigeria")
computer.balance += 2000
def main():
    pass
    # playGame(user,computer)

def playGame(user1,user2):
    while True:
        stake = int(input('Stake in Naira: '))
        if stake < 100:
            typewrite('Minimum of 100 Naira')
        else:
            if stake > user1.balance:
                raise InterruptedError(f"{user1.username}'s balance is lower than stake")
            if stake > user2.balance:
                raise InterruptedError(f"{user2.username}'s balance is lower than stake")
            user1.balance -= stake
            user2.balance -= stake
            break
                
    prompt = input("Roll: (yes/no)")
    if prompt.lower() == "yes":
        user_roll = roll()
    else:
        exit()
    typewrite(f"{user1.username} rolled {user_roll}")
    typewrite(f"Waiting for {user2.username} to roll")
    typewrite("...", 1)
    user2_roll = roll()
    typewrite(f"{user2.username} rolled {user2_roll}")
    game = Dice(user1, user2,stake)
    game.set_roll(user_roll, user2_roll)
    winner = game.get_winner()
    if winner:
        if winner == user1:
            user1.balance += (game.stake * 2) - (game.stake * 0.2)
            typewrite(f'{user1.username} win')
        else:
            user2.balance += (game.stake * 2) - (game.stake * 0.2)
            typewrite(f'{user2.username} win')
    else:
        user1.balance += stake
        user2.balance += stake
        typewrite('Draw')    
    return game

if __name__ == "__main__":
    main()
