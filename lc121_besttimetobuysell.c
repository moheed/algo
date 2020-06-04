int find_max(int* a,int size){
    int i=0;
    int max=0;
    for (i=0; i<size; i++)
        if (max<a[i])max=a[i];
    return max;
}
/*Reivision Note: complexity constraint:runtime: in O(n) or O(nlgn)*/
int maxProfit(int* prices, int pricesSize){
    int i=0;
    int j=0;
    int p=0;//profit
    
    
    /*Optimal O(n) solution by using dp:
     * Idea: daily_possible_profit[day]=price[day]-min_buy_price [day =1 to size of input array]
     * min_buy_price: can be tracked while doing loop pass(as buy happens before sell)
     */
    int min_buy_price;
    if(pricesSize <1)return 0;
    min_buy_price=prices[0];//assume first day was the best day to buy(lowest buy), update it as iterate
    for(i=0; i<pricesSize; i++){
        if (p < (prices[i]-min_buy_price)) { //0 profit on first day
            p = prices[i]-min_buy_price;  //update for better profit
        }
        if (prices[i]<min_buy_price){
            //update the min_buy_price so that we can check optimal profit in future
            min_buy_price=prices[i];
        }
    }
    
