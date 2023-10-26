class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

def find_parent(parent, vertex):
    if parent[vertex] == -1:
        return vertex
    return find_parent(parent, parent[vertex])

def kruskal_min_max_spanning_tree(edges, num_vertices, min_cost=True):
    edges.sort(key=lambda edge: edge.weight, reverse=min_cost)

    parent = [-1] * num_vertices
    min_max_tree = []

    for edge in edges:
        src_parent = find_parent(parent, edge.src)
        dest_parent = find_parent(parent, edge.dest)

        if src_parent != dest_parent:
            min_max_tree.append(edge)
            parent[src_parent] = dest_parent

    return min_max_tree

def display_tree(tree, min_tree=True):
    if min_tree:
        print("Árbol de Expansión Mínima:")
    else:
        print("Árbol de Máximo Coste:")
    total_weight = 0
    for edge in tree:
        print(f"{edge.src} - {edge.dest} : {edge.weight}")
        total_weight += edge.weight
    print(f"Peso Total del Árbol: {total_weight}")

def main():
    num_vertices = int(input("Ingrese el número de vértices: "))
    num_edges = int(input("Ingrese el número de aristas: "))

    edges = []
    for _ in range(num_edges):
        src, dest, weight = map(int, input("Ingrese (src dest peso): ").split())
        edges.append(Edge(src, dest, weight))

    min_tree = kruskal_min_max_spanning_tree(edges, num_vertices, min_cost=True)
    max_tree = kruskal_min_max_spanning_tree(edges, num_vertices, min_cost=False)

    display_tree(min_tree, min_tree=True)
    display_tree(max_tree, min_tree=False)

if __name__ == "__main__":
    main()

