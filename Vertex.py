"""
Vertex Class
----------

This class represents an individual Vertex in a Graph. 

Each Vertex consists of the following properties:
    - is_trusted: boolean indicating whether this Vertex is a trusted courier or not
    - edges: A list of vertices connected to this Vertex (adjlist)

The class also supports the following functions:
    - add_edge(Vertex): Adds an edge to the Vertex. 
    - remove_edge(Vertex): Removes an edge from the Vertex
    - get_edges(): Returns a list of all the vertices connected to the Vertex
    - update_status(is_trusted): Updates the status of the Vertex to trusted or not trusted
    - get_is_trusted(): Returns whether the Vertex is trusted or not

Your task is to complete the following functions which are marked by the TODO comment.
You are free to add properties and functions to the class as long as the given signatures remain identical.
Good Luck!
"""


class Vertex():
    # These are the defined properties as described above
    is_trusted: bool
    edges: 'list[Vertex]'

    def __init__(self, is_trusted: bool) -> None:
        """
        The constructor for the Vertex class.
        :param is_trusted: Whether the Vertex is trusted or not.
        """
        self.is_trusted = is_trusted
        self.edges = []

    def add_edge(self, vertex: 'Vertex') -> None:
        """
        Adds an edge to the given vertex.
        If adding the given vertex would result in the graph no 
        longer being simple or the vertex is invalid, do nothing.
        :param vertex: The vertex to add an edge to.
        """
        if vertex == self:
            return
        elif vertex in self.edges:
            return
        elif isinstance(vertex, Vertex) == False or isinstance(self, Vertex) == False:
            return
        else:
            self.edges.append(vertex)
            vertex.edges.append(self)
            return
        return
        # TODO Fill this in

    def remove_edge(self, vertex: 'Vertex') -> None:
        """
        Removes the given vertex from the adjlist.
        If the vertex is invalid or does not exist, do nothing.
        :param vertex: The vertex to remove.
        """
        if vertex == self:
            return
        if isinstance(vertex, Vertex) == False or isinstance(self, Vertex) == False:
            return
        if vertex in self.edges:
            self.edges.remove(vertex)
            vertex.edges.remove(self)
            return
        return
        # TODO Fill this in

    def get_edges(self) -> 'list[Vertex]':
        """
        Returns the list of vertices connected to the current node.
        :return: The list of vertices connected to the current node.
        """

        return self.edges

    def update_status(self, is_trusted: bool) -> None:
        """
        Updates the status of whether the vertex can be trusted or not.
        """
        if isinstance(is_trusted, bool) == False :
            return
        if is_trusted == None:
            return
        if is_trusted == True:
            self.is_trusted = True
        else:
            self.is_trusted = False
        return
        # TODO Fill this in

    def get_is_trusted(self) -> bool:
        """
        Returns whether the vertex is trusted or not.
        :return: True if the vertex is trusted, False otherwise.
        """

        return self.is_trusted