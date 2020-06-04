/**
 * Note: The returned array must be malloced, assume caller calls free().
 

 */
int compare(int16_t alphabetS[],int16_t alphabet[]){
    int i=0;
    int64_t *p1=alphabetS;
    int64_t *p2= alphabet;
    /*
    printf("alphabet[]=");
    for (i=0; i<26; i++){
        printf("%d ", alphabet[i]);
    }
    printf("\nalphabetS[]=");
    for (i=0; i<26; i++){
        printf("%d ", alphabetS[i]);
    }
    */
    for (i=0; i<6; i++){
        if( p1[i] == p2[i] ){
            continue;
        }else{
            break;
        }
    }
    if (i==6) return 1;
    return 0;
    
}
int* findAnagrams(char * s, char * p, int* returnSize){
    int16_t alphabet[26]={0}; //to store num_occurances of chars(a-z) in p
    int16_t alphabetS[26]={0};//to store the num occurances of chars in the current processing substring of s
    int i=0; 
    int plen=strlen(p);
    int slen=strlen(s);
           
    
    *returnSize=0;
    int* indices = malloc(20101 * sizeof(int));//Max anagrams could be of strlen(s)
    memset(indices, 0, 20101*sizeof(int));
    
    if(slen >20100 || plen > 20100){//s and p are out of given input size restriction
        return indices;
    }
    if(slen < plen){//s is smaller than p, no anagram
        return indices;
    }
    
    for(i=0; i<plen; i++){
        alphabet[p[i]-'a']++;//store the number of occurence of char present in p
    }
    
    for(i=0; i<plen; i++){
        alphabetS[s[i]-'a']++;//store the number of occurence of char present in first plen char of s
    }
    i=0;
    int prev_comp=0;
    if((prev_comp=compare(alphabetS,alphabet)) ==1){
            indices[*returnSize]=i;
            *returnSize+=1;
    }
    //iterate over each char of string s
    for (i=1; i <= slen-plen; i++){
        
        alphabetS[s[i-1]-'a']--;
        alphabetS[s[i+plen-1]-'a']++;
        //if char-in and char-out are same skip compare, otherwise call compare() which is O(26)
        //compare the two hashed alphabet-set, one from p other from currently under processing s (of len p); 
        //if match we found one index store it.
        if((prev_comp && (s[i-1] == s[i+plen-1])) || compare(alphabetS,alphabet) ==1){
            indices[*returnSize]=i;
            *returnSize+=1;
            prev_comp=1;
        }else{
            prev_comp=0;
        }
    }
    printf("%d, ", *returnSize);
    
    return indices;
}
