This is a project to show how different sorting algorithms 
take different computational time with different sizes of keys.
The sorting algorithms are mergesort and insertionsort.

mergesort.py -

The script to run the mergesort algorithm.

insertionsort.py -

The script to run the insertionsort algorithm.

filehandler.py -

Handles the files relating to the keys and log.

randomkeygen.py - 

Generates random keys of length n in groups of 5.
Uses the filehandler to export to txt files.

tester.py - 

Takes the keys and runs the sorting algorithms. 
It records the time difference. 
On the windows platform the time library seems to not be 
accurate at smaller times. 
Giving the result of 0 nanoseconds computational time, 
which is unlikely.

plotter.py -

Uses matplotlib.pyplot to graph the log file values.
The x axis is on a log scale. the y axis is given in 
scientific notation. (10^9ns = 1 second)

NOTES -

Values for the insertionsort at key lengths of 1000000 
are not given because they took too long. I ran the script 
over night and still didn't get any results.

To run the program the scripts are run at seperate 
times although they could potentially be run with one script. 
I chose to run them seperately as I tinkered with things.