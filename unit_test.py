from random import sample,randint
from sudoku import isValid

def pattern(r,c,base,side): return (base*(r%base)+r//base+c)%side

def shuffle(s): return sample(s,len(s))

def generateValidSudoku():
    base  = 3
    side  = base*base
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c,base,side)] if randint(0,1)==1 else "." for c in cols ] for r in rows ]

    # for line in board: print(line)
    print(isValid(board))

def generateRandomSudoku():
    base  = 3
    side  = base*base
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [randint(1,9) if randint(0,1)==1 else "." for c in cols ] for r in rows ]
    print(board)
    # for line in board: print(line)
    print(isValid(board))
generateValidSudoku()
generateRandomSudoku()