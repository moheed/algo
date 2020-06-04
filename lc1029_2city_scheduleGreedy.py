class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """Solution times out
        from itertools import combinations
        
        costA=[]
        costB=[]
        tc=[]
        #costs=[[20,40], [30,50], [40,60], [50,70], [80,90],[100,90]]
        num_people=len(costs)
        for x in costs:
            costA.append(x[0])
            costB.append(x[1])
        indexA=[]
        for x in range(0, num_people):
            indexA.append(x)
        comb = combinations(indexA, num_people//2)
        print(indexA)
        tcA=0
        tcB=0
        gtcB=0
        for x in costB:
            gtcB+=x
        
        for indices in list(comb):
            #print(indices)
            tcB=gtcB   
            for x in indices:
                tcA+=costA[x]
                tcB-=costB[x]
            
            tc.append(tcA+tcB)
           
            tcA=0
            tcB=0
        """
        def abs_diff_compare(x=[1,2], y=[3,4]):
            x1=x[0]-x[1] if x[0]>=x[1] else x[1]-x[0]
            y1=y[0]-y[1] if y[0]>=y[1] else y[1]-x[0]
            return x1 if x1>y1 else y1
        save_costs=costs
        costs.sort(reverse=True, key=abs_diff_compare)
        print(costs)
        nA=0
        nB=0
        tc=0
        num_people=len(costs)
        max_ppl=num_people//2
        
        for x in costs:
            if nA< max_ppl and nB< max_ppl :
                if x[0] <x[1]:
                    nA+=1
                    tc+=x[0]
                else:
                    nB+=1
                    tc+=x[1]
            elif nA< max_ppl:
                nA+=1
                tc+=x[0]
            elif nB< max_ppl:
                nB+=1
                tc+=x[1]
            
            
        return tc
