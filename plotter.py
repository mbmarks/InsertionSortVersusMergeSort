import matplotlib.pyplot as plt
import numpy as np
from statistics import mean

from filehandler import extractoutputfile

tests = extractoutputfile()

m_random_x = [10,100,1000,10000,100000,1000000]
m_random_y = [None]*6
i_random_x = [10,100,1000,10000,100000,1000000]
i_random_y = [None]*6

m_a_x = [10,100,1000,10000,100000,1000000]
m_a_y = [None]*6
i_a_x = [10,100,1000,10000,100000,1000000]
i_a_y = [None]*6

m_d_x = [10,100,1000,10000,100000,1000000]
m_d_y = [None]*6
i_d_x = [10,100,1000,10000,100000,1000000]
i_d_y = [None]*6

for i in tests:
    if i[1] == 'merge':
        if i[2] == 'random':
            if i[0] == 10:
                if type(m_random_y[0]) == type(None):
                    m_random_y[0] = i[3]
                else:
                    m_random_y[0] = mean([m_random_y[0],i[3]])
            elif i[0] == 100:
                if type(m_random_y[1]) == type(None):
                    m_random_y[1] = i[3]
                else:
                    m_random_y[1] = mean([m_random_y[1],i[3]])
            elif i[0] == 1000:
                if type(m_random_y[2]) == type(None):
                    m_random_y[2] = i[3]
                else:
                    m_random_y[2] = mean([m_random_y[2],i[3]])
            elif i[0] == 10000:
                if type(m_random_y[3]) == type(None):
                    m_random_y[3] = i[3]
                else:
                    m_random_y[3] = mean([m_random_y[3],i[3]])
            elif i[0] == 100000:
                if type(m_random_y[4]) == type(None):
                    m_random_y[4] = i[3]
                else:
                    m_random_y[4] = mean([m_random_y[4],i[3]])
            else: 
                if type(m_random_y[5]) == type(None):
                    m_random_y[5] = i[3]
                else:
                    m_random_y[5] = mean([m_random_y[5],i[3]])
        elif i[2] == 'a':
            if i[0] == 10:
                if type(m_a_y[0]) == type(None):
                    m_a_y[0] = i[3]
                else:
                    m_a_y[0] = mean([m_a_y[0],i[3]])
            elif i[0] == 100:
                if type(m_a_y[1]) == type(None):
                    m_a_y[1] = i[3]
                else:
                    m_a_y[1] = mean([m_a_y[1],i[3]])
            elif i[0] == 1000:
                if type(m_a_y[2]) == type(None):
                    m_a_y[2] = i[3]
                else:
                    m_a_y[2] = mean([m_a_y[2],i[3]])
            elif i[0] == 10000:
                if type(m_a_y[3]) == type(None):
                    m_a_y[3] = i[3]
                else:
                    m_a_y[3] = mean([m_a_y[3],i[3]])
            elif i[0] == 100000:
                if type(m_a_y[4]) == type(None):
                    m_a_y[4] = i[3]
                else:
                    m_a_y[4] = mean([m_a_y[4],i[3]])
            else: 
                if type(m_a_y[5]) == type(None):
                    m_a_y[5] = i[3]
                else:
                    m_a_y[5] = mean([m_a_y[5],i[3]])
        else:
            if i[0] == 10:
                if type(m_d_y[0]) == type(None):
                    m_d_y[0] = i[3]
                else:
                    m_d_y[0] = mean([m_d_y[0],i[3]])
            elif i[0] == 100:
                if type(m_d_y[1]) == type(None):
                    m_d_y[1] = i[3]
                else:
                    m_d_y[1] = mean([m_d_y[1],i[3]])
            elif i[0] == 1000:
                if type(m_d_y[2]) == type(None):
                    m_d_y[2] = i[3]
                else:
                    m_d_y[2] = mean([m_d_y[2],i[3]])
            elif i[0] == 10000:
                if type(m_d_y[3]) == type(None):
                    m_d_y[3] = i[3]
                else:
                    m_d_y[3] = mean([m_d_y[3],i[3]])
            elif i[0] == 100000:
                if type(m_d_y[4]) == type(None):
                    m_d_y[4] = i[3]
                else:
                    m_d_y[4] = mean([m_d_y[4],i[3]])
            else: 
                if type(m_d_y[5]) == type(None):
                    m_d_y[5] = i[3]
                else:
                    m_d_y[5] = mean([m_d_y[5],i[3]])

    if i[1] == 'insertion':
        if i[2] == 'random':
            if i[0] == 10:
                if type(i_random_y[0]) == type(None):
                    i_random_y[0] = i[3]
                else:
                    i_random_y[0] = mean([i_random_y[0],i[3]])
            elif i[0] == 100:
                if type(i_random_y[1]) == type(None):
                    i_random_y[1] = i[3]
                else:
                    i_random_y[1] = mean([i_random_y[1],i[3]])
            elif i[0] == 1000:
                if type(i_random_y[2]) == type(None):
                    i_random_y[2] = i[3]
                else:
                    i_random_y[2] = mean([i_random_y[2],i[3]])
            elif i[0] == 10000:
                if type(i_random_y[3]) == type(None):
                    i_random_y[3] = i[3]
                else:
                    i_random_y[3] = mean([i_random_y[3],i[3]])
            elif i[0] == 100000:
                if type(i_random_y[4]) == type(None):
                    i_random_y[4] = i[3]
                else:
                    i_random_y[4] = mean([i_random_y[4],i[3]])
            else: 
                if type(i_random_y[5]) == type(None):
                    i_random_y[5] = i[3]
                else:
                    i_random_y[5] = mean([i_random_y[5],i[3]])
        elif i[2] == 'a':
            if i[0] == 10:
                if type(i_a_y[0]) == type(None):
                    i_a_y[0] = i[3]
                else:
                    i_a_y[0] = mean([i_a_y[0],i[3]])
            elif i[0] == 100:
                if type(i_a_y[1]) == type(None):
                    i_a_y[1] = i[3]
                else:
                    i_a_y[1] = mean([i_a_y[1],i[3]])
            elif i[0] == 1000:
                if type(i_a_y[2]) == type(None):
                    i_a_y[2] = i[3]
                else:
                    i_a_y[2] = mean([i_a_y[2],i[3]])
            elif i[0] == 10000:
                if type(i_a_y[3]) == type(None):
                    i_a_y[3] = i[3]
                else:
                    i_a_y[3] = mean([i_a_y[3],i[3]])
            elif i[0] == 100000:
                if type(i_a_y[4]) == type(None):
                    i_a_y[4] = i[3]
                else:
                    i_a_y[4] = mean([i_a_y[4],i[3]])
            else: 
                if type(i_a_y[5]) == type(None):
                    i_a_y[5] = i[3]
                else:
                    i_a_y[5] = mean([i_a_y[5],i[3]])
        else:
            if i[0] == 10:
                if type(i_d_y[0]) == type(None):
                    i_d_y[0] = i[3]
                else:
                    i_d_y[0] = mean([i_d_y[0],i[3]])
            elif i[0] == 100:
                if type(i_d_y[1]) == type(None):
                    i_d_y[1] = i[3]
                else:
                    i_d_y[1] = mean([i_d_y[1],i[3]])
            elif i[0] == 1000:
                if type(i_d_y[2]) == type(None):
                    i_d_y[2] = i[3]
                else:
                    i_d_y[2] = mean([i_d_y[2],i[3]])
            elif i[0] == 10000:
                if type(i_d_y[3]) == type(None):
                    i_d_y[3] = i[3]
                else:
                    i_d_y[3] = mean([i_d_y[3],i[3]])
            elif i[0] == 100000:
                if type(i_d_y[4]) == type(None):
                    i_d_y[4] = i[3]
                else:
                    i_d_y[4] = mean([i_d_y[4],i[3]])
            else: 
                if type(i_d_y[5]) == type(None):
                    i_d_y[5] = i[3]
                else:
                    i_d_y[5] = mean([i_d_y[5],i[3]])


