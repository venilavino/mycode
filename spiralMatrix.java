class MatrixSpiral {
    public static void main(String[] args)
    {
        int [][]matrix = {
                {1,2,3,4},
                {5,6,7,8},
                {9,10,11,12},
                {13,14,15,16}
        };
        printSpiral(matrix);
    }
    public static void printSpiral(int[][] matrix)
    {
        int top = 0;
        int bottom = matrix.length-1; 
        int left = 0;
        int right = matrix[0].length-1;

        int direction = 0;

        while ( top <= bottom && left <= right )
        {
            int i = 0;
            if( direction == 0 )
            {
                for( i = left; i <= right; i++ )
                {
                    System.out.print( matrix[top][i]+ " " );
                }
                top++;
                direction = 1;
            }
            else if( direction == 1 ) 
            {
                for( i = top; i <= bottom; i++ )
                {
                    System.out.print( matrix[i][right] + " " );
                }
                right--;
                direction = 2;
            }
            else if( direction == 2 )
            {
                for( i = right; i >= left; i-- )
                {
                    System.out.print(matrix[bottom][i] + " ");
                }
                bottom--;
                direction = 3;
            }
            else
            {
                for( i = bottom; i >= top; i-- )
                {
                    System.out.print( matrix[i][left] + " " );
                }
                left++;
                direction = 0;
            }
        }
    }
}
