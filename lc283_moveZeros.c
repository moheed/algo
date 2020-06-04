void moveZeroes(int* nums, int numsSize){
    int i=0;
    int j=0;
    for (i=0; i<numsSize; i++){
        if (nums[i]!=0) continue;
        //found first zero element       
        for (j=i+1; j< numsSize;j++){
            if( nums[j]==0) continue; //non-zero element followed by zeros.
            nums[i++]= nums[j];
            nums[j]=0;
        }
        break;
    }
}
