from ast import expr_context
import graphlib
from pathlib import Path
from pickle import TRUE
from re import A
from Graph import Graph
from Vertex import Vertex

import unittest


def assert_equal(got, expected, msg):
    """
    Simple assert helper
    """
    assert expected == got, \
        "[{}] Expected: {}, got: {}".format(msg, expected, got)


def assert_lists(got: 'list[Vertex]', expected: 'list[Vertex]'):
    """
    Assert two lists are equal not considering order
    """
    assert_equal(len(got), len(expected),
                 "Incorrect number of elements returned")
    for i in range(len(got)):
        assert got[i] in expected,\
            "Element {} not in expected list".format(got[i])


class SampleGraphTestCases(unittest.TestCase):
    """
    Sample testing functionality for the Graph class
    Feel free to add your own tests here!
    """

    def setUp(self):
        """
        Set up the vertices to be used throughout the test
        This is a basic graph
        A(T)-B(U)
        |     |
        C(U)-D(T)
        """
        self.graph = Graph()

        self.A = Vertex(True)
        self.B = Vertex(False)
        self.C = Vertex(True)
        self.D = Vertex(False)
        self.E = Vertex(False)
        self.F = Vertex(True)
        self.vertices = [self.A, self.B, self.C, self.D,self.E, self.F]

        self.graph.add_vertex(self.A)
        self.graph.add_vertex(self.B)
        self.graph.add_vertex(self.C)
        self.graph.add_vertex(self.D)
        self.graph.add_vertex(self.E)
        self.graph.add_vertex(self.F)

        self.graph.add_edge(self.A, self.B)
        self.graph.add_edge(self.A, self.C)
        #self.graph.add_edge(self.A, self.D)
        self.graph.add_edge(self.B, self.D)
        self.graph.add_edge(self.D, self.F)
        self.graph.add_edge(self.E, self.C)
        self.graph.add_edge(self.F, self.E)
        #self.graph.add_edge(self.E, self.D)
      

    def test_graph_construction(self):
        """
        Test that the sample graph is correctly constructed
        """
        assert_lists(self.vertices, self.graph.vertices)
        assert_lists(self.A.get_edges(), [self.B, self.C])
        assert_lists(self.B.get_edges(), [self.A, self.D])
        assert_lists(self.C.get_edges(), [self.A, self.D])
        assert_lists(self.D.get_edges(), [self.B, self.C])

    def test_graph_add_edge(self):
        """
        Test that an extra edge can be added to the sample graph
        """
        self.graph.add_edge(self.A, self.D)

        assert_lists(self.A.get_edges(), [self.B, self.C, self.D])
        assert_lists(self.B.get_edges(), [self.A, self.D])
        assert_lists(self.C.get_edges(), [self.A, self.D])
        assert_lists(self.D.get_edges(), [self.A, self.B, self.C])

    def test_graph_remove_edge(self):
        """
        Test that an edge can be removed from the sample graph
        """
        self.graph.remove_edge(self.A, self.C)
        
        assert_lists(self.A.get_edges(), [self.B])
        assert_lists(self.B.get_edges(), [self.A, self.D])
        assert_lists(self.C.get_edges(), [self.D])
        assert_lists(self.D.get_edges(), [self.B, self.C])

    def test_graph_send_message(self):
        """
        Test that we can send a message from A to C
        """
        #self.graph.remove_edge(self.A, self.C)
        #self.graph.remove_edge(self.A, self.B)
        #self.graph.remove_edge(self.B, self.D)
        #self.graph.add_edge(self.A, self.D)
        #self.graph.add_edge(self.C, self.E)
        #self.graph.add_edge(self.A, self.D)
        #self.graph.add_edge(self.B, self.E)
        #self.graph.remove_edge(self.B, self.C)
        path = self.graph.send_message(self.A, self.F)
        #a = self.graph.send_message(self, self.A, self.D)
        print(self.A, self.B, self.C, self.D, self.E, self.F)
        print(path)
        
        assert_equal(len(path), 3, "Incorrect number of vertices in path")
        #assert_equal(len(path), 3, "Incorrect number of vertices in path")
        #assert_equal(path[0] == self.A, True, "Incorrect path")
        #assert_equal(path[1] == self.B, True, "Incorrect path")
        #assert_equal(path[2] == self.D, True, "Incorrect path")

        #self.graph.add_edge(self.A, self.D)
        #path = self.graph.send_message(self.A, self.D)

    def test_graph_check_security(self):
        """
        Test the check security function
        """
        '''print(self.graph.vertices)
        res = self.graph.check_security(self.A, self.F)
        print(res)'''

        print(self.A, self.B, self.C, self.D, self.E, self.F)
        res = self.graph.check_security(self.A, self.F)
        print(res)

        assert_equal(res, [], "Incorrect edges returned")

if __name__ == "__main__":

    SampleGraphTestCases.setUp(unittest.TestCase)
    #SampleGraphTestCases.test_graph_construction(unittest.TestCase)
    #SampleGraphTestCases.test_graph_add_edge(unittest.TestCase)
    #SampleGraphTestCases.test_graph_remove_edge(unittest.TestCase)
#SampleGraphTestCases.test_graph_send_message(unittest.TestCase)
    SampleGraphTestCases.test_graph_check_security(unittest.TestCase)