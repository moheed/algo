class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        A 1 dimension dp problem:
        More about fundamentals on DP: later.
        DP problems can be of two type: (Any other type?)
            i. Optimization problems
            ii.Combinatorial problems.
        Steps to tackle a problem using DP:
        step#0: Check if solvable by DP: [Optional?]
            a. Show that problem can be broken in subproblems.
            b. Show that problem follows "principle of optimality"
            
            Principle of Optimality:
                Problem can be solved by taking sequence of decision to get optimal solution.
            b1. Optimal substructure
                Optimal solution for problem can be obtained by using optimal solutions of its subprob.
            b2. Overlapping Subproblems : Smell recursion.
        
        Step#1
        Define sub problems
        
        Step#2
            write down recurrence that relate to solution
        
        Step#3
            Recognize and solve base cases.
        
        Note1: 
            While trying to solve dp problem, it is helpful 
                a. to think as 'creating table filling algo':
                b. know the calculation need to be done.
                c. pick the best order to do then
                d. Ignore ones, you dont have to fill in.
            This leads to backtracking.
            BackTracking:
                a. When trying memoized solution for a problem, start with backtrack solution that
                finds the correct answer.
                b. Backtrack solution enumerates all valid answer for the problem. Choose the best one!
            Typical Restriction while BackTracking:
                i. It should be a function, calculating the answer using recursion.
                ii. It should return answer with return statement and MUST not store answer 
                    somewhere else.
                iii.All non-local variables that this function uses MUST be READONLY. Function should
                    only modify its local variables and arguments.
              Restriction Note:
                i.The correctly written backtrack function should always represent an 
                answer to a well-stated question. While writing backtrack function, one 
                should create such question and check if it answers well-stated question.
                ii. minimize argument-space of backtrack function, if something can be computed within
                    backtrack function, just compute it.
                    
                    
        Note2:
        Top-down approach to any problem is to:[Memoization of recursive function ]
           Here state[n] is obtained by combining states that can reach to state[n]
           a. Write the recursive code
           b. Memoize the return value and use it to reduce recursive calls.
           Eg. 
        Bottom-up approach:[table filling] 
            Here state-trasition happens from base[0] to base[n]
            Start from base-case and keep filling table, reuse when needed
            Eg. factorial(n)
            
            
        Note3:
        To sum it up, if you identify that a problem can be solved using DP, try to create a 
        backtrack function that calculates the correct answer. Try to avoid the redundant arguments,
        minimize the range of possible values of function arguments and also try to optimize the time
        complexity of one function call (remember, you can treat recursive calls as they would run in
        O(1) time). Finally, you can memoize the values and don't calculate the same things twice.
        
        """
        
        #Approach
        """
            step#1: Define sub-problems: Identify states and their dependencies.
            if I somehow find content(k), for one additonal child ie content(k+1), given the same# 
            of cookies, I definitely can calculate content(k+1).
            Because if content(k) has exhausted all cookies, content(k+1) will be same as content(k)
            otherwise if there are cookies remaining, and 
                g[k+1]> s (for all s) then content(k+1)=content(k)
               or g[k+1] <= s (for some s) then content(k+1)= content(k)+1
            
            step#2:
            g[k] greed of kth child (with n child total), 
            s[] sizeofCookie with m cookies in total.
            content(k)= content(k-1) +1  } (if g[k]<= s, for some s in all s[]) && k <= m
                      = content(k-1)     }  otherwise 
                      
            step#3: Base cases.
            content(0)=1  if g[0] <= s[0]
                      =0   otherwise
            content(1)=content(0)+1         (if g[1] <= s for some s in all s[] ie s[0], s[1]) && 1<=m
                      =content(0)
            content(k) =content(k-1)        if k>m
            
            #step4: create a backtrack function
            
            /* ensure it returns an answer with a return stmt: how many content out of k child
                    ==>It returns number of content children for given k.
            
            def backtrack_content_child(k:int)->int:
                if k == 0:
                    return 0;
                if (k > numberofTotalCookies):
                    return backtrack_content_child(k-1)
                #k >=1                
                for i=0; i <numberofTotalCookie; i++:
                    if greed[k] > x:   
                        return backtrack_content_child(k-1)
                    else:
                        return (backtrack_content_child(k-1)+1)
                        
            step#5:
            since we reach to solution state(k) by using state[k-1], this is simply top-down
            and hence we use memoization and remove recusive calls. At each point in algorithm,
            before we return, we Memoize ie set CookieMemoArray[k] with current return value.
            However, as its easily seen, to run above algorithm, we only need previous value of
            CookieMemoArray[], only one variable will be sufficient to maintain this.
            [Actually that is what we want as answer, maxContentChild]
            
            def backtrack_content_child(k:int)->int:
                if k == 0:
                    CookieMemoArray[k]=0; #(actual implementation it will be maxContentChild )
                    return 0;
                if (k > numberofTotalCookies):
                    #return  backtrack_content_child(k-1), replaced with following 2 line
                    CookieMemoArray[k]=backtrack_content_child(k-1);
                    return  CookieMemoArray[k];#actual implementation, it will be maxContentChild  
                
                #k >=1                
                #NOTICE HOW this for-loop can be removed from within recursion, if we know the                           maxCookieSize
                for i=0; i <numberofTotalCookie; i++:
                    if greed[k] > cookie[i]:   
                        #return backtrack_content_child(k-1)  replace by following 2 line
                        CookieMemoArray[k] = backtrack_content_child(k-1)
                        return  CookieMemoArray[k]
                    else:
                        if we looped over all cookies and none of 
                        them have size cookie[i]>=greed[k]                        
                        #return (backtrack_content_child(k-1)+1) replaced by following 2 line
                        CookieMemoArray[k]=(backtrack_content_child(k-1)+1)
                        return  CookieMemoArray[k];#actual implementation, it will be maxContentChild
        
        step#6
            Final function follows below in actual code.
        
        """
        
        def maxCookieSize(s:List[int])->int:
            max=0
            for x in s:
                if max< x:
                    max=x;
            return max
        maxCookieLen=maxCookieSize(s)
        #maxContentChild=0
        s2=s
        s2.sort()
        s2=s2[::-1]#s2 is now sorted in decreasing
        global_index=0
        def backtrack_content_child(k:int, maxContentChild:int )->(int):
                
                cookiesLeft=len(s)-maxContentChild;
                print("cookiesLeft",cookiesLeft)
                if k > len(s) and cookiesLeft < 1:
                    return maxContentChild;
                
                for x in s:
                    if g[k] <= maxCookieLen and k<=len(s):
                        maxContentChild=maxContentChild+1
                    elif g[k] == maxCookieLen:
                        maxContentChild=maxContentChild+1
                
                    elif g[k] < maxCookieLen:
                        maxContentChild=maxContentChild+1
                    
                    
                print("g[",k,"]=",g[k]," CookiesLeft:", cookiesLeft, "ContentChilds:",maxContentChild,"MaxCookieLenSoFar:",maxCookieLen)
                return maxContentChild
                
        #definition of findContentChildred actual function
        maxContentChild=0
        print("size of input(g,s):", len(g),len(s))
        print("maxCookieLen:",maxCookieLen)
        for k in range(0, len(g)):
            if len(s) - maxContentChild ==0:
                break;
            
            maxContentChild = backtrack_content_child(k, maxContentChild);
            
            
        return maxContentChild
            
