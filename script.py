def search_bb(list, target):
    """Returns the index (a number) of the target 
       in the given list, or -1 if absent
    Params:
        list - a list of items
        target - a target to search for
    """
    # tup = enumerate(list)
    # for i, j in enumerate(list):
    #     if j == target:
    #         return i
    # return -1

    for index in range(len(list)):
        if list[index] == target:
            return index
    return -1

    # for i in list:
    #     if i == target:
    #         return index
    #     index += 1
    #     else:
    #         return -1

# print(search(['John','Paul','George','Ringo'], 'George'))
# #=> 2

# print(search(['John','Paul','George','Ringo'], 'Yoko'))
# #=> -1


########alt method
def alt_search(list, target):
    """Returns the index (a number) of the target 
       in the given list, or -1 if absent"""
    for i, item in enumerate(list): #each item & index
        if item == target: #compare
            return i #if found
    return -1 #if not in list


#########time it
import time

def wall_search(list, target):
    """Returns the index (a number) of the target 
       in the given list, or -1 if absent"""
    start = time.time() #start stopwatch
    for i, item in enumerate(list):
        if item == target:
            end = time.time() #stop stopwatch (need to end and return twice in case dont get here)
            print("time:",end-start) #time elapsed <--wall-clock time
            return i
    end = time.time() #stop stopwatch
    print("time:",end-start) #time elapsed
    return -1

##############operation count
def search(list, target):

    comparisons = 0 #count comparisons
    for i, item in enumerate(list):
        comparisons += 1 #count comparison about to do
        if item == target:
            print("comps:",comparisons) #num operations
            return i
    print("comps:",comparisons) #num operations
    return -1

print(search(['John','Paul','George','Ringo'], 'George'))
#=> 2 comps: 3

print(search(['John','Paul','George','Ringo'], 'Yoko'))
#=> -1 comps: 4

print (search(list(range(10**6)), -1))
#=> comps: 1000000, -1

print (search(list(range(10**6)), 50))
#=> comps: 51, 50