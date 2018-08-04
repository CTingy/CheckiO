def safe_pawns(pawns: set) -> int:
    safe_pawns = set()
    while pawns:
        pawn = max(pawns, key=lambda x: x[1])
        next_pawn = {chr(ord(pawn[0])+1) + str(int(pawn[1])-1), chr(ord(pawn[0])-1) + str(int(pawn[1])-1)}
        if next_pawn & pawns:
            safe_pawns.add(pawn)
        pawns.remove(pawn)
    return len(safe_pawns)
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

'''
def safe_pawns(pawns):
    safe_count = 0
  
    for item in pawns:
        if chr(ord(item[0])+1) + str(int(item[1])-1) in pawns:
            safe_count += 1
        elif chr(ord(item[0])-1) + str(int(item[1])-1) in pawns:
            safe_count += 1
    return safe_count
----------------------------------------------------------------
def safe_pawns(pawns):
    answer = 0
    for pawn in pawns :
        if chr(ord(pawn[0])-1)+str(int(pawn[1])-1) in pawns or chr(ord(pawn[0])+1)+str(int(pawn[1])-1) in pawns : answer +=1
    return answer
'''