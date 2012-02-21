class A{
	public String s = "hello";
	
	public String getWord(){return s;}
}

class B extends A{
	public String s = "world";
	public String getWord(){return s;}
	
	static public void main(String[] args){
		A a = new B();
		System.out.println("Class A: " + a.s + " class B: "+ a.getWord());
	}
}