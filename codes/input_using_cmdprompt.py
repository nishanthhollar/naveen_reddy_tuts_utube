"""Write the code to find out the cube  of a number and pass the values directly from command prompt
WHat this code does is that it directly takes input while we are calling the python file itself

example
python input_using_cmdprompt.py 12 

we run this on the command prompt we get the answer 
the cube root of a number is 1728"""


import sys
x = int(sys.argv[1])
result = x*x*x
print("The cube root of a number is ", result)