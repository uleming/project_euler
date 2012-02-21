import java.util.*;
class PrimesSumm{
	private static final int len = 2000000;
	private static final boolean[] range = new boolean[len];
	private static final List<Integer> primes = new ArrayList<Integer>();
	private static int currentPrime = 0;
	
	public static void run(){
		initialize();
		while(currentPrime < len){
			currentPrime = getNextPrime();
			primes.add(currentPrime);
			erase(currentPrime);
		}
	}
	
	private static void initialize(){
		primes.add(2);
		erase(2);
		primes.add(3);
		erase(3);
		currentPrime = 3;
	}
	
	private static void erase(int var){
		for (int i = var; i<len; i+=var){
			range[i] = true;
		}
	}
	
	private static int getNextPrime(){
		boolean var = range[currentPrime];
		while( (currentPrime+=2) < len ) {
			if (!range[currentPrime]) {
				return currentPrime;
			}
		}
		return currentPrime;
	}
	
	public static List<Integer> getList(){
		return primes;
	}
}









class runner{
	public static void main(String[] args){
		long summ = 0;
		PrimesSumm.run();
		List<Integer> list = PrimesSumm.getList();
		for(Integer var: list){
			summ+=var;
		}
		System.out.println("Summ is:  " + summ);
		
	}
}