package com.leetcode;

public class RemoveElement {

    public int removeElement(int[] nums, int val) {
        int j = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val ) {
                if (nums[j] == val) {
                    nums[j] = nums[i];
                    nums[i] = val;
                }
                j += 1;
            }
        }
        return j;
    }

}
