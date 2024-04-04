def build_metro_graph(lines):
    """
    This function builds a graph representation of a metro system.

    Args:
        lines (dict): A dictionary where keys are metro line names and values are lists of stations on that line.

    Returns:
        dict: A graph where keys are stations and values are dictionaries representing neighboring stations and the transfer time between them.
    """
    # Now every edge is set to 1
    graph = {}
    for line, stations in lines.items():
        for i, station in enumerate(stations):
            if station not in graph:
                graph[station] = {}
            if i > 0:
                graph[station][stations[i-1]] = 1
            if i < len(stations) - 1:
                graph[station][stations[i+1]] = 1
    return graph

def dijkstra_algo(graph, start_station, end_station):
    """
    This function implements Dijkstra's algorithm to find the shortest path between two stations in a metro network.

    Args:
        graph (dict): A graph representation of the metro system.
        start_station (str): The name of the starting station.
        end_station (str): The name of the destination station.

    Returns:
        list, int: A list representing the shortest path from start_station to end_station, 
                   and the total travel time on that path.
    """
    shortest_distance = {station: float('inf') for station in graph}
    shortest_distance[start_station] = 0
    visited = set()
    predecessors = {}
    while visited != set(graph):
        current_station = min((set(shortest_distance.keys()) - visited), key=shortest_distance.get)
        visited.add(current_station)
        for neighbor, weight in graph[current_station].items():
            if shortest_distance[neighbor] > shortest_distance[current_station] + weight:
                shortest_distance[neighbor] = shortest_distance[current_station] + weight
                predecessors[neighbor] = current_station
    # Reconstruct the shortest path
    shortest_path = [end_station]
    while end_station != start_station:
        end_station = predecessors[end_station]
        shortest_path.append(end_station)
    shortest_path.reverse()
    return shortest_path, shortest_distance[shortest_path[-1]]