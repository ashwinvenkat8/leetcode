class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [0] * n
        
        def is_cycle(idx: int):
            if visited[idx] == 2:
                return False
            if visited[idx] == 1:
                return True
            
            visited[idx] = 1

            for neighbor in graph[idx]:
                if is_cycle(neighbor):
                    return True
            
            visited[idx] = 2
            return False
        
        safe_nodes = []
        for node in range(len(graph)):
            if not is_cycle(node):
                safe_nodes.append(node)

        return safe_nodes
