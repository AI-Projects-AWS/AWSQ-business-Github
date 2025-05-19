import java.util.*;

/**
 * Solution for the 3Sum problem.
 * 
 * Given an array of integers, find all unique triplets in the array
 * which gives the sum of zero.
 */
public class three_sum {
    
    /**
     * Finds all unique triplets in the array which sum to zero.
     * 
     * @param nums The input array of integers
     * @return A list of lists, where each inner list contains three integers that sum to zero
     */
    public static List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        
        // Edge case: if array is null or has less than 3 elements
        if (nums == null || nums.length < 3) {
            return result;
        }
        
        // Sort the array to handle duplicates and use two pointers approach
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length - 2; i++) {
            // Skip duplicates for the first element of the triplet
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            int target = -nums[i];
            int left = i + 1;
            int right = nums.length - 1;
            
            while (left < right) {
                int sum = nums[left] + nums[right];
                
                if (sum == target) {
                    // Found a triplet
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    
                    // Skip duplicates for the second element
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    
                    // Skip duplicates for the third element
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    
                    // Move both pointers
                    left++;
                    right--;
                } else if (sum < target) {
                    // Need a larger sum, move left pointer
                    left++;
                } else {
                    // Need a smaller sum, move right pointer
                    right--;
                }
            }
        }
        
        return result;
    }
    
    /**
     * Main method for testing the threeSum function.
     */
    public static void main(String[] args) {
        // Example 1
        int[] nums1 = {-1, 0, 1, 2, -1, -4};
        System.out.println("Example 1 Input: " + Arrays.toString(nums1));
        System.out.println("Output: " + threeSum(nums1));
        
        // Example 2
        int[] nums2 = {0, 0, 0};
        System.out.println("\nExample 2 Input: " + Arrays.toString(nums2));
        System.out.println("Output: " + threeSum(nums2));
        
        // Example 3
        int[] nums3 = {-2, 0, 1, 1, 2};
        System.out.println("\nExample 3 Input: " + Arrays.toString(nums3));
        System.out.println("Output: " + threeSum(nums3));
    }
}