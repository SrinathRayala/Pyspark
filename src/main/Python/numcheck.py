#This is the number game.
import random
import pprint
print("Hello what is your name")
name =input()
print('Well, '+name + ' i am thinking of number')
secreatNumber=random.randint(1,20)
print('screatnumber ' + str(secreatNumber))
for guessasTaken in range(1,7):
    print('take a gues')
    guess = int(input())
    if guess < secreatNumber:
        print('low')
    elif guess > secreatNumber:
        print('high')
    else:
        break
if guess == secreatNumber:
    print('good job' + str(secreatNumber) + 'and guessTaken' + str(guessasTaken))
print('you took' + str(guessasTaken) + ' gussess')


message='kkwer;hqw;r"eh;wjqreh;qehrwerk;hjqlkrehqkejrhqjrh"'
count={}
for character in message.upper():
    count.setdefault(character,0)
    count[character]=count[character]+1
text=pprint.pformat(count)
print(text)