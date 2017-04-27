import java.util.*;
class string_reverse {
    public static void main(String[] args) {
        System.out.println("Enter The String");
        Scanner out=new Scanner(System.in);
        String rev=out.nextLine();
        char revout[]= rev.toCharArray();
        System.out.println("the reversed string:");
        for(int j=revout.length-1;j>=0;j--){
            System.out.print(revout[j]);
            
        }
        
    }

    }
