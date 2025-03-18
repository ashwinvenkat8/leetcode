import java.lang.Math;

class Solution {
    public int[] plusOne(int[] digits) {
        int[] result = null, tempResult = null, extendedResult = null;
        
        if (digits[digits.length-1]+1 > 9) {
            int carry = 1;
            tempResult = new int[digits.length];
            System.arraycopy(digits, 0, tempResult, 0, digits.length);
            for (int i = tempResult.length-1; i >= 0; --i) {
                tempResult[i] += 1*carry;
                if (tempResult[i] > 9) {
                    carry = (tempResult[i] / 10);
                    tempResult[i] = tempResult[i] % 10;
                }
                else
                    carry = 0;
            }
            if(carry == 1) {
                result = new int[tempResult.length + 1];
                result[0] += carry;
                System.arraycopy(tempResult, 0, result, 1, tempResult.length);
            }
            else {
                result = new int[tempResult.length];
                System.arraycopy(tempResult, 0, result, 0, tempResult.length);
            }
        }
        else {
            result = new int[digits.length];
            System.arraycopy(digits, 0, result, 0, digits.length);
            result[result.length-1] += 1;
        }
        
        return result;
    }
}