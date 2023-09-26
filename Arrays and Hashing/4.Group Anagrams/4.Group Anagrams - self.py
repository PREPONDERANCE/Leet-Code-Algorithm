def groupAnagrams(strs: list[str]) -> list[list[str]]:
        allNone = False
        count = 0
        arr = [[]] * 1
        arr[0] = []
        for string in strs:
            count += 1
            if string == "": allNone = False
            else: allNone = True
        if allNone == False:
            for i in range(count):
                arr[0].append("")
            return arr
        
        def isAnagram(s: str, t: str) -> bool:
            if len(s) != len(t): return False
            if s == t: return True

            countS, countT = {}, {}
            for i in range(len(s)):
                countS[s[i]] = countS.get(s[i], 0) + 1
                countT[t[i]] = countT.get(t[i], 0) + 1

            for c in countS:
                if countS[c] != countT.get(c, 0):
                    return False
            return True

        hashMap, i = {}, 0
        for string in strs:
            if len(hashMap) == 0:
                hashMap[string] = hashMap.get(string, i)
            else:
                for key in hashMap:
                    if isAnagram(key, string):
                        hashMap[string] = hashMap.get(string, hashMap[key])
                        break
                if not isAnagram(key, string):
                    i += 1
                    hashMap[string] = hashMap.get(string, i)
        
        nums = max(hashMap.values()) + 1
        target_arr = [[]] * nums
        for i in range(nums):
            target_arr[i] = []
        
        for key in hashMap:
            print(key, hashMap[key])
            target_arr[hashMap[key]].append(key)
            
        return target_arr
        
        
strings = ["c", "c"]
print(groupAnagrams(strings))