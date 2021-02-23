from random import randint
from sys import maxsize

def gennumber():
    return randint(-maxsize,maxsize)

# n number of digits, t [(default) random, 
# a ascending order, d decending order]
def genlist(n,t='random'):
    a = list()
    for _ in range(n):
        a.append(gennumber())
    if t == 'a':
        a.sort()
    elif t == 'd':
        a.sort(reverse=True)
    return a