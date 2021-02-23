from time import sleep, time_ns

from mergesort import mergesort
from insertionsort import insertionsort
from filehandler import createlistfile, extractlistfile, outputfile

times = [10,100,1000,10000,100000,1000000]
kind = ['a','random', 'd']

for t in times:
    for k in kind:
        createlistfile(t,k)

def testinsertion(a,i,k):
    started = time_ns()
    insertionsort(a)
    ended = (time_ns() - started)
    outputfile(i,k,'insertion',ended)

def testmerge(a,i,k):
    started = time_ns()
    mergesort(a,0,len(a)-1)
    ended = (time_ns() - started)
    outputfile(i,k,'merge',ended)


for k in kind:
    for i in times:
        a = extractlistfile(i,k)
        for j in a:
            testmerge(j,i,k)

for k in kind:
    for i in times:
        a = extractlistfile(i,k)
        for j in a:
            testinsertion(j,i,k)

