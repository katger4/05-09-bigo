Searching
How fast is it?

Wall-Clock Time
    What is wrong with this approach?

    import time

    start = time.time() #start stopwatch

    # ... do algorithm

    end = time.time() #stop stopwatch
    print("time:",end-start) #time elapsed

    NOT consistent! computer doing other things
    Depends on the execution environment (e.g., the machine that youre working on)

Operation Count
    Instead: count "how many (significant) things we do"
    Correlated with clock time, but can be measured independently from processor speed.

Big Data
    How many operations do we need to do as the amount of data (the size of the list) increases?

    len(list)   # comp (avg)    # comp (worst)
    10          5               10
    20          10              20
    50          25              50
    100         50              100
    1000        500             1000
    n           n/2             n

Linear Search - has particular slope (linear relationship bt amt of data working with and at of time needed to process it - if data doubles in size, time doubles)
    def linear_search(list, target):
        for i, item in enumerate(list):
            if item == target:
                return i
        return -1

    If it takes 1 microsecond to search 1 item, how long will it take to search 100 billion items?
        28 hours!
    30 trillion items?
        347 days!

A faster search?
    How might we be faster about this?
    Consider: telephone, goldilocks

Binary Search
    Search a sorted list by comparing to the middle number, then either going to the top or bottom half, and repeating. When you know what target you want, list is in order, and look for a articular target in that list, return index.

    def binary_search(list, target):

        start_index = 0 #initial goalposts
        end_index = len(list)-1

        while start_index <= end_index: #at least one thing to look at

            middle_index = (start_index + end_index)//2 #integer division

            if(list[middle_index] == target):
                return middle_index #found the item!
            elif target > list[middle_index]:
                start_index = middle_index+1 #move goalpost
            else:
                end_index = middle_index-1 #move goalpost

        return -1 #did not find the item

Binary Search Speed
    http://www.cs.armstrong.edu/liang/animation/web/BinarySearch.html
    Each time through the while loop, the amount to search gets cut in half.
    Need to search N items:
        N*(1/2)*(1/2)*(1/2)
        N*(1/(2**k)) = 1
            k = number of loops <--solve for k
        N = 2**k
        1/N = 1/(2**k)
        k = math.log(N, 2) #log base 2 --> lg(N) = how many times we need to search for things in binary search
    If the data set doubles in size, iterations increases by 1

    If it takes 1 microsecond to search 1 item, how long will it take to search 100 billion items?
        36 microsecs!
    30 trillion items?
        44 microsecs!

    But binary search requires a list to be sorted!

Sorting
    One sorting algorithm:
        Find ("select") the smallest item
        Put it first
        Select the second smallest item
        Put it second
        Select the third smallest item
        Put it third
        ...

Selection Sort
def selection_sort(list):
    """Sorts the list (in place)"""

    for i in range(len(list)):
        selected = i #smallest
        for j in range(i,len(list)): #koth search rest
            if(list[j] < list[selected]):
                selected = j

        # swap smallest into place
        list[i],list[selected] = list[selected],list[i]

Selection Sort Speed
    To select the first (smallest) item, need to search n items.
    To select the second item, need to search n-1 items
    To select the third item, need to search n-2 items
    ...
    To select the second-to-last, need to search 2 items
    To select the last, need to search 1 item

    n + (n+1) + (n-2) +...+ 2 + 1 --> (n*(n+1))/2 --roughly--> n**2

    quadratic method/curve: If the data set doubles in size, the runtime quadruples in size

Faster Sorts
There are many faster sorting algorithms, most of which require n*lg(n) operations
Can we generalize this concept of "speed"?

Runtime Polynomials
    A polynomial f(n) representing the number of operations as a function of data size.
    def average(list):

       total = 0 # +1
       count = 0 # +1
       for num in list: #n*(
          total = total + num # +2
          count += 1        # +2)

       average = total/count #+2
       return average       #+2

    T(n) = 1+1+n*(2+2)+2+1
    T(n) = 4n+5

Big-O Notation
    We classify different algorithms based on a function f(n) > T(n)/c  that acts as an "upper bound" for the polynomial

    We say these algorithms have order f(n), written as O(f(n))
        T(n) = 4n+5 --> O(n)
        T(n) = (n(n+1))/2 --> O(n**2)

    In practice, an algorithm''s order is simply the "biggest" (fastest-growing) term of the polynomial, ignoring the coefficient.
        T(n) = n/1000000 + 9999999999   --> O(n)
        T(n)= (n**3+1)/n+1              --> O(n**2)
        T(n) = (n**2+1)(n*lg(n)+3)      --> O(n**3*lg(n))
        T(n) = (n+3)/(n+1)              --> O(1) <-- holy grail of algorithm speed (does not increase with more stuff, amt of work is always the same even as you go to infinity)
        T(n) = 999***999                --> O(1)

Common Complexities (in order of increasing slowness/work required)
    #Big-O                       type                example
    O(1)                        constant            determine if even or odd
    O(lg(n))                    logarithmic         Binary Search
                 
    O(n)                        linear              Linear Search
                 
    O(n*lg(n))                  log-linear          Fast sorts
                                "linearithmic"      
    O(n**2)                     quadratic           Slow sorts
                 
    O(n**c, c>1) eg. O(n**3)    polynomial          All-pairs shortest paths (FW)
    O(c**n, c>1) eg. O(2**n)    exponential         Some cryptography algorithms
    O(n!)                       factorial           Traveling Salesperson Problem

    #Big-O                      n=10                n=100               n=1000
    O(1)                        1us                 1us                 1us
    O(lg(n))                    3us                 6us                 10us
                 
    O(n)                        1us                 100us               1ms
                 
    O(n*lg(n))                  33us                664us               9.9s
                                      
    O(n**2)                     100us               10ms                1s
    ______________________below this line, unreasonable speeds___________________________
    O(2**n)                     1s                  4*10**16yrs         n/a
                                                      ^2million times the age of the universe
    O(n!)                       3s                  2*10**134universes  good god

