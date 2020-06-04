class Solution:
    def lexo(self, word1, word2, populate_order):
        count=0;
        lw1=len(word1)
        lw2=len(word2)
        i=0
        while count<lw1:
            if count==lw2:#word2 finished
                return False
            x=word1[count]
            y=word2[count]
            if populate_order[ord(x)-ord('a')] < populate_order[ord(y)-ord('a')]:#return true
                print(x,populate_order[ord(x)-ord('a')], y, populate_order[ord(y)-ord('a')])
                return True
            elif populate_order[ord(x)-ord('a')] == populate_order[ord(y)-ord('a')]:
                count+=1
            else:
                return False
        if count == lw1:
            return True
        return False
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        populate_order=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#26 alphabets
        count=0
        index=0
        for x in order:
            index=ord(x)-ord('a')
            populate_order[index]=count;
            count+=1
        print(populate_order)
        i=0;
        while i< len(words)-1:
            if not self.lexo(words[i], words[i+1], populate_order):
                return False
            i+=1
        return True
        
       
