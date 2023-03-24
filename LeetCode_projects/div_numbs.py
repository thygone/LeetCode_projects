'''
Author: Dane Selch
source: LeetCode

description
 Given an array of distinct integers candidates and a 
 target integer target, return a list of all unique 
 combinations of candidates where the chosen numbers sum 
 to target. You may return the combinations in any order.

 The same number may be chosen from candidates an unlimited
 number of times. Two combinations are unique if the 
 frequency
 of at least one of the chosen numbers is different.

 The test cases are generated such that the number of 
 unique combinations that sum up to target is less than 
 150 combinations for the given input.

 ex:
 input: [2,3,7] target = 7
 output [[2,2,3], [7]]
 explained: 2+2+3 == 7 and 7 = 7
   >> numbers can repeat.

'''

'''
psudo:
goal start with smallest value and make my way up. 
ex:
        target 21 array = [2,3,4,5,10,15]
        loops logic
            21 % (2)  == 0
            no
                21 / 2 = 10.5
                temp = round(10.5) - 1 = 10 -1 = 9
                j = i+1
                while numb[j] < 2*numb[i]              { while numb{j} < (2*2)}                             
                    numb[i] + numb[j]== target # once you hit 2x you don't need to test any more.        
                        yes >>
                        no >> j++ 
            i = 0
            2*9...+3 = 21 good
            2*9 + 4 > 21
            2*8 + 3 < 21
            2*8 + 3*2 > 21
            2*8 + 4 < 21
            ...
            ...
            n[0] + n[1]
            2*7 + 3 < 21            (17) = const1 = 2*7 + 3
            2*7 + 3 + 3 < 21        (20) = const2 = 2*7 + 3*2
            2*7 + 3 + 3 + 3 > 21    (23) = const2 fail
            2*7 + 3 + 4 = 21        (21) = const2             
            2*7 + 4 < 21            (18)
            2*7 + 4 * 2 > 21        (22)
            ...
            2*6 = const0            (12) = const0
            2*6 +3 < 21             (15) = const0 + numbs[i+1] = const1     
            2*6 + 3 +3              (18)  const1 + 3 = const2
            2*6 + 3 + 3 + 3         (21)  const2 + 3 = target  PASS
            2*6 + 3 +  4            (19)  const1 + 4 = const2B
            2*6 + 3 + 4 + 4         (23)  const2b + 4 > target  FAIL
            2*6 + 3 + 5             (20)  const1 + 5 = const2C
            2*6 + 3 + 5 + 5         (25)  const2C + 5 > target  FAIL
            2*6 + 3 + 10            (25)  const1 + 10 > target FAIL  N-1
            2*5                     (10) = new const0B
            2*5 + 3                 (13) = const0B + numbs[i+1] = const1
            2*5 + 3+3               (16) = const1(13) + 3 = const2
            2*5 + 3+3+3             (19) = const2(16) + 3 = const3
            2*5 + 3+3+3+3           (22) = const3(19) + numbs[i+1] > 21 FAIL
            2*5 + 3+3+4             (20) = const2(16) + 4 = const3B
            2*5 + 3+3+4+4           (24) = const3B(20) + 4 > 21 FAIL
            2*5 + 3+3 + 5           (21) = const2(16) + 5 == PASS
            2*5 + 3+4               (17) = const1(13) + 4
            ....
            i = 1
            j = i+1
            21 % 3 = 0
            21/3 = 7 = N 
            while N >= 1
                temp = 3*N
                temp + X == 21
                 N--
            logic graph 
            3 * 7 = 21        >= 21     N = 6 
            3 * 6 = 18 = temp    
            temp + 4 = 22     >= 21     N = 5
            3 * 5 + 4 = 19      < 21              
            3 * 5 + 4 + 4 = 23  > 21                 
            3 * 5 + 5 = 20      < 21
            3 * 5 + 5 + 5 = 25  > 21
            3 * 5 + 6 = 21      >= 21   N = 4
            3 * 4 + 4 = 16      ...
            3 * 4 + 4 + 4 = 20  ...
            3 * 4 + 4 + 4 + 4 = 24 >=21   
            3 * 4 + 4 + 5 = 21   
            3 * 4 + 5 = 17 
            3 * 4 + 5 + 5 = 22
            3 * 4 + 10 = 22       N = 3
            3 * 3 = 9
            3 * 3 +             

## all 1st value

'''
#brute force method
solutions = []
#######################################
# function: add_numbers
# purpose: it will check if 2x the current value will 
#       result in passing the target. if it does it will incrament in the 
# list of valuse. if not it will add the number to the current equation and 
# recursivly call itself.
# input: numbs > an arrey that holds all the numbers submitted
#        i > the index value being used
#        equation > the current equation being used
#        target > the target value
def add_numbers(numbs,equation,target):
    global solutions
    i = 0
    while i < len(numbs): # go through all numbers in sequence 
        equation[j] = numbs[i]
        print(f'current station i = {i} equation = {equation}')
        print(f'total = {sum(equation)+numbs[i]}')
        print(j)
        if sum(temp) == target:
            solutions.append(equation)
            print("pass")
        elif sum(temp) > target:
            equation[j] = 0
            print('overshot')
        elif sum(temp) < target:
            print("needs more")
            add_numbers(numbs,i,temp,j+1,target)
            
        
        i+=1
        


    
test = [2,3,5,7]
expected = [[2,2,3],[2,5],[7]]
add_numbers(test,0,[],0,7)
print(solutions)
print(expected)
# challenge to get it to be better 
# solutions = []
# # finds all numbers in the given list that are multiples of the first.
# def replace(val1,val2,solution):
#     global solutions
#     temp = solution
#     temp.remove(val1)
#     temp.remove(val2)
#     temp.append(val1+val2)
#     solutions.append(temp)

# def find_additional_solutions(solution, numbs, target):
#     global solutions
#     for i in range(len(solution)-1):
#         for j in range(len(solution)):
#             if solution[i] + solution[j] in numbs:
#                 replace(solution[i],solution[j], solution)
