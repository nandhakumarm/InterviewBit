public class Solution {
	// DO NOT MODIFY THE LIST
	public int repeatedNumber(final List<Integer> a) {
	    int[] count = new int[a.size()];
        for(int i = 0; i < a.size(); i++){
            if(count[a.get(i)] == 1)
                return a.get(i);
            else
                count[a.get(i)] = 1;                      
        }
        return 0;
	}
}

