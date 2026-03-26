from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #the empty value for the keys is  a list
        anagram_map=defaultdict(list)#initilize a dictinary
        results=[]#initialize the output...which is a list

        #iterate through the input array 
        for words in strs:
            sorted_words=tuple(sorted(words))
            #we are making the sorted words as a key 
            #key must be immutable..sorted() returns a list whch is mutable, hence we explixitly convert it into a tupe which is  immutable
            anagram_map[sorted_words].append(words)
        
        for value in anagram_map.values():
            results.append(value)
        return results


