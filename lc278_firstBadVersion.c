// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) {
     int low=1;
     int high=n;
     int mid=0;
     int answer=-1;
    while(low<=high){
        mid=high -(high-low)/2;//prevents integer overflow
        //mid= (high+low)/2; //danger of integer overflow, use the long mid
        
        if (isBadVersion(mid)){//search in low
            answer=mid;
            high=mid-1;
            
        }else{//search in high
            low=mid+1;
        }
        
    }
    
    return answer;
    
}
