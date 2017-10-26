class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int te=nums1.length+nums2.length;//te = total entries
         int[] x = new int[te];
         //MERGE SORT IMPLEMENTATION
            int cc = 0;// array c counter
			int dc = 0;// array d counter
			for (int i = 0; i < te; i++) {
				if (cc < nums1.length && dc < nums2.length) {
					if (nums1[cc] < nums2[dc]) {
						x[i] = nums1[cc];
						cc++;
					} else {
						x[i] = nums2[dc];
						dc++;
					}
				} else if (cc < nums1.length && dc == nums2.length) {
					x[i] = nums1[cc];
					cc++;
				} else if (dc < nums2.length && cc == nums1.length) {
					x[i] = nums2[dc];
                    dc++;
				}
        }
        if(te%2==0)//even number entries implies final median will be the average of 2 median values
        {
            return (double)(((double) x[te/2]+x[te/2-1])/2);
           
    }
        else{
            return x[te/2];
        }
}
}
