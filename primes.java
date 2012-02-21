import java.util.*;
class primes{
	
	static List<Integer> primes = new ArrayList<Integer>();
	static int current = 3;
	static {
		primes.add(2);
		primes.add(3);
	}
	public static void main(String[] args){
		while(primes.size()<10001){
			int var = getNext();
			if (isPrime(var)){
				primes.add(var);
			}
		}
		System.out.println(primes+"\n Length of array: " + primes.size());
	}
	
	static int getNext(){
		return current = current + 2;
	}
	
	static boolean isPrime(int num){
		for (Integer value: primes){
			if (num%value == 0){
				return false;
			}
		}
		return true;
	}
}