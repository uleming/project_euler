import java.lang.*;
import java.io.*;

class BinaryToDecimal{
  public static void main(String[] args) throws IOException{
    BufferedReader bf= new BufferedReader(new InputStreamReader(System.in));
    System.out.print("Enter the Binary value: ");
    String str = bf.readLine();
    long num = Long.parseLong(str);
    long rem;
    while(num > 0){
      rem = num % 10;
      num = num / 10;
      if(rem != 0 && rem != 1){
        System.out.println("This is not a binary number.");
        System.out.println("Please try once again.");
        System.exit(0);
      }
    }
    int i= Integer.parseInt(str,2);
    System.out.println("Decimal:="+ i);
  }
}