m_random_x = np.array(m_random_x)
m_random_y = np.array(m_random_y)
i_random_x = np.array(i_random_x)
i_random_y = np.array(i_random_y)

m_a_x = np.array(m_a_x)
m_a_y = np.array(m_a_y)
i_a_x = np.array(i_a_x)
i_a_y = np.array(i_a_y)

m_d_x = np.array(m_d_x)
m_d_y = np.array(m_d_y)
i_d_x = np.array(i_d_x)
i_d_y = np.array(i_d_y)

plt.plot(m_random_x,m_random_y, marker='o',label='Merge Sort')
plt.plot(i_random_x,i_random_y, marker='.',label='Insertion Sort')
plt.xscale('log')

plt.ylabel('Time (ns)')
plt.xlabel('# of Keys')

plt.title('Sort times for Random Keys')

plt.legend()

plt.savefig('img/randomsort.png')

plt.show()
plt.clf()

plt.plot(m_a_x,m_a_y,marker='o',label='Merge Sort')
plt.plot(i_a_x,i_a_y,marker='.',label='Insertion Sort')
plt.xscale('log')

plt.ylabel('Time (ns)')
plt.xlabel('# of Keys')

plt.title('Sort times for Ascending Sorted Keys')

plt.legend()

plt.savefig('img/ascendingsort.png')

plt.show()
plt.clf()

plt.plot(m_d_x,m_d_y,marker='o',label='Merge Sort')
plt.plot(i_d_x,i_d_y,marker='.',label='Insertion Sort')
plt.xscale('log')

plt.ylabel('Time (ns)')
plt.xlabel('# of Keys')

plt.title('Sort times for Descending Sorted Keys')

plt.legend()

plt.savefig('img/descendingsort.png')

plt.show()
plt.clf()