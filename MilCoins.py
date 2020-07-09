import random
Heads = 0
Tails = 1
H_count = Heads
T_count = Tails
H_count = 0
T_count = 0
Coin = [Heads,Tails]
count = +1
random.shuffle(Coin)

for x in range(0,1000000):
    random.shuffle(Coin)
    if Coin[0] == False:
        H_count + count
        H_count = H_count + count
    elif Coin[0] == True:
        T_count + count
        T_count = T_count + count

print(H_count, 'Is how much heads has been flipped', T_count, 'Is how much tails has been flipped')