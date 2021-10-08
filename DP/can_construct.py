def can_construct(targetString, wordBank):
    """[summary]

    Args:
        targetString ([string]): [description]
        wordBank ([list]): [description]
    """

    target_len = len(targetString)

    table = [False] * (target_len+1)
    # print(table)
    # base case
    table[0] = True

    for i in range(target_len):
        for word in wordBank:
            # if the word matches the character string prosition i
            if word == targetString[i:i+len(word)]:
                table[i+len(word)] = True
    return table[target_len]



print(can_construct('abcdef',['ab','abc','cd','def','abcd']))
print(can_construct('purple',['purp','p','ur','le','purpl']))
print(can_construct('abcdef',['ab','abc','cd','def','abcd','ef','c']))
print(can_construct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
print(can_construct('enterapotentpot',['a','p','ent','enter','ot','o','t']))
