'''
 Author: Dane Selch
 source: LeetCode

 Directions:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
Input: board = 
[["5","3",".",".","7",".",".",".","."] row 1
,["6",".",".","1","9","5",".",".","."] row 2
,[".","9","8",".",".",".",".","6","."] row 3
,["8",".",".",".","6",".",".",".","3"] ...
,["4",".",".","8",".","3",".",".","1"] .
,["7",".",".",".","2",".",".",".","6"] .
,[".","6",".",".",".",".","2","8","."] .
,[".",".",".","4","1","9",".",".","5"] .
,[".",".",".",".","8",".",".","7","9"]] row 9
Output: true

'''

def isValidSudoku(board) -> bool:
    if check_row(board) and check_col(board) and check_box(board):
        return True
    else:
        return False
def check_row(board) -> bool:
    for row in board:
        numbers = []
        for square in row:
            if square != ".":
                if square in numbers:
                    return False
                else:
                    numbers.append(square)
    return True # only return true if everything passes    
def check_col(board) -> bool:
    numbers = [[0],[0],[0],[0],[0],[0],[0],[0],[0]] # hold all numbers per column
    for row in board:
        for square in range(len(row)):
            if row[square] in numbers[square]:
                print(row[square])
                print(numbers[square])
                return False
            elif row[square] != ".":
                numbers[square].append(row[square])
    return True


def check_box(board) -> bool:
    numbers = [[0],[0],[0],[0],[0],[0],[0],[0],[0]] # holds numbers in each square
    for row in range(len(board)):        
        for col in range(len(board[row])):#col number
            val = board[row][col]
            if val != ".":
                
                #top 3 boxes
                if row < 3 and col < 3: # box 1
                    if val in numbers[0]:
                        return False
                    else:
                        numbers[0].append(val)

                elif row < 3 and col >= 3 and col < 6: # box 2
                    if val in numbers[1]:
                        return False
                    else:
                        numbers[1].append(val)
                elif row < 3 and col >= 6: # box 3    
                    if val in numbers[2]:
                        return False 
                    else:
                        numbers[2].append(val)

                # 2nd row of boxes      
                elif row >= 3 and row < 6 and col < 3: # box 4
                    if val in numbers[3]:
                        return False
                    else:
                        numbers[3].append(val)
                elif row >= 3 and row < 6 and col >= 3 and col < 6: # box 5
                    if val in numbers[4]:
                        return False
                    else:
                        numbers[4].append(val)
                elif row >= 3 and row < 6 and col >= 6: # box 6    
                    if val in numbers[5]:
                        return False   
                    else:
                        numbers[5].append(val)
                
                #last row of boxes
                elif row >= 6 and col < 3: # box 7
                    if val in numbers[6]:
                        return False
                    else:
                        numbers[6].append(val)
                elif row >= 6 and col >= 3 and col < 6: # box 8
                    if val in numbers[7]:
                        return False
                    else:
                        numbers[7].append(val)
                elif row >=6 and col >= 6: # box 9    
                    if val in numbers[8]:
                        return False
                    else:
                        numbers[8].append(val) 

            

    return True



board = [["5","3",".",".","7",".",".",".","."] 
        ,["6",".",".","1","9","5",".",".","."] 
        ,[".","9","8",".",".",".",".","6","."] 
        ,["8",".",".",".","6",".",".",".","3"] 
        ,["4",".",".","8",".","3",".",".","1"] 
        ,["7",".",".",".","2",".",".",".","6"] 
        ,[".","6",".",".",".",".","2","8","."] 
        ,[".",".",".","4","1","9",".",".","5"] 
        ,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))
