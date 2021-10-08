def all_construct(targetString, wordBank):
    """[summary]

    Args:
        targetString ([string]): [description]
        wordBank ([list]): [description]
    """

    target_len = len(targetString)
    table = [[] for i in range(target_len+1)]
    # print(table)
    # base case
    table[0] = [[]]

    for i in range(target_len):
        for word in wordBank:
            # if the word matches the character string prosition i
            if len(table[i]) != 0:
                if word == targetString[i:i+len(word)]:
                    for li in table[i]:
                        table[i+len(word)].append([*li, word])

    return table[target_len]



print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef']))
print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(all_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(all_construct('qqqqqqqqqqqqqqqqqqqqq', ['q', 'qqq', 'qqqqq', 'qqqqqqq', 'qqqqqq', 'qqqq', 'qqqqqqqqqq']))
