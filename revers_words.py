def revers_words(stng):

    words = stng.split(' ')
    for i in range(len(words)):

        temp_st = ''

        for ch in words[i]:

            temp_st = ch+temp_st

        words[i] = temp_st

    return ' '.join(words)

stng = "Let's take LeetCode contest"
print(revers_words(stng))

