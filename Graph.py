import random as rnd
from igraph import *


def add_weights(graph):
    list_edges = []
    for i in range(len(graph.es)):
        list_edges.append(rnd.randint(1, 10))
    graph.es["weight"] = list_edges


def set_vertex_names(graph):
    list_names = []
    for i in range(len(graph.vs)):
        list_names.append(i)
    graph.vs["name"] = list_names


def get_vertex_names(graph):
    list_index = []
    for index in graph.vs["name"]:
        list_index.append(index)
    return list_index


def set_edge_color(isSolution):
    if isSolution: return "red"
    return "black"


def solution(graph, solution):
    list_edges_solution = [False] * len(graph.es)
    for i in range(len(solution) - 1):
        if solution[i] > solution[i + 1]:
            index = graph.get_edgelist().index((solution[i + 1], solution[i]))
        else:
            index = graph.get_edgelist().index((solution[i], solution[i + 1]))
        list_edges_solution[index] = True
    if solution[0] > solution[i + 1]:
        index = graph.get_edgelist().index((solution[i + 1], solution[0]))
    else:
        index = graph.get_edgelist().index((solution[0], solution[i + 1]))
    list_edges_solution[index] = True
    return list_edges_solution


def create_full_graph(n_vertex):
    graph = Graph.Full(n_vertex)
    add_weights(graph)
    set_vertex_names(graph)

    return graph


def plot_graph(graph):
    visual_style = {"vertex_label": get_vertex_names(graph), "edge_label": graph.es["weight"]}
    plot(graph, **visual_style)


def plot_graph_solution(graph, best_path):
    solution_edges = solution(graph, best_path)
    visual_style = {
        "vertex_label": get_vertex_names(graph), "edge_label": graph.es["weight"],
        "edge_width": [1 + 2 * int(sol) for sol in solution_edges],
        "edge_color": [set_edge_color(sol) for sol in solution_edges]
    }
    plot(graph, **visual_style)
