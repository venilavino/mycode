import java.io.*;
import java.util.*;
class string_compare
{
public static void main(String[] args)
{
String str1,str2;
Scanner s=new Scanner(System.in);
System.out.print("string1 And ");
str1=s.nextLine();
System.out.print("string2 ");
str2=s.nextLine();
if(str1.equals(str2))
{
System.out.println("Both are equal");
}
else
{
System.out.println("Both are not equal");
}
}
}
