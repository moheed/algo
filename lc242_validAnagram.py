class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Anagram: string 2 is formed by some other permutation of characters from first string.
        Idea1. is to loop over target string and 
        matching chars from first string.   O(n**2)
        
        Idea2: Loop over src string. 
        for each char in src string, 
            If not found in hash_map(), add to hash_map.(set1)
            increment its occurance in hash_map(for repeated chars)
        loop-over target string and see if hashing results in same hash-map
        
        Idea3:same as hash(but use array as hash)create an array of size alphabet-set.
        for src-string loop-over and increment array for each character occurances.
        
        """
        
        """
        This is map solution, works fine 65% faster than other submission
        RUNTIME:48ms, better than the later two:
        1. uses twice hash_map size than the prev
        2. run 2*n iteration (where n is the largest string input size.)
        3. hash-table lookup is O(1)
        Starts from below this line
        """
        
        #Using zip to iterate simultaneously: this has same runtime as of two for loop for x/y
        hmap={}
        for x,y in zip_longest(s,t,fillvalue='-'):
            
            try:
                hmap[x]= hmap[x]+1  #{'a':2, 'b':3.. etc}store occuracne of chars.
            except KeyError:
                hmap[x]=1  #store for first time
            try:
                hmap[y]= hmap[y]-1  #{'a':2, 'b':3.. etc}store occuracne of chars.
            except KeyError:
                hmap[y]=-1  #store for first time
            
        return all(value == 0 for value in hmap.values())
        
       #nothing gets executed below this line
    
    
       
        hmap={}
        for x in s:
            
            try:
                hmap[x]= hmap[x]+1  #{'a':2, 'b':3.. etc}store occuracne of chars.
            except KeyError:
                hmap[x]=1  #store for first time
            """
            if x in hmap:
                hmap[x]= hmap[x]+1  #{'a':2, 'b':3.. etc}store occuracne of chars.
            else:
                hmap[x]=1  #store for first time
            """
        for y in t:
            """
            if y in hmap:
                if hmap[y]==1:
                    hmap.pop(y)
                else:
                    hmap[y]=hmap[y]-1
            else:
                return False
            """
            try:
                hmap[y]=hmap[y]-1
                if hmap[y]==0:
                    hmap.pop(y)
            except KeyError:
                return False
        
        if not hmap:
            return True
        else:
            return False
        
        
        """
        Array kind of solution(using build-in list), 
        basically str_array works as hash_map and we run over both the strings
        incrementing value at index that are found while scanning source and decrementing while scanning
        target. this scanning of src and target is done in single loop
        RUNTIME:56 ms for anagram/nagaram: Mostlikely because runtime is 4*n(n is large string input size)
        """
        """
        str_array = [0]*26
        size1 = len(s)
        size2 = len(t)
    
        if size1!=size2:
            return False
    
        for i in range(size1):
            str_array[97-ord(s[i])]+=1
            str_array[97-ord(t[i])]-=1
                       
        for i in range(26):
            if str_array[i] > 0:
                return False
        
        
        return True
        
        """
        """
        Actual array solution: Slowest: I guess because, python dont have a built-in array data-structure
        rather it has list. array module which exist is not the best array implementation!
        """
        """
        import array as arr
        #array(typecode [, initializer])
        init_arr=[0]*26
        str_array=arr.array('i',init_arr)
        size1 = len(s)
        size2 = len(t)
    
        if size1!=size2:
            return False
    
        for i in range(size1):
            str_array[97-ord(s[i])]+=1
            str_array[97-ord(t[i])]-=1
                       
        for i in range(26):
            if str_array[i] > 0:
                return False
        
        
        return True
        """
    
    
        
