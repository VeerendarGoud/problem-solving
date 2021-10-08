def count_construct(targetString, wordBank):
    """[summary]

    Args:
        targetString ([string]): [description]
        wordBank ([list]): [description]
    """

    target_len = len(targetString)
    table = [0] * (target_len+1)
    # print(table)
    # base case
    table[0] = 1

    for i in range(target_len):
        for word in wordBank:
            # if the word matches the character string prosition i
            if table[i] != 0:
                if word == targetString[i:i+len(word)]:
                    table[i+len(word)] += table[i]
                
    return table



print(count_construct('abcdef',['ab','abc','cd','def','abcd']))
print(count_construct('purple',['purp','p','ur','le','purpl']))
print(count_construct('abcdef',['ab','abc','cd','def','abcd','ef','c']))
print(count_construct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
print(count_construct('enterapotentpot',['a','p','ent','enter','ot','o','t']))
