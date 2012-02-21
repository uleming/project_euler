import java.util.*;
class problem29{
	public static void main(String[] args){
		Set<Double> set = new HashSet<Double>();
		for (long a=2; a<=100;a++){
			for(long b= 2; b<=100;b++){
				double value = Math.pow(a,b);
				set.add(value);
				}
			}
			System.out.println(set.size());
		}
	}
