def checkInclusion(s1,s2):
        
    s1_dict = dict()
    conti = False
    
    for ch in s1:
        if ch in s1_dict:
            s1_dict[ch] +=1
        else:
            s1_dict[ch] = 1
            
    for i in range(len(s2)):
        
        if s2[i] in s1_dict:
            permu_st = s2[i:i+len(s1)]
            print(permu_st)
            new_dict = dict()
            
            for ch in permu_st:
                if ch in new_dict:
                    new_dict[ch] +=1
                else:
                    new_dict[ch] = 1
            print(new_dict)
            print(s1_dict)
                
            if new_dict == s1_dict:
                return True
    return False

s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1,s2))
s1 ="ab"
s2 ="eidboaoo"
print(checkInclusion(s1,s2))
s1 = "a"
s2 = "ab"
print(checkInclusion(s1,s2))
s1 ="adc"
s2 = "dcda"
print(checkInclusion(s1,s2))

