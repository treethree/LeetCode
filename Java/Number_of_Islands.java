//package Java; //Add this to run in your atom script terminal

class Number_of_Islands {
    private int row,col;
    public int numIslands(char[][] grid) {
         int res = 0;
         row = grid.length;
        if(row == 0) return 0;
         col = grid[0].length;
        for(int i=0; i<row; i++)
        {
            for(int j=0; j<col; j++)
            {
                if(grid[i][j] == '1')
                {
                    dfs(grid, i, j);
                    res++;
                }
            }
        }
        return res;
    }
    public void dfs(char[][] grid, int a, int b)
    {
        if(a < 0 || b < 0 || a >= row || b >= col || grid[a][b] != '1') return;
        grid[a][b] = '0';
        dfs(grid, a,b+1);
        dfs(grid, a,b-1);
        dfs(grid, a+1,b);
        dfs(grid, a-1,b);
    }
}
