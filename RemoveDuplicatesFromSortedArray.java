package com.leetcode;

public class RemoveDuplicatesFromSortedArray {

    public int removeDuplicates(int[] nums) {
        int j = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[j]) {
                j++;
                if (j != i) {
                    nums[j] = nums[i];
                }
            }
        }
        return ++j;
    }

}