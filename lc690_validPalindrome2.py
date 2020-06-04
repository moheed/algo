class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Approach: Check Plaindrome
        abcdedcba
        =>two pointers one at begin other at end, keep comparing, if they meet and everything match
        its palindrome.
        Use same approach with two pointers, start from beg and end. at the first time, when
        they dont match:
            check which side has the wrong char.
            (skip-over it.)
            continue remaining iteration to see if its palindrome
            
        """
        
        i=0
        j=len(s)
        print(j)
        if j <3:
            return True
        #anotherway to reverse "".join(reversed(input)):NOTE this is O(1) in python: Is it?
        rev_s=s[::-1]   
        if s == rev_s:
            return True
        
        
        
        #we have almost same string
        #find where they differ, one way is to iterate, which is O(n)
        #Other way is to part the straight and reversed string in half O(lgn)
        """
        l=0
        t=len
        
        mid=t//2
        lefts=s[l:mid]
        rights=s[mid:t]
        rlefts=rev_s[l:mid]
        rrights=rev_s[mid:t]
        
        while t>=2:
            if lefts !=rlefts:
                tmp=mid
                mid=t//2
                t=mid
                lefts=lefts[l:mid]
                rights=s[mid:t]
                rlefts=rlefts[l:mid]
                rrights=rlefts[mid:t]
            elif rights !=rrights:
                left_search=False
                l=mid
                mid=t//2
            else:
                continue
        
        
        
        
        
        """
       
        i=0
        j=len(s)
        print(j)
        if j <3:
            return True
        skipped_one_char=False
        j=j-1#last element at len-1
        while i<=j:
            if s[i]==s[j]:
                i+=1
                j-=1
                continue
            else:
                if skipped_one_char==True:
                    #print("return:", i,s[i], j, s[j])
                    return False
                skipped_one_char=True
                #skip left side one char Not sufficient condition to make decision
                #if a[i+1]==a[j]:
                #For eg, as soon as u skip this what if next char in string matches to the 'toberemoved'
                #char of string
                #eg "cuppucu"  ==> undesired char in string is rightmost 'u'.
                #on first iteration, since we increment i first, and a[i](u) matches the right pointer
                # of string which is actually undesirable.
                #
                #sufficient condition is to check further one element and see if we are on right track
                #if we check one more element, we gaurantee that palindromness property will be preserved
                #if that is not the case, then string is not palindrom from left side checks with atmost
                #one extra char.
                #We dont need to consider this for right side, because left check is always done first,
                #and if it fails(checking two elements in row) that means right side skipping 1 char 
                #is the only option remaining to try. and hence else is sufficient.
                if s[i+1]==s[j] and s[i+2]==s[j-1]:#on right track: 
                    #check if we access out of bound!we dont go out of bound, because atmost 1 char means
                    # we check 2nd extra element. As string of len <2 are trivial solution, we never go 
                    #out of bound.(string len will always be strictly greater than 2)
                    i+=1
                    #print ("skipleft", i, j)
                else:#skip right one char
                    j-=1
                    #print ("skip", i, j)
                continue
        return True
        
        """
        def isPalin(s, i, j):
            t = s[i:j+1]
            return t == t[::-1]
        
        l = 0
        h = len(s) - 1
        while l < h :
            if l < h and s[l] == s[h]:
                l += 1
                h -= 1
                continue
            elif l < h and s[l] != s[h]:
                return isPalin(s, l+1, h) or isPalin(s, l, h-1)
        
        return True
        """
