public class Solution {
	public String longestCommonPrefix(ArrayList<String> a) {
	    String myStr=new String();
		if(a.size()==0){
			return myStr;
		}
		if(a.size()==1){
			return a.get(0);
		}
		int minLen=Integer.MAX_VALUE;
		for(int i=0;i<a.size();i++){
			if(a.get(i).length()<minLen){
				minLen=a.get(i).length();
			}
		}
		for(int i=0;i<minLen;i++){
			for(int j=0;j<a.size()-1;j++){
				String s1=a.get(j);
				String s2=a.get(j+1);
				if(s1.charAt(i)!=s2.charAt(i)){
					return s1.substring(0,i);
				}
			}
		}
		return a.get(0).substring(0, minLen);
	}
}

