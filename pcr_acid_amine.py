import numpy as np

bases_ARN = ['A','C','G','U']
bases_ADN = ['A','C','G','T']
bases = bases_ARN
names_ADN = {'A':'adénosine','C':'cytosine','G':'guanine','T':'thymine'}
names_ARN = {'A':'adénosine','C':'cytosine','G':'guanine','U':'uracile'}
bases_names = names_ARN
# a : adénine
# t : thymine
# c : cytosine
# g : guanine
# u : uracile (ARN)
# C-G (3 hydrogène) et A-T (2 hydrogène)

base = np.random.choice(bases)
print(base, bases_names[base])
# https://pynative.com/python-random-choice/
l = 67
seq = 'ATAUG'+''.join([(np.random.choice(bases)) for n in range(l)])
print('seq:',seq)

import traduction
traduction.main(seq)