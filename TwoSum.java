package com.leetcode;


import org.omg.PortableInterceptor.INACTIVE;

import java.util.*;

/**
 * Question no. 1
 */
public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        /**
         * O(n^2)
         */
//        int len = nums.length;
//        for (int i = 0; i < len; i++) {
//            int reqVal = target - nums[i];
//            for (int j = i+1; j < len; j++) {
//                if (nums[j] == reqVal) {
//                    return new int[] {i,j};
//                }
//            }
//        }


        /**
         * The below code heavy
         */
        Map<Integer, Integer> dict = new HashMap<>();
        int[] result = new int[2];
        for (int i = 0; i < nums.length; i++) {
            if (dict.containsKey(target - nums[i])) {
                result[0] = dict.get(target - nums[i]);
                result[1] = i;
            } else {
                dict.put(nums[i], i);
            }
        }

        return result;
    }
}
