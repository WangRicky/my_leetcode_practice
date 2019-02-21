class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        map = {}
        maxlen = 0
        length = 0
        offset = 0
        for x in s:
            if x in map:
                offset = max(map[x],offset)
            maxlen = max (maxlen,length - offset + 1)
            map[x] =length + 1
            length  += 1
        return maxlen