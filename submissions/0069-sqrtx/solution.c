int mySqrt(int x) {
    if (x <= 1) {
        return x;
    }
    double prev, curr = x;
    double next;
    for (int _ = 0; _ < 20; _++) {
        next = (1.0/2) * (curr + x / curr);
        prev = curr;
        curr = next;
    }
    return curr;
}
