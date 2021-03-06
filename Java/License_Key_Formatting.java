class Solution {
    public String licenseKeyFormatting(String S, int K) {
        // Replacing all - and converting all letters to uppercase
        String S1 = S.replace("-","");
        S1 = S1.toUpperCase();

        // Making stringBuilder
        StringBuilder sb = new StringBuilder();
        sb.append(S1);
        
        int len = sb.toString().length();
        // Inserting '-' from back at every K position
        for(int i=K; i < len; i=i+K) {
                sb.insert(len-i,'-');
            }
        return sb.toString();

    }
}
