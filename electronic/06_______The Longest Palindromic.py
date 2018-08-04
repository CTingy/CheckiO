def longest_palindromic(text):
    result = ''
    for i in range(len(text)):
        for j in range(i+1, len(text)+1):
            subtext = text[i:j]
            if (subtext == subtext[::-1]) & (len(text[i:j]) > len(result)):
                result = subtext
    return result


'''
if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"

---------------
def longest_palindromiclongest_palin (text):
    w= len(text)

    substrings= [text[i:i+j] for j in range(1,w+1) for i in range(w) if i+j<=w]
    palindromic = [s for s in substrings if s==s[::-1]]
    
    return max(palindromic, key=len)
-------------------------------
def longest_palindromic(text):
    return max([text[b:e] for b in range(len(text)+1) for e in range(b+1, len(text)+1) if text.find(text[b:e][::-1]) != -1], key=len)
----------------------------------------
'''