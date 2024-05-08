import random

print("           welcome to strongca's game jajaja! \n\n")
party_size = input("Set the party size\n")
users = []

for ip in range(int(party_size)):
    name = input("what's your name jajaja! \n")
    print("hello ", name, " welcome to strongca's game jajaja\n\n") 
    users.append(name)

digit = input ("please select game mode 4-10\n")
digit = int(digit)
print("guess a numer with ", digit, " digit\n\n") 


random.seed()
generted = random.randint(10**(digit-1),10**(digit)-1)
generted = str(generted)
print("generated num: ", generted)

def guess_num():
    guess = input ("take a guess\n\n")
    count = 0
    while (len(guess) != len(generted)) or (not guess.isnumeric()):
        count+=1
        if count >= 6:
            print(".........")
        elif count >= 3:
            print("please input", digit, "digit number, okay????????????")
        else:
            print("please input", digit, "digit number, okay???")
        guess = input("\n")
    return guess


trycount = 4
while trycount > 0:
    for user in range (len(users)):
        print("Greeting!", users[user])
        guess = guess_num()
        correctnumber = 0
        for i in range(digit):
            if guess[i] in generted:
                correctnumber = correctnumber + 1
        correctlocation = 0
        for i in range(digit):
            if guess[i] == generted[i]:
                    correctlocation+=1
        if guess == generted:
            print("what!!!!!!you are Jessica!!!!!")
            break
        print("you have", correctnumber, "correct number", "and you have", correctlocation, "correct location")
        print("you have",trycount,"attempts only")
    trycount -=1
if trycount == 0:
    print ("try better next time babe~")