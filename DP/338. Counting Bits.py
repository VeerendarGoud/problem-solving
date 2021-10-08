# brute force

def number_ones(n):

    if n == 0:
        return 0

    count = 0

    # while n >0:
    #     if n&1:
    #         count+=1
    #         n >>= 1

    while (n):

        n = n & (n-1)
        count += 1

    return count

n = 36
print(number_ones(n))

def counting_bits(n):

    number_of_bits_array = [0]*(n+1)

    for i in range(n+1):

        number_of_bits_array[i]= number_ones(i)

    
    return number_of_bits_array


# n = 2
# print(counting_bits(n))
# n = 3
# print(counting_bits(n))
# n = 7
# print(counting_bits(n))
# n = 15
# print(counting_bits(n))
# n = 31
# print(counting_bits(n))
#print([i for i in range(n+1)])
        