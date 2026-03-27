class Solution:
    def ladderLength(self, beginWord: str, endword: str, wordList: List[str]) -> int:
        st = set(wordList)
        n = len(st)
        q = []
        if endword not in st:
            return 0
        q.append((beginWord,1))
        while q:
            word,step = q.pop(0)

            for i in range(len(word)):
                original = word[i]
                if word == endword:
                    return step
                for j in range(ord('a'),ord('z')+1):
                    val = word[:i]+chr(j)+word[i+1:]
                    if val in st:
                        st.remove(val)
                        q.append((val,step+1))
            word = word[:i]+original+word[i+1:]
        return 0

        
                

        