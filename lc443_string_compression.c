int compress(char* chars, int charsSize){

    char* s;
    s=chars;
    int i,j;
    i=0,j=0;
    int count=0;
    int len=0;
    int tlen=0;
    char tmp[5]={0};
    int truncated=0;
    while(i < charsSize){
        //printf("iteration:i=%d\n", i);
        while(chars[i] == s[j]){
            count++;
             j++;
            if (j==charsSize)break;
           
        }
        //printf("j=%d\n", j);
        //count chars are same, if count >1 compress
        if(count > 1){
            tlen=sprintf(tmp, "%d", count);
            chars[truncated]=chars[i];
            strncpy(&chars[truncated+1], tmp, tlen );
            truncated=truncated+1+tlen;
            len=len + tlen + 1;
        }else{
            len+=1;
            chars[truncated]=chars[i];
            truncated++;
        }
        
        //printf("%s:%d\n", chars, count);
        count=0;
        i=j;
    }
    return len;
}
