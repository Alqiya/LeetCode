class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        t_dict={}

        def string_to_dict(string,dictionary):
            for letter in string:
                if letter in dictionary:
                    dictionary[letter]+=1
                elif letter==' ':
                    continue
                else:
                    dictionary[letter]=1
            return dictionary
            
        str_s=string_to_dict(s,s_dict)
        str_t=string_to_dict(t,t_dict)

        return str_s==str_t