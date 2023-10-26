import sys
import matplotlib.pyplot as plt

class PrimMST:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = None

        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v

        return min_index

    def prim_mst(self):
        parent = [-1] * self.V
        key = [sys.maxsize] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

            self.print_mst_step(u, parent, key)

    def print_mst_step(self, u, parent, key):
        print("Edge \tWeight")
        total_weight = 0
        for i in range(1, self.V):
            print("{} - {}\t{}".format(parent[i], i, self.graph[i][parent[i]]))
            total_weight += self.graph[i][parent[i]]
        print("Total Weight of MST: {}".format(total_weight))

    def draw_graph(self):
        G = plt.figure()
        pos = {i: (i * 30, 0) for i in range(self.V)}

        for i in range(self.V):
            for j in range(i, self.V):
                if self.graph[i][j] > 0:
                    plt.plot([i, j], [0, 0], 'ro-')
                    plt.text((i + j) / 2, -2, str(self.graph[i][j]))

        plt.title("Minimum Spanning Tree")
        plt.show()

if __name__ == "__main__":
    vertices = 5
    g = PrimMST(vertices)

    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    g.draw_graph()
    g.prim_mst()
