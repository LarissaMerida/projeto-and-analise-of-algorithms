#include <bits/stdc++.h> 
using namespace std; 
#define MAX 100 
#define INF 1e9 int adjMatrix[MAX][MAX], max_flow, flow, src, sink; 
vector<int> parent, adjList[MAX]; 

void augment(int v, int minEdge) 
{     
	if(v == src) 
	{
	   flow = minEdge; 
	   return;
	 }    
	 else if(parent[v] != -1)
	 {         
	 	augment(parent[v], min(minEdge, adjMatrix[parent[v]][v]));         
	 	adjMatrix[parent[v]][v] -= flow;         
	 	adjMatrix[v][parent[v]] += flow;     
	 }
} 

int maxflow()
{     
	max_flow = 0;     
	while(1)
	{         
		flow = 0;         
		bitset<MAX> vis; 
		vis[src] = true;         
		queue<int>q; q.push(src);         
		parent.assign(MAX, -1);         
		while(!q.empty())
		{

			int u = q.front(); q.pop();             
			if(u == sink) 
				break;             
			for(int j = 0; j<adjList[u].size(); j++)
			{                 
				int v = adjList[u][j];                 
				if(adjMatrix[u][v] > 0 && !vis[v])
				{                     
					vis[v] = true, q.push(v), parent[v] = u;                 
				}             
			}         
		}         
		augment(sink, INF);         
		if(flow == 0)break;         
		max_flow+=flow;     
	}     
	return max_flow; 
}  
int main()
{     //ios_base::sync_with_stdio(0);    
	 int n, m;     
	 scanf("%d %d", &n, &m);     
	 memset(adjMatrix, 0, sizeof adjMatrix);     
	 for(int i = 0; i < m; i++)
	 {        
	 	int u, v, w;         
	 	scanf("%d %d %d", &u, &v, &w);         
	 	adjList[u].push_back(v);         
	 	adjList[v].push_back(u);         
	 	adjMatrix[u][v] = w; // fluxo entre esses dois vertices     
	 }     
	 src = 0; // inicio     sink = 1; // destino     
	 printf("%d\n", maxflow()); 
}  /* entrada pra o grafo do video 5 7 0 2 100 0 3 50 2 3 50 2 4 50 2 1 50 3 4 100 4 1 125 */