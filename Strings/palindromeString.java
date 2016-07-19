public class Solution {
	public int isPalindrome(String a) {
		a=a.toLowerCase();
		a=a.replaceAll("[^A-Za-z0-9]", "");
		//System.out.println(a);
//		StringBuilder s=new StringBuilder(a);
		//int length=s.length();
		int left=0;
		int right=a.length()-1;
		while(left<=right){
			if(a.charAt(left)!=a.charAt(right)){
				return 0;
			}
			left++;
			right--;
		}
		
	
		return 1;
	}
}

