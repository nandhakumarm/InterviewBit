//change the class name to flip to execute on local machine
//class name should be "Solution" for submitting on interviewbit
public class Solution {
    public ArrayList<Integer> flip(String A) {
        ArrayList<Integer> tempList=new ArrayList<Integer>();
		boolean hasZero=false;
        int str_length=A.length();
		int[] input=new int[str_length];
		for(int i=0;i<str_length;i++){
			input[i]=Integer.parseInt(String.valueOf(A.charAt(i)));
			
		if(input[i]==0){
				hasZero=true;
			}
		}
		if(!hasZero){
			return tempList;
		}
		

		int maxDiff = 0;
		int flipStartIndex = 0;
		int flipEndIndex = 0;
		int onesToFlip = 0;
		int totalNumberOfOnes = 0;

		int currentDiff = 0;
		int currentStart = 0;
		int currentOnesToFlip = 0;

		for (int i = 0; i < input.length; i++) {
		    if (input[i] == 0) {
				currentDiff -= 1;
		    } else {
				currentDiff += 1;
				currentOnesToFlip++;
				totalNumberOfOnes++;
		    }
		    if (currentDiff < maxDiff) {
				maxDiff = currentDiff;
				flipStartIndex = currentStart;
				flipEndIndex = i;
				onesToFlip = currentOnesToFlip;
		    } else if (currentDiff > 0) {
				currentDiff = 0;
				currentStart = i + 1;
				currentOnesToFlip = 0;
		    }
		}
		//System.out.println(flipEndIndex +" "+ flipStartIndex + " "+ onesToFlip +   totalNumberOfOnes +" "+ onesToFlip);
	//ArrayList<Integer> tempList=new ArrayList<Integer>();
	tempList.add(flipStartIndex+1);
	tempList.add(flipEndIndex+1);
	return tempList;
    }
}

