class Solution:
    def defangIPaddr(self, address: str) -> str:
        i=0
        j=0
        strlist=list(address)
        defang=[]
        while i< len(strlist):
            if strlist[i] == '.':
                 defang.append('[')
                 defang.append('.')
                 defang.append(']')
            else:     
                defang.append(address[i])
            i+=1
        retstr=""
        
    
        # return string   
        return (retstr.join(defang))
        
            
