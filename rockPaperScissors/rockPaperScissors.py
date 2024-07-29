
import random 
def rockPaperScissors():
    plays = ['rock', 'paper', 'scissors']
    wins = 0
    losses = 0
    while True:
        opponent = random.choice(plays)
        ethan = input("Rock, paper or scissors? ('sissy' to forfeit)").lower()
        if ethan =='sissy':
            print('Run along baby!')
            break
        elif ethan not in plays:
            print("None of that cheating crap! Choose a real play!")
            continue
        elif ethan == opponent:
            print("TIE!\n")
            print(f'Player: {ethan}')
            print(f'Opponent: {opponent}\n')
            print(f"Total wins:{wins}")
            print(f"Total losses:{losses}")
        elif ethan == 'rock' and opponent == 'scissors':
            print("VICTORY!\n")
            wins +=1
            print(f'Player: {ethan}')
            print(f'Opponent: {opponent}\n')
            print(f"Total wins:{wins}")
            print(f"Total losses:{losses}")
        elif ethan == 'paper' and opponent == 'rock':
            print("VICTORY!\n")
            wins +=1
            print(f'Player: {ethan}')
            print(f'Opponent: {opponent}\n')
            print(f"Total wins:{wins}")
            print(f"Total losses:{losses}")
        elif ethan == 'scissors' and opponent == 'paper':
            print("VICTORY!\n")
            wins +=1
            print(f'Player: {ethan}')
            print(f'Opponent: {opponent}\n')
            print(f"Total wins:{wins}")
            print(f"Total losses:{losses}")
        else:
            print("LOSER!")
            losses +=1
            print(f'Player: {ethan}')
            print(f'Opponent: {opponent}\n')
            print(f"Total wins:{wins}")
            print(f"Total losses:{losses}")
rockPaperScissors()
