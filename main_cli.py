from algorithm import GraphAdjList, GraphAdjMatrix

if __name__ == '__main__':
    graph_list = GraphAdjList()
    graph_matrix = GraphAdjMatrix()
    graph_matrix.load_from_graph_file('test_adj_matrix.txt')
    graph_matrix.print_adj_mat()
    print(graph_matrix.find_list_connected_component('bfs').__len__())
    list_file = [i.strip().split(' ') for i in open('test_adj_list.txt', mode='r').read().strip().split('\n')]
    # print(matrix_file)
    # print(list_file)
