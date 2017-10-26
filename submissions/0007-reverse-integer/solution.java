class Solution {
   public int reverse(int x) {
		String s, t;
		s = Integer.toString(x);
		t = s;
		for (int i = 0; i < s.length(); i++) {
			t = t.substring(0, i) + s.charAt(s.length() - 1 - i) + t.substring(i + 1, t.length());
		}
		if (t.charAt(t.length() - 1) == '-') {
			t = "-" + t.substring(0, t.length() - 1);
		}
		long y;
		y = Long.parseLong(t);
		if (y >= Integer.MAX_VALUE || y <= Integer.MIN_VALUE) {
			return 0;
		} else {
			return Integer.parseInt(t);
		}
	}
}
