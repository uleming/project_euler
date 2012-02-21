import java.util.*;
class problem29{
	public static void main(String[] args){
		Set<Long> set = new HashSet<Long>();
		for (int a=2; a<=100;a++){
			for(int b= 2; b<=100;b++){
				long value = Math.pow(a,b);
				set.add(value);
				}
			}
		}
		System.out.println(set.size());
	}