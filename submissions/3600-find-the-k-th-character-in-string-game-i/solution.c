char kthCharacter(int k) {
   char* word = malloc(sizeof(char));
   int len = 1;
   word[0] = 'a';

    while (len < k) {
        char* next_word = malloc(2 * len * sizeof(char));
        for(int i = 0; i < len; i++){
            next_word[i] = word[i];
            next_word[len + i] = word[i] + 1 ;
        }


        free(word);
        word = next_word;
        len *= 2;
    }
   return word[k-1]; 
}

  
