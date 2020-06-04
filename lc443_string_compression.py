class Solution:
    def compress(self, chars: List[str]) -> int:
        truncate=0
        p=0
        q=0
        count=0
        while p< len(chars):
            while q < len(chars):
                if chars[p] == chars[q]:
                    count=count+1
                else:
                    break
                q+=1
            if count>1:
                chars[truncate]=chars[p]
                truncate+=1
                i=0;
                while i < len(str(count)):
                    chars[truncate]=(str(count))[i]
                    truncate+=1
                    i+=1
            else:
                chars[truncate]=chars[p]
                truncate+=1
            
            p=q
            count=0
                       
            
        return truncate;
        
