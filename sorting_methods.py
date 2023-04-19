'''
 Author: Dane Selch
 source: school

 direction: sort reference file, here I will reference different types of 
 sorting algorithms.
'''
    
'''
    insertion sort : 0(n^2)
    take a value comepare it to all previous values till you find one larger
    than it. place the value there and shift everything over.
    EX:
        3,5,1,4,2   sorted | unsorted
        v,[3],5,1,4,2   v = where it will go
        3,v|[5],1,4,2
        v,3,5,|[1],4,2
        1,3,v,5,|[4],2
        1,v,3,4,5,|[2]
'''
def insert_sort(li):
    print(f'insertions sort as follows')
    print(f'starting with {li}')
    for i in range(1,len(li)):
        # start at 2nd value as the first will always
        # be sorted
        holder = li[i]
        for j in range(i): # don't go past i 
            if holder < li[j]:
                holder = li[j]
                li[j] = li[i]
                li[i] = holder
        print(li)


'''
    bubble sort : O(n)^2
    bubble sort (from least to greatest) will contilually
    swap large values on the left with the value on the right 
    should it be smaller. this continues till no swaps are made
    EX
        [4,2],1,5,3 -> [2,4],1,5,3 -> 2 and 5 swap
        2,[4,1],5,3 -> 2,[1,4],5,3 
        2,1,[4,5],3 -> 2,1,[4,5],3 -> no swap
        2,1,4,[5,3] -> 2,1,4,[3,5] -> 5 and 3 swap
        .... -> repeat 
        1,2,3,4,5
'''


def bub_sort(li):
    print(f'\n\nBubble sort as follows:')
    print(f'starting with {li}')
    for j in range(len(li)):
        for i in range(len(li)-1):
            if li[i] > li[i+1]:
                holder = li[i]
                li[i] = li[i+1]
                li[i+1] = holder
            print(li)



'''
selection sort
    it will find the minimum element of an array and place it at the 
    head of a list. it then divides the list into 2 sections. sorted and not sorted
    EX             sorted|not sorted
        4,2,[1],5,3 -> 1,|2,4,5,3
        1,|[2],4,5,3 -> 1,2,|4,5,3
        1,2|,4,5,[3] -> 1,2,3,|5,4
        1,2,3,|5,[4] -> 1,2,3,4|5
        done
'''

def sel_sort(li):
    print(f'\n \nSelected sort as follows:')
    print(f'starting with {li}')
    for i in range(len(li)):
        lowest = i
        for j in range(i+1,len(li)):
            if li[j] < li[lowest]:
                lowest = j
                

        
        if lowest > i:
            temp = li[i]
            li[i] = li[lowest]
            li[lowest] = temp 
        print(li)

'''
Quick sort: partitions a list (breaks it apart) into 
    3 groups; lower, same, and greater values. it then reconstructs
    them into the correct order

    EX:
        4, 5, 9, [6], 6, 14, 10
        low/=      S 6        high
        4,5,6,     |        9,14,10  
     L4,5  S6             L9, S10 H14
     L4 H5  |               S9 |   S14      
      L4 S5 |               |  |    |
      S4  | |               |  |    |
      4   5 6      6        9 10    14
      
     '''
def Quick_sort(li):
    # if there is only one value then return it. 
    print(f'li = {li}')
    if len(li) < 2:
        return li
    low, high = [], []
    #get a random value to use as deciding factor
    mid = round(len(li)-1)
    print(f' mid value = {li[mid]}')
    axis = li[round(mid)]
    for i in range(len(li)-1):
        if i != mid:
            if li[i] <= axis: #if value is <= goes to low side
                low.append(li[i])
            if li[i] > axis: #if value is > then gose to hish side
                high.append(li[i])
    
    return Quick_sort(low) + [axis] + Quick_sort(high)

'''
merge:
    will take values from 2 lists and combine them into 1 list 
    in order least to greatest
    -- helper function for merge sort
    **usually uses randint to find a random value to use as axis
    point.
    EX:
        4, 5, 9, [6], 6, 14, 10
        low/=              high
        4,5,9,6            9,14,10  
     4,5  9,6             6, 10, 14
     4 5  9 , 6          6, 10   14      
     | |  \  /          6    10     |
           | \          /     \     |
      4 5  6      6       9   10    14
'''
def merge(L,R):
    # in case that there are no values in L or right return the other
    # list
    print(f'left = {L}   right = {R}')
    if len(L) == 0:
        return R
    if len(R) == 0:
        return L

    sorted = [] 
    # if we are not at the end.
    #i is left index anr j is right index
    i = j = 0
    #while sorted is shorter then the combined length of both lists 
    while len(sorted) < len(R) + len(L):
        # append shortest value
        if L[i] <= R[j]:
            sorted.append(L[i])
            i+=1
        else:
            sorted.append(R[j])
            j+=1

        # if you reach the end of either list then you can just finish
        # by appending the rest of the other list.
        if i == len(L):
            sorted+=R[j:]
            break

        if j == len(R):
            sorted+=L[i:]
            break
    print(f'sorted list = {sorted}')
    return sorted
'''
merge sort: 
    divide the array into 2 parts from the mid point recursivly
    until you are down to one value each, then

'''
def merge_sort(li):
    if len(li) < 2:
        return li

    mid = len(li) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        L=merge_sort(li[:mid]),
        R=merge_sort(li[mid:]))



#running all functions
print(f'insert sorting')
insert_sort([4,2,1,5,3])
print(f'bubble sorting')
bub_sort([4,2,1,5,3])
print(f'selection sorting')
sel_sort([4,2,1,5,3])
print(f'\nquick sorting: starting with {[4,2,1,5,3,1]}')
print(Quick_sort([4,2,1,5,3,1]))
print(f'\nmerge sorting: starting with {[4,5,2,1,3,7]}')
merge_sort([4,5,2,1,3,7])