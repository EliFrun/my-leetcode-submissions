char* thousandSeparator(int n) {
    char* to_s = (char*) malloc(11 * sizeof(char));
    sprintf(to_s, "%d", n);
    int len = strlen(to_s);
    if (len <= 3) {
        return to_s;
    }

    int commas_needed = (len - 1) / 3;
    char* ret = (char*) malloc((len + commas_needed + 1) * sizeof(char));
    ret[len + commas_needed] = '\0';
    
    int i = len + commas_needed - 1;
    int j = len - 1;
    while(i >= 0 && j >= 0) {
        if ((len - 1 - j) % 3 == 0 && j != len - 1) {
            ret[i] = '.';
            i--;
        }
        ret[i] = to_s[j];
        j--;
        i--;
    }
    return ret;
}
