class primes_less2000000{
	static List primeList = new ArrayList();
	static {
		primesList.add(2);
		primesList.add(3);
	}
	static boolean[] numbers = new boolean[2000001];
	
	public static void main(String[] args){
		int var = getNext();
		while (var<primes.length){
			if (isPrime(var)){
				primesList.add(var);
				markAll(var);
			}
		}
		
	}
	
	static void markAll(int delta){
		for (int x = delta; i < 2000001; i+=delta){
			numbers[x] = true;
		}
	}
	
	static int getNext(){
		primesList.get(primesList.size()-1)+2;
	}
}