# program that computes the sum of all integers from 0 to n
# illustrates while loops and nested loops

# this is an infinite loop as the loop condition is always true:
while True:
    n = int(input("Enter n: "))     # the upper bound
    # exit the loop and terminate the application by typing CTRL-C or
    #    entering the empty string "". The latter will cause an error.
    
    s = 0               # the sum 
    i = 0               # loop "index" variable
    
    while i <= n:
        s = s + i   # same as s += i
        i = i + 1   # same as i += 1
    
    print("sum = ", s)
    # after this print we go back and read n again

    
