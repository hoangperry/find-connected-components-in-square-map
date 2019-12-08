import random


class GraphAdjMatrix:
    def __init__(self):
        self.adj_mat = None

    def add_vertex(self, name):
        if self.adj_mat is None:
            self.adj_mat = {
                name: {
                    name: 0
                }
            }
            return
        self.adj_mat[name] = dict()
        for key in self.adj_mat:
            self.adj_mat[name][key] = 0
            self.adj_mat[key][name] = 0

    def print_adj_mat(self):
        if self.adj_mat is None:
            return
        for key in self.adj_mat:
            for _key in self.adj_mat[key]:
                print(self.adj_mat[key][_key], end=" ")
            print()

    def add_edge(self, source_vertex, destination_vertex):
        self.adj_mat[source_vertex][destination_vertex] = 1
        self.adj_mat[destination_vertex][source_vertex] = 1
        return

    def dfs_recursive(self, v, visited=None):
        if visited is None:
            visited = list()
        if self.adj_mat is None:
            return list()
        visited.append(v)
        for key in self.adj_mat[v]:
            if self.adj_mat[v][key] == 1 and key not in visited:
                visited = self.dfs_recursive(key, visited)
        return visited

    # def bfs_recursive(self, v, visited=None):
    #     if visited is None:
    #         visited = list()
    #         visited.append(v)
    #     if self.adj_mat is None:
    #         return list()
    #     for key in self.adj_mat[v]:
    #         if self.adj_mat[v][key] == 1:
    #             visited.append(v)
    #             visited = self.bfs_recursive(key, visited)
    #     return visited

    def bfs_non_recurisve(self, v):
        visited = [v]
        queue = [v]
        while not queue.__len__() == 0:
            v = queue[0]
            queue = queue[1:]
            for key in self.adj_mat[v]:
                if self.adj_mat[v][key] == 1 and key not in visited:
                    print(key)
                    visited.append(key)
                    queue.append(key)
        return visited

    def dfs_non_recursive(self, v):
        visited = list()
        stack = [v]
        while stack:
            key = stack.pop()
            if key in visited:
                continue
            visited.append(key)
            for i in self.adj_mat[key]:
                if self.adj_mat[key][i] == 1:
                    stack.append(i)
        return visited

    def update_graph(self, mat):
        self.adj_mat = None
        list_v = list()
        for i in range(mat.__len__()):
            for j in range(mat[i].__len__()):
                if mat[i][j] == 1:
                    name_v = "{}_{}".format(j, i)
                    self.add_vertex(name_v)
                    list_v.append(name_v)

        for i in range(list_v.__len__()):
            for j in range(i + 1, list_v.__len__()):
                kaa_1 = [int(x) for x in list_v[i].split("_")]
                kaa_2 = [int(x) for x in list_v[j].split("_")]
                if abs(kaa_1[0] - kaa_2[0]) <= 1 and abs(kaa_1[1] - kaa_2[1]) <= 1:
                    self.add_edge("{}_{}".format(kaa_1[0], kaa_1[1]), "{}_{}".format(kaa_2[0], kaa_2[1]))

    def find_list_connected_component_dfs(self):
        if self.adj_mat is None:
            return list()
        visited = list()
        components = list()
        for i in self.adj_mat:
            if i in visited:
                continue
            a = self.dfs_non_recursive(i)
            visited += a
            components.append(a)
        return components

    def find_list_connected_component_bfs(self):
        if self.adj_mat is None:
            return list()
        visited = list()
        components = list()
        for i in self.adj_mat:
            if i in visited:
                continue
            a = self.bfs_non_recurisve(i)
            visited += a
            components.append(a)
        return components

    def find_list_connected_component(self, algorithm):
        if algorithm.lower() == 'bfs':
            return self.find_list_connected_component_bfs()
        elif algorithm.lower() == 'dfs':
            return self.find_list_connected_component_dfs()


class GraphAdjList:
    def __init__(self):
        self.adj_list = None

    def add_vertex(self, name):
        if self.adj_list is None:
            self.adj_list = {
                name: list()
            }
            return
        self.adj_list[name] = list()

    def add_edge(self, source_vertex, destination_vertex):
        self.adj_list[source_vertex].append(destination_vertex)
        self.adj_list[destination_vertex].append(source_vertex)
        return

    def update_graph(self, mat):
        self.adj_list = None
        list_v = list()
        for i in range(mat.__len__()):
            for j in range(mat[i].__len__()):
                if mat[i][j] == 1:
                    name_v = "{}_{}".format(j, i)
                    self.add_vertex(name_v)
                    list_v.append(name_v)

        for i in range(list_v.__len__()):
            for j in range(i + 1, list_v.__len__()):
                kaa_1 = [int(x) for x in list_v[i].split("_")]
                kaa_2 = [int(x) for x in list_v[j].split("_")]
                if abs(kaa_1[0] - kaa_2[0]) <= 1 and abs(kaa_1[1] - kaa_2[1]) <= 1:
                    self.add_edge("{}_{}".format(kaa_1[0], kaa_1[1]), "{}_{}".format(kaa_2[0], kaa_2[1]))

    def bfs_non_recurisve(self, v):
        visited = [v]
        queue = [v]
        while not queue.__len__() == 0:
            v = queue[0]
            queue = queue[1:]
            for key in self.adj_list[v]:
                if key not in visited:
                    print(key)
                    visited.append(key)
                    queue.append(key)
        return visited

    def dfs_non_recursive(self, v):
        visited = list()
        stack = [v]
        while stack:
            key = stack.pop()
            if key in visited:
                continue
            visited.append(key)
            for i in self.adj_list[key]:
                stack.append(i)
        return visited

    def find_list_connected_component_dfs(self):
        if self.adj_list is None:
            return list()
        visited = list()
        components = list()
        for i in self.adj_list:
            if i in visited:
                continue
            a = self.dfs_non_recursive(i)
            visited += a
            components.append(a)
        return components

    def find_list_connected_component_bfs(self):
        if self.adj_list is None:
            return list()
        visited = list()
        components = list()
        for i in self.adj_list:
            if i in visited:
                continue
            a = self.bfs_non_recurisve(i)
            visited += a
            components.append(a)
        return components

    def find_list_connected_component(self, algorithm):
        if algorithm.lower() == 'bfs':
            return self.find_list_connected_component_bfs()
        elif algorithm.lower() == 'dfs':
            return self.find_list_connected_component_dfs()

# if __name__ == '__main__':
#     graph = Graph()
#     adj_matrix = load_adj_matrix_from_file('adj_matrix_test.txt')
#     list_v = list()
    # for i in range(adj_matrix.__len__()):
    #     for j in range(adj_matrix[i].__len__()):
    #         if adj_matrix[i][j] == 1:
    #             name_v = "{}_{}".format(j, i)
    #             graph.add_vertex(name_v)
    #             list_v.append(name_v)
    #
    # for i in range(list_v.__len__()):
    #     for j in range(i + 1, list_v.__len__()):
    #         kaa_1 = [int(x) for x in list_v[i].split("_")]
    #         kaa_2 = [int(x) for x in list_v[j].split("_")]
    #         if abs(kaa_1[0] - kaa_2[0]) <= 1 and abs(kaa_1[1] - kaa_2[1]) <= 1:
    #             graph.add_edge("{}_{}".format(kaa_1[0], kaa_1[1]), "{}_{}".format(kaa_2[0], kaa_2[1]))

    # graph.print_adj_mat()
    # v = list()
    # for i in graph.adj_mat:
    #     if i in v:
    #         continue
    #     a = graph.DFS(i)
    #     v += a
    #     print(a)
