
def lengthOfLongestSubstring(s):
        
    max_curr_s = ''
    fast = 0
    count_dict = dict()
    max_len = 0
    curr_s = ''
    curr_len = len(s)
    
    while fast < curr_len:
        
        if s[fast] in count_dict:

            count_dict[s[fast]] +=1
            curr_s = curr_s + s[fast]
            
            for ch in curr_s:
                if ch == s[fast]:
                    curr_s = curr_s[1:]
                    count_dict[s[fast]] -=1
                    break
                else:
                    curr_s = curr_s[1:]
                    del count_dict[ch]     
        else:
            count_dict[s[fast]] = 1
            curr_s = curr_s + s[fast]

            if len(curr_s) > max_len:
                max_len = len(curr_s)
                max_curr_s = curr_s

        #print(max_curr_s)
        fast +=1
    print(max_curr_s)
    return max_len


s = "abcabcbb"
print(lengthOfLongestSubstring(s))
s = "bbbbb"
#print(lengthOfLongestSubstring(s))
s = ""
#print(lengthOfLongestSubstring(s))
s = "pwwkew"
#print(lengthOfLongestSubstring(s))