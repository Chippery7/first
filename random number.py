import random
last = []
vowels = ['a','e','i','o','u']
regular_two = ['p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
regular_one = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l,' 'm','n']
v_choose = random.randint(0,4)
rone_choose = random.randint(0,10)
rtwo_choose = random.randint(0,9)
letters = ['vowels','regular_one','regular_two']
random_letters = random.shuffle(letters)
random_letters = letters
if v_choose == 0:
    print(vowels[0])
    vowels = 'a'
    last.append(vowels)
elif v_choose == 1:
    print(vowels[1])
    vowels = 'e'
    last.append(vowels)
elif v_choose == 2:
    print(vowels[2])
    vowels = 'i'
    last.append(vowels)
elif v_choose == 3:
    print(vowels[3])
    vowels = 'o'
    last.append(vowels)
elif v_choose == 4:
    print(vowels[4])
    vowels = 'u'
    last.append(vowels)
if rtwo_choose == 0:
    print(regular_two[0])
    rtwo_choose = 'p'
    last.append(rtwo_choose)
elif rtwo_choose == 1:
    print(regular_two[1])
    rtwo_choose = 'q'
    last.append(rtwo_choose)
elif rtwo_choose == 2:
    print(regular_two[2])
    rtwo_choose = 'r'
    last.append(rtwo_choose)
elif rtwo_choose == 3:
    print(regular_two[3])
    rtwo_choose = 's'
    last.append(rtwo_choose)
elif rtwo_choose == 4:
    print(regular_two[4])
    rtwo_choose = 't'
    last.append(rtwo_choose)
elif rtwo_choose == 5:
    print(regular_two[5])
    rtwo_choose = 'v'
    last.append(rtwo_choose)
elif rtwo_choose == 6:
    print(regular_two[6])
    rtwo_choose = 'w'
    last.append(rtwo_choose)
elif rtwo_choose == 7:
    print(regular_two[7])
    rtwo_choose = 'x'
    last.append(rtwo_choose)
elif rtwo_choose == 8:
    print(regular_two[8])
    rtwo_choose = 'y'
    last.append(rtwo_choose)
elif rtwo_choose == 9:
    print(regular_two[9])
    rtwo_choose = 'z'
    last.append(rtwo_choose)
if rone_choose == 0:
    print(regular_one[0])
    regular_one = 'b'
    last.append(regular_one)
elif rone_choose == 1:
    print(regular_one[1])
    regular_one = 'c'
    last.append(regular_one)
elif rone_choose == 2:
    print(regular_one[2])
    regular_one = 'd'
    last.append(regular_one)
elif rone_choose == 3:
    print(regular_one[3])
    regular_one = 'f'
    last.append(regular_one)
elif rone_choose == 4:
    print(regular_one[4])
    regular_one = 'g'
    last.append(regular_one)
elif rone_choose == 5:
    print(regular_one[5])
    regular_one = 'h'
    last.append(regular_one)
elif rone_choose == 6:
    print(regular_one[6])
    regular_one = 'j'
    last.append(regular_one)
elif rone_choose == 7:
    print(regular_one[7])
    regular_one = 'k'
    last.append(regular_one)
elif rone_choose == 8:
    print(regular_one[8])
    regular_one = 'l'
    last.append(regular_one)
elif rone_choose == 9:
    print(regular_one[9])
    regular_one = 'm'
    last.append(regular_one)
random.shuffle(last)
print(last)