//watch out for the class name
public class Solution {
	public int firstMissingPositive(ArrayList<Integer> a) {
	   
				int length=a.size();
		int right=length-1;
		int left=0;
		if(a.size()==1){
			if(a.get(0)<=0){
				return 1;
			}
			else if(a.get(0)>1){
				return 1;
			}
			else return 2;
		}
		int count=0;
		while(left<right){
			if(a.get(left)<=0 && a.get(right)<=0){
			right--;
			}
			
			else if(a.get(left)<=0 && a.get(right)>0){
				int temp1=a.get(left);
				int temp2=a.get(right);
				a.set(left, temp2);
				a.set(right, temp1);
				right--;
				left++;
			}
			else if(a.get(left)>0 && a.get(right)<=0){
				left++;
			}
			else if(a.get(left)>0 && a.get(right)>0){
				left++;
			}
			
			
		}
		//System.out.println();
		/*for(int i=0;i<a.size();i++){
			System.out.print(a.get(i)+" ");
		}
		System.out.println(left+" "+right);
*/
		if(right==left && left==0){
			return 1;
		}
		//if(left==a.size()-1) left+=1;
		left+=1;
		for(int i=0;i<left;i++){
			int index=0;
			index=Math.abs(a.get(i))-1;
			if(index<left){
			//	System.out.println(index);
				if(a.get(index)>0){
					a.set(index, (-1*a.get(index)));
				}
			}
		}
		//int i=0
		for(int i=0;i<left;i++){
			if(a.get(i)>0) return i+1;
		}
		//if(i==left) return
		
		return left+1;

	}
}

