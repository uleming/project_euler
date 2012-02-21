import java.util.*;
class a26{
	public static void main(String[] args){
		Integer rest = 1;
		int max = 0;
		int maxValue = 0;
		for (int x = 2;x<1000;x++){
			Set<Integer> set = new HashSet<Integer>();
			set.add(1);
			int n = 0;
			rest = 1;
			while (true){
				while (rest < x){
					rest = rest * 10;
					}
				rest = rest%x;
				if (rest == 0 || set.contains(rest)){
					if (max < n){
						max = n;
						maxValue = x;
						}
					break;
					}
				set.add(rest);
				n = n +1;
				}
			}
	
		System.out.println(maxValue);
	}
}
