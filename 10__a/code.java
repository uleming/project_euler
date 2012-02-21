
import java.util.*;
class code{
    private static int RANGE = 2 000 000;
    private static List<Integer> primes = new LinkedList<Integer>();
    private static int[] data = new int[2000000];

    public static void main(String[] args) {
        int prime = 2;
        while(true){
            if(isPrimeNumber(prime)){
                primes.add(prime);
                markOccurences(prime);
                getNextPrime(prime);
            }
        }
    }

    private static void markOccurences(int multiplier){
        for(int c = multiplier; c < 2 000 000; c+=multiplier ){
            data[c] = 1;
            }
    }
    private static boolean isPrimeNumber(int number){

    }

    private static int getNextPrime(prime){
        while(data[prime=+2]==0)

    }
}

