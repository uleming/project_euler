class maxnum{
    static long value = 600851475143l;
    public static void main(String[] args) {
        long var;
        for (var = 3; var < value; var +=2){
            if (value % var == 0){
                System.out.println(var);
                value = value / var;
            }
        }
        System.out.println(value);
    }
}
