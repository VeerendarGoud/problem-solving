# def solve(A, B):
        
#     b_dict = dict()
#     b_len = len(B)
    
#     b_dict = dict()
#     b_len = len(B)
    
    
            
#     for i in range(len(A)):
#         if A[i] == B[0]:
#             if A[i:i+b_len] == B:
#                 return i+1        
#     return -1


# # A = "knpzitssxg"
# # B = "sxg"
# A = "kotzaxrgtjrah"
# B = "zaxrgt"
# print(solve(A, B))

# A = [1,0,0,0,1]
# B = [
#     [2,4],
#     [1,5],
#     [3,5]
# ]
# result = []
# for i in range(len(A)):
            
#     if i !=0:
#         A[i] += A[i-1]

# for row in B:

#     one_cunt = A[row[0]-1] - A[row[1]-1]
#     zero_count = ((row[1]-row[0])+1 )- one_cunt


#     result.append([one_cunt%2,zero_count])
    

# print(result)

# result = []

# for row in B:
        
#     sub_arr = A[row[0]-1:row[1]]
    
#     xor = sub_arr.pop()

#     if xor == 0:
#         zero_count = 1
#     else:
#         zero_count = 0
    
#     for ele in sub_arr:
#         xor ^= ele
#         if ele == 0:
#             zero_count += 1
        
    
#     result.append([xor,zero_count])

# print(result)

# A = 5
# B = [
#     [1,2,10],
#     [2,3,20],
#     [2,5,25]
# ]

# result = [0] * (A+2)

# for row in B:

#     print(row[0]-1,row[1]-1)

#     result[row[0]-1]  += row[2]
#     result[row[1]]  -= row[2]

# sum = 0

# for i in range(len(result)):
#    sum += result[i]
#    print(sum)

# print(result[:-1])

a = ['q','w','e','r','t']

# print(a.pop())
# a.append(10)
# print(a)

for i,a in enumerate(a):

    print(i,a)
   