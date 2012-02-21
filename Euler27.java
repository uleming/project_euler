class Euler27 
{
	public static boolean isPrime( long number )
	{
		if( number < 2 )
		{
			return false;
		}
		else if ( number == 2 )
		{
			return true;
		}
		else
		{
			for( long i=2; i<=Math.sqrt(number); i++ )
			{
				if( number%i == 0 )
				{
					return false;
				}
			}
		}
 
		return true;
	}
 
	public static void main(String[] args) 
	{
		int result = 0;		
		int max = 0;
 
		for( int a=-999; a<=999; a++ )
		{
			for( int b=-999; b<=999; b++ )
			{
				int n = 0;
				int number = 0;
 
				while(true)
				{
					number = n*n + a*n + b;
 
					if( !isPrime(number) )
					{
						break;
					}
 
					n++;
				}
 
				if( n > max )
				{
					max = n;
					result = a * b;
				}
			}
		}
 
		System.out.println( result );
	}
}