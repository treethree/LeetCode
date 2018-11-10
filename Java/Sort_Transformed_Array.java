// Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.
//
// The returned array must be in sorted order.
//
// Example
// Given nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5, return [3, 9, 15, 33]
// Given nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5, return [-23, -5, 1, 7]
//
// Notice
// Expected time complexity: O(n)

// If a >=0, the minimum value is at the array's vertex. So we need to move the two end pointers toward the vertex and output from right to left.
// If a <0, the maximum value is at the array's vertex. So we need to move the two end pointers toward the vertex but output from left to right.

public class Solution {
    public int[] sortTransformedArray(int[] nums, int a, int b, int c) {
        // Write your code here
        int[] res = new int[nums.length];
        int start = 0;
        int end = nums.length - 1;
        int i = a >= 0 ? nums.length - 1 : 0;
        while(start <= end) {
            int startNum = getNum(nums[start], a, b, c);
            int endNum = getNum(nums[end], a, b, c);
            if(a >= 0) {
                if(startNum >= endNum) {
                    res[i--] = startNum;
                    start++;
                }
                else{
                    res[i--] = endNum;
                    end--;
                }
            }
            else{
                if(startNum <= endNum) {
                    res[i++] = startNum;
                    start++;
                }
                else{
                    res[i++] = endNum;
                    end--;
                }
            }
        }
        return res;
    }
    public int getNum(int x, int a, int b, int c) {
        return a * x * x + b * x + c;
    }
}
