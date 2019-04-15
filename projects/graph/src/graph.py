"""
Simple graph implementation
"""


class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, name):
        if not name in self.vertices:
            self.vertices[name] = set()
    def add_directed_edge(self,v1, v2):
        try:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        except:
            return "Missing a vertex"
    def breadth_first_traversal(self, start_node):
        queue = [start_node]
        result = []
        visited = {}
        current_vertex = None

        while len(queue) > 0: 
            current_vertex = queue.pop(0)
            result.append(current_vertex)
            for vertice in self.vertices[current_vertex]:
                if not vertice in visited:
                    visited[vertice] = True
                    queue.append(vertice) 
        return result
    def depth_first_traversal_recursively(self, start_node, result = []):
        result += start_node
        for neighbor in self.vertices[start_node]:
            if neighbor not in result:
                result = self.depth_first_traversal_recursively(neighbor, result)
        return result
    def depth_first_traversal_stack(self, start_node):
        stack = [start_node]
        result = []
        visited = {}
        visited[start_node] = True
        while len(stack) >0:
            current_vertex = stack.pop()
            result.append(current_vertex)
            for vertice in self.vertices[current_vertex]:
                if not vertice in visited:
                    visited[vertice] = True
                    stack.append(vertice)
        return result
    def breadth_first_search(self, start_node, destination_node):
        current_node = start_node
        queue = [[start_node]]
        path = []
        visited = {}
        while current_node != destination_node:
            current_node = queue.pop(0)
            path.append(current_node)
            for vertice in self.vertices[current_node]:
                if not vertice in visited:
                    visited[vertice] = True
                    queue.append(vertice) 
        

graph = Graph()  # Instantiate your graph
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_directed_edge('5', '3')
graph.add_directed_edge('6', '3')
graph.add_directed_edge('7', '1')
graph.add_directed_edge('4', '7')
graph.add_directed_edge('1', '2')
graph.add_directed_edge('7', '6')
graph.add_directed_edge('2', '4')
graph.add_directed_edge('3', '5')
graph.add_directed_edge('2', '3')
graph.add_directed_edge('4', '6')
print(graph.breadth_first_search('1','2'))