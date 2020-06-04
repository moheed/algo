class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1=len(num1)
        l2=len(num2)
        result=""
        carry=0
        i=0
        #map to store chars to int mapping
        aton={'0':0, '1':1,'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,'9':9}
        ntoa={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
        while i< l2 and i<l1:
            val= aton[num1[l1-i-1]] + aton[num2[l2-i-1]]+carry
            if val > 9:
                val=val%10
                carry=1
            else:
                carry =0
            result=ntoa[val]+result
            i+=1
        if i==l2:#num2 finished
            while i< l1:#one of the input is finished
                val= aton[num1[l1-i-1]] +carry
                if val > 9:
                    val=val%10
                    carry=1
                else:
                    carry =0
                result=ntoa[val]+result
                #print (i,result)
                i+=1
        else:
            while i< l2:#one of the input is finished
                val= aton[num2[l2-i-1]] +carry
                if val > 9:
                    val=val%10
                    carry=1
                else:
                    carry =0
                result=ntoa[val]+result
                #print (i,result)
                i+=1
        if carry:
            result=ntoa[carry]+result
            
        return result
