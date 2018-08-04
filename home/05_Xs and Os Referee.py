def checkio(game_result: list) -> str:
    li = []
    for row in game_result:
        li.append(list(row))
    
    ans3 = ''
    ans4 = ''
    for i in range(len(row)):
        ans1 = ''
        ans2 = ''

        ans3 += li[i][i]
        ans4 += li[i][len(row)-i-1]

        for j in range(len(row)):
            ans1 += li[i][j]
            ans2 += li[j][i]
        if ans1 == 'XXX' or ans2 == 'XXX':
            return 'X'
        elif ans1 == 'OOO' or ans2 == 'OOO':
            return 'O'
    
    if ans3 == 'XXX' or ans4 == 'XXX':
        return 'X'
    if ans3 == 'OOO' or ans4 == 'OOO':
        return 'O'
    
    return 'D'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

'''
def checkio(game_result):
    # Check rows
    for row in game_result:
        if row[0] == row[1] == row[2] != ".":
            return row[0]

    # Check colums
    for col in range(3):
        if game_result[0][col] == game_result[1][col] == game_result[2][col] != ".":
            return game_result[0][col]

    # Check diagonals
    if game_result[0][0] == game_result[1][1] == game_result[2][2] != ".":
        return game_result[1][1]
    if game_result[2][0] == game_result[1][1] == game_result[0][2] != ".":
        return game_result[1][1]
    return "D"
-------------------------------------
def checkio(result):
    rows = result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)

    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'
-------------------------------------------
def checkio(board):
    # First we put everything together into a single string
    x = "".join(board)

    # Next we outline the 8 possible winning combinations. 
    combos = ["012", "345", "678", "036", "147", "258", "048", "246"]
  
    # We go through all the winning combos 1 by 1 to see if there are any
    # all Xs or all Os in the combos
    for i in combos:
        if x[int(i[0])] == x[int(i[1])] == x[int(i[2])] and x[int(i[0])] in "XO":
            return x[int(i[0])]
    return "D" 
----------------------------------------------
def checkio(game_result):
    for player in 'XO':
        if any(row == player*3 for row in game_result):
            return player
        if any(''.join(col) == player*3 for col in zip(*game_result)):
            return player
        if all(row[i] == player for i, row in enumerate(game_result)):
            return player
        if all(row[i] == player for i, row in zip((2, 1, 0), game_result)):
            return player
    else:
        return 'D'
'''


