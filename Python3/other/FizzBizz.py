"""
20.04.2019
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the
number and for the multiples of five print "Buzz". 
For numbers which are multiples of both three 
and five print "FizzBuzz".
"""
# this excersise is timed

for i in range(1,101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(f"{i}")

#timed excercise
#4min 19s

"""
This code sucks! There has to be a way to do this in under 3 lines even using 
f-strings. And definately I can do it so the first function does not have to 
exist. But under time pressure I had to resort to basics. 
"""
# 2-line solution, still separates division by 15, hmm
# for i in range(1,101):
#     print(
#         "FizzBizz" if i % 15 == 0
#         else "Fizz" if i % 3 == 0 
#         else "Buzz" if i % 5 == 0 
#         else i
#         )