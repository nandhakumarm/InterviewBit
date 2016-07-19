//change the class name to largestNumber to execute on local machine
//class name should be "Solution" for submitting on interviewbit
public class Solution {
	// DO NOT MODIFY THE LIST
	public String largestNumber(final List<Integer> a) {
	    String[] strs = new String[a.size()];
    for(int i=0; i<a.size(); i++){
        strs[i] = String.valueOf(a.get(i));
    }
 
    Arrays.sort(strs, new Comparator<String>(){
        public int compare(String s1, String s2){
            String leftRight = s1+s2;
            String rightLeft = s2+s1;
            return -leftRight.compareTo(rightLeft);
 
        }
    });
 
    StringBuilder sb = new StringBuilder();
    for(String s: strs){
        sb.append(s);
    }
 
    while(sb.charAt(0)=='0' && sb.length()>1){
        sb.deleteCharAt(0);
    }
 
    return sb.toString();
	}
}

