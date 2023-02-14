from Graph import *
import sys


def load_graph(graph):
    graph.add_vertex("Gilroy")
    graph.add_vertex("Cheyenne")
    graph.add_vertex("Fargo")
    graph.add_vertex("Zanesville")
    graph.add_vertex("Worcester")
    graph.add_vertex("Tupelo")
    graph.add_vertex("Lubbock")

    graph.add_edge("Lubbock", "Gilroy", 1133.82, True)
    graph.add_edge("Lubbock", "Fargo", 958.28, True)
    graph.add_edge("Lubbock", "Zanesville", 1182.17, True)
    graph.add_edge("Fargo", "Zanesville", 881.36, True)
    graph.add_edge("Cheyenne", "Fargo", 562.24, True)
    graph.add_edge("Cheyenne", "Lubbock", 548.06, True)
    graph.add_edge("Gilroy", "Cheyenne", 941.17, True)
    graph.add_edge("Zanesville", "Worcester", 555.24, True)
    graph.add_edge("Tupelo", "Zanesville", 538.58, True)
    graph.add_edge("Tupelo", "Lubbock", 756.94, True)
    graph.add_edge("Worcester", "Tupelo", 1068.52, True)


# end def load_graph(graph):


def path_to_target(start, goal, graph):
    dijkstra(graph, graph.get_vertex(start), graph.get_vertex(goal))
    target = graph.get_vertex(goal)
    path = [target.get_id()]
    shortest(target, path)
    result = path[::-1], target.get_distance()
    reset_visited_and_distances(graph)
    return result


# end def path_to_target(start, goal, graph):

def reset_visited_and_distances(graph):
    for v in graph:
        v.set_distance(sys.maxsize)
        v.clear_visited()


# end def reset_visited_and_distances(graph):

def print_path(array):
    if len(array[0]) == 2:
        print(f"The shortest distance between {array[0][0]} and {array[0][-1]} is {round(array[1])} kilometers.")
    elif len(array[0]) == 3:
        print(
            f"The shortest distance between {array[0][0]} and {array[0][-1]} is {round(array[1])} kilometers through {array[0][-2]}.")
    elif len(array[0]) == 4:
        print(
            f"The shortest distance between {array[0][0]} and {array[0][-1]} is {round(array[1])} kilometers through {array[0][-3]} and {array[0][-2]}.")


# end def print_path(array, via=None):


def main():
    graph = Graph()
    load_graph(graph)
    pathGilroyLubbock = path_to_target("Gilroy", "Lubbock", graph)
    load_graph(graph)
    pathGilroyZanesville = path_to_target("Gilroy", "Zanesville", graph)
    load_graph(graph)
    pathTupeloFargo = path_to_target("Tupelo", "Fargo", graph)
    load_graph(graph)
    pathWorcesterGilroy = path_to_target("Worcester", "Gilroy", graph)

    print_path(pathGilroyLubbock)
    print_path(pathGilroyZanesville)
    print_path(pathTupeloFargo)
    print_path(pathWorcesterGilroy)


# end def main():


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
