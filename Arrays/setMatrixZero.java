//watch out for the class name
public class Solution {
	public void setZeroes(ArrayList<ArrayList<Integer>> A) {
	    int[] rows = new int[A.size()];
        int[] columns = new int[A.get(0).size()];
        for(int i = 0; i < A.size(); i++){
            for(int j = 0; j < A.get(i).size(); j++){
                if(A.get(i).get(j) == 0){
                    rows[i] = 1;
                    columns[j] = 1;
                }
            }
        }
        
        for(int i = 0; i < A.size(); i++){
            for(int j = 0; j < A.get(i).size(); j++){
                if(rows[i] == 1 ||columns[j] == 1){
                    A.get(i).set(j, 0);
                }
            }
        }
	}
}

