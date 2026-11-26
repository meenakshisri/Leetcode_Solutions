class Solution {

    public static void DFS(int node, int[][] isConnected, boolean[] visited)
    {
        visited[node]=true;

        for(int nbr = 0; nbr<isConnected.length; nbr++)
        {
            if(isConnected[node][nbr] == 1 && !visited[nbr])
            {
                DFS(nbr, isConnected, visited);
            }
        }
       
    }

    public int findCircleNum(int[][] isConnected) {
        
        int n = isConnected.length;

        boolean[] visited = new boolean[n];

        int provinces = 0;

        for(int i = 0; i<n; i++)
        {
            if(!visited[i])
            {
                provinces++;
                DFS(i, isConnected, visited);
            }
        }
    return provinces;

    }
}