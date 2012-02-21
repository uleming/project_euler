import java.util.*;
class Test{
	public static void main(String[] args){
		List<Integer> list = new ArrayList<Integer>();
		list.add(12);
		list.add(1);
		list.add(45);
		for(Integer i:list)
			System.out.println(i);
	}
}