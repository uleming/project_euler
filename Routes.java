class Routes{
	private static int len = 21;
	private static long[][] map = new long[len][len];
	private static long weight = 1;
	
	public static void main(String[] args){
		fillMap();
		System.out.println(map[len-1][len-1]);
	}
	
	private static void fillMap(){
		fillEdges();
		for (int y = 1;y<len;y++){
		//	System.out.println();
			for (int x = 1;x<len;x++){
				map[x][y] = map [x-1][y] + map [x][y-1];
			//	System.out.print(map[x][y]+"   ");
			}
		}
	}
	
	private static void fillEdges(){
		for (int a = 0; a<len; a++){
			map[a][0] = weight;
			map[0][a] = weight;
		}
	}
}
