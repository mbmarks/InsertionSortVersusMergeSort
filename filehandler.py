from time import time, gmtime
from randomkeygen import genlist

def createlistfile(n,t):
    with open('keys/' + str(t) + '.' + str(n) + 'keys.txt', 'w+') as f:
        for _ in range(5):
            a = genlist(n,t)
            for items in a:
                f.write('%s,' %items)
            f.write('\n')
    f.close()
    return

def extractlistfile(n,t):
    keys = list()
    with open('keys/' + str(t) + '.' + str(n) + 'keys.txt', 'r') as f:
        for l in f.readlines():
            a = l.split(',')
            a.pop()
            a = list(map(int,a))
            #this pop removes the \n
            keys.append(a)         
    f.close()
    return keys

def filenametime(t):
    a = gmtime(t)
    return str(a.tm_mon) + str(a.tm_mday) + str(a.tm_hour) + str(a.tm_min) + str(a.tm_sec)

### Create output file function
def outputfile(n,t,sort,time_taken):
    with open('log/output.log', 'a+') as f:
        f.write('{} {} {} {} nanosec\n'.format(n,sort,t,time_taken))
    f.close()

def extractoutputfile():
    tests = list()
    with open('log/output.log', 'r') as f:
        for l in f.readlines():
            a = l.split(' ')
            a.pop()
            a[0] = int(a[0])
            a[3] = int(a[3])
            tests.append(a)
    f.close()
    return tests