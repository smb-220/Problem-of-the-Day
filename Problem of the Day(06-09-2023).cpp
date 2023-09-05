//Mother Vertex
class Solution 
{
    public:
	void dfs(int u, vector<int>adj[], vector<bool>&vis)
	{
		vis[u] = true;
		
		for(auto v: adj[u])
		{
			if(!vis[v])
				dfs(v, adj, vis);
		}
	}
	
	int findMotherVertex(int V, vector<int>adj[])
	{
		vector<bool>vis(V, false);
		int v;
		for(int i = 0; i < V; i++)
		{
			if(!vis[i]){
				dfs(i, adj, vis);
				v = i;
			}
		}
		vis.assign(V, false);
		dfs(v, adj, vis);
	
		for(auto i: vis)
			if(!i)
				return -1;			
		return v;
	}
};
