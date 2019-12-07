import random


def print_matrix(mat):
    for i in mat:
        print(i)


def print_adj_list(_list):
    for i in _list:
        print(i)


def generate_random_map(size):
    return [[random.randint(0, 1) for j in range(size)] for i in range(size)]


def adj_matrix_to_adj_list(mat):
    adj_list = [list() for i in range(mat.__len__())]
    for i in range(mat.__len__()):
        for j in range(mat[0].__len__()):
            if mat[i][j] == 1:
                adj_list[i].append(j)
    return adj_list


def adj_list_to_adj_matrix(_list):
    adj_mat = [
        [
            0 for j in range(_list.__len__())
        ]
        for i in range(_list.__len__())
    ]
    for i in range(_list.__len__()):
        for j in range(_list[i].__len__()):
            adj_mat[i][_list[i][j]] = 1
    return adj_mat


def load_adj_matrix_from_file(filename):
    return [
        [
            int(j)
            for j in row.strip().split(' ')
        ]
        for row in open(filename, mode='r').read().split('\n')
        if row.__len__() != 0
    ]


def dfs_matrix(mat, v=0, visited=list()):
    visited.append(v)
    for i in range(mat[v].__len__()):
        if mat[v][i] == 1 and i not in visited:
            visited = dfs_matrix(mat, i, visited)
    return visited


def kosaraju(mat):
    visited = list()
    S = [dfs_matrix(mat, 0)]
    for i in range(1, mat.__len__()):
        for visited in S:
            if i not in visited:
                S.append(dfs_matrix(mat, i))
                break
    return S


class Graph:
    def __init__(self, num_of_node=0):
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
        for key in self.adj_mat:
            for _key in self.adj_mat[key]:
                print(self.adj_mat[key][_key], end=" ")
            print()

    def add_edge(self, source_vertex, destination_vertex):
        self.adj_mat[source_vertex][destination_vertex] = 1
        self.adj_mat[destination_vertex][source_vertex] = 1
        return

    def DFS(self, v, visited=None):
        if visited is None:
            visited = list()
        if self.adj_mat is None:
            return list()
        visited.append(v)
        for key in self.adj_mat[v]:
            if self.adj_mat[v][key] == 1 and key not in visited:
                visited = self.DFS(key, visited)
        return visited


if __name__ == '__main__':
    graph = Graph()
    adj_matrix = load_adj_matrix_from_file('adj_matrix_test.txt')
    list_v = list()
    for i in range(adj_matrix.__len__()):
        for j in range(adj_matrix[i].__len__()):
            if adj_matrix[i][j] == 1:
                name_v = "{}_{}".format(j, i)
                graph.add_vertex(name_v)
                list_v.append(name_v)

    for i in range(list_v.__len__()):
        for j in range(i + 1, list_v.__len__()):
            kaa_1 = [int(x) for x in list_v[i].split("_")]
            kaa_2 = [int(x) for x in list_v[j].split("_")]
            if abs(kaa_1[0] - kaa_2[0]) <= 1 and abs(kaa_1[1] - kaa_2[1]) <= 1:
                graph.add_edge("{}_{}".format(kaa_1[0], kaa_1[1]), "{}_{}".format(kaa_2[0], kaa_2[1]))

    graph.print_adj_mat()
    v = list()
    for i in graph.adj_mat:
        if i in v:
            continue
        a = graph.DFS(i)
        v += a
        print(a)
