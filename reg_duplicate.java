import java.util.HashSet;
import java.util.Set;
class DuplicateInArray 
{
    public static void main(String[] args) 
    {
        int[] array = {2017121,2017122,2017123,2017124,2017124,2017125,2017126};
         
        Set<Integer> set = new HashSet<Integer>();
         
        for(int i = 0; i < array.length ; i++) 
        {
          
            if(set.add(array[i]) == false) 
            {
                System.out.println("Duplicate element found : " + array[i]);
            }
        }
    }
}
