class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        groupby = {}
        ans = []
        
        for i in range(len(strs)):
            dic[i] = "".join(sorted(strs[i]))
        for k,v in dic.items():
            groupby[v] = [k] if v not in groupby.keys() else groupby[v] + [k]
        
        for value in groupby.values():
            tmp = []
            for i in value:
                tmp.append(strs[i])
            ans.append(tmp)
        return ans
