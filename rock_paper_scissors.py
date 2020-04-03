import random,sys

print('ROCK, PAPER, SCISSORS! Best of 3')
win = 0
loss = 0
tie = 0
i = 0

while win < 3 and loss < 3:
    i += 1
    print('so far the record is '+ str(win) + ' WINS, '+ str(loss) + ' LOSSES, '+ str(tie) + ' TIES' + '\n')
    player = ''
    while player.lower() != 'r' and player.lower() != 'p' and player.lower() != 's' and player.lower() != 'q':
        player = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ')
        if player.lower() == 'r':
            print('Player deals ROCK!')
        elif player.lower() == 'p':
            print('Player deals PAPER!')
        elif player.lower() == 's':
            print('Player deals SCISSORS!')
        elif player.lower() == 'q':
            print('---')
            print('FINAL RECORD: '+ str(win) + ' WINS, '+ str(loss) + ' LOSSES, '+ str(tie) + ' TIES')
            sys.exit()
        else:
            continue

    cpu = random.randint(0,2)
    if cpu == 0:
        print('CPU deals ROCK!')
    elif cpu == 1:
        print('CPU deals PAPER!')
    else:
        print('CPU deals SCISSORS!')

    if cpu == 0 and player.lower() == 'p':
        win += 1
        print('Round ' + str(i) + ' goes to you')
    elif cpu == 0 and player.lower() == 's':
        loss += 1
        print('Round ' + str(i) + ' goes to CPU')
    elif cpu == 1 and player.lower() == 'r':
        loss += 1
        print('Round ' + str(i) + ' goes to CPU')
    elif cpu == 1 and player.lower() == 's':
        win += 1
        print('Round ' + str(i) + ' goes to you')
    elif cpu == 2 and player.lower() == 'r':
        win += 1
        print('Round ' + str(i) + ' goes to you')
    elif cpu == 2 and player.lower() == 'p':
        loss += 1
        print('Round ' + str(i) + ' goes to CPU')
    else:
        tie += 1
        print('Round ' + str(i) + ' is tied')

print('---')
print('FINAL RECORD: '+ str(win) + ' WINS, '+ str(loss) + ' LOSSES, '+ str(tie) + ' TIES')
