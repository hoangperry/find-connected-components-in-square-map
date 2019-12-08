from algorithm import GraphAdjList, GraphAdjMatrix

if __name__ == '__main__':
    graph_matrix = GraphAdjMatrix()
    graph_matrix.load_from_graph_file('test_adj_matrix.txt')
    graph_matrix.print_adj_mat()
    print("Num of connected Component: {}".format(graph_matrix.find_list_connected_component('bfs').__len__()))

    graph_list = GraphAdjList()
    graph_list.load_from_graph_file('test_adj_list.txt')
    graph_list.print_adj_list()
    # print(matrix_file)
    # print(list_file)
