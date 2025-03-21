class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        if (mat == null || mat.length == 0) {
            return new int[0];
        }
        
        int N = mat.length;
        int M = mat[0].length;
        
        int[] result = new int[N*M];
        int k = 0;
        ArrayList<Integer> intermediate = new ArrayList<Integer>();
        
        for (int d = 0; d < N + M - 1; d++) {
            
            intermediate.clear();
            
            int r = d < M ? 0 : d - M + 1;
            int c = d < M ? d : M - 1;
            
            while (r < N && c > -1) {
                
                intermediate.add(mat[r][c]);
                ++r;
                --c;
            }
                
            if (d % 2 == 0) {
                Collections.reverse(intermediate);
            }
            
            for (int i = 0; i < intermediate.size(); i++) {
                result[k++] = intermediate.get(i);
            }
        }
        
        return result;
    }
}