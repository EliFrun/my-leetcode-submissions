class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        ArrayList<List<Integer>> ret = new ArrayList<List<Integer>>();
        if(nums.length < 3){
            return ret;
        }
        Arrays.sort(nums);
        for(int i = 0; i < nums.length - 2; i++){
            int num1 = nums[i];
            while(i < nums.length - 3 && nums[i + 3] == num1){
                i++;
            }
            for(int j = i + 1; j < nums.length - 1; j++){
                int num2 = nums[j];
                while(j < nums.length - 2 && nums[j + 2] == num2){
                    j++;
                }
                int k = binarySearch(nums, j + 1, nums.length - 1,  - num1 - num2);
                if(k >= 0) {
                    int num3 = nums[k];
                    if (num3 == - num1 - num2){
                        boolean alreadyExists = false;
                        for(List<Integer> triple: ret){
                            if(triple.get(0) == num1 && triple.get(1) == num2 && triple.get(2) == num3){
                                alreadyExists = true;
                                break;
                            }
                        }
                        if(!alreadyExists){
                            ret.add(new ArrayList<Integer>(){{
                                add(num1);
                                add(num2);
                                add(num3);
                            }});       
                        }
                    }
                }
            }
        }
        return ret;
    }
    
    public static int binarySearch(int[] ls, int first, int last, int target){
        int ret = -1;
        int middle = (first + last) / 2;
        while(ls[first] <= target && target <= ls[last]){
            if(ls[first] == target){
                ret = first;
                break;
            }
            if(ls[last] == target){
                ret = last;
                break;
            }
            if(last - first == 1){
                break;
            }
            middle = (first + last) / 2;
            if(target <= ls[middle]){
                last = middle;
            } else {
                first = middle;
            }
        }
        return ret;
    }
}
