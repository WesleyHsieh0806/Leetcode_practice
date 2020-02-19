class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 目標:從string最前到最後 並利用front right兩標兵紀錄substring頭尾index
        # 每當遇到重複的字元front移動到前面那個重複字元的後面 例如abcda
        # 遇到第二個a 就會移動到b的index
        # Time complexity:O(n^2)
        maximum = 0
        front = 0
        right = 0
        char_list = {}
        if len(s) == 0:
            return 0
        for i in range(0, len(s)):
            if s[i] not in char_list:
                char_list[s[i]] = i
                right = i
            else:

                if (right-front+1) > maximum:
                    maximum = (right-front+1)
                pivot = char_list[s[i]]+1
                for j in range(front, pivot):
                    del char_list[s[j]]
                front = pivot
                char_list[s[i]] = i

                right = i
        if (right-front+1) > maximum:
            maximum = (right-front+1)
        return maximum
