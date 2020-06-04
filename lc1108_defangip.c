char * defangIPaddr(char * address){
    char* defang;
    defang=malloc(strlen(address)+1+6);
    int i=0;
    int j=0;
    for(i=0; i<strlen(address); i++){
        if(address[i] == '.'){
            defang[j++]='[';
            defang[j++]='.';
            defang[j++]=']';
        }else{
            defang[j++]=address[i];
        }
    }
    defang[j]='\0';
    return defang;
}
