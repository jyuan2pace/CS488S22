#I will create chaos
import sys
import random

n_of_chunks = int(sys.argv[1])
loss_ratio = float(sys.argv[2])
loseThem = random.sample(range(0, n_of_chunks-1), int(n_of_chunks*loss_ratio))

with open('LOSEUS.txt', 'w') as f:
    f.writelines("%s\n" % loseit for loseit in loseThem)
