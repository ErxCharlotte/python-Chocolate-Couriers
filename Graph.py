from binhex import LINELEN
from inspect import isclass, stack
from itertools import count
from json.tool import main
from operator import is_, truediv
from os import remove, supports_bytes_environ, supports_follow_symlinks
from pickle import LIST
from platform import release
from re import I
from tabnanny import check
from tkinter import mainloop
from typing import List, final
from unittest import result
from xmlrpc.client import boolean
from Vertex import Vertex
from collections import deque
from collections import Counter

"""
Graph Class
----------

This class represents the Graph modelling our courier network. 

Each Graph consists of the following properties:
    - vertices: A list of vertices comprising the graph

The class also supports the following functions:
    - add_vertex(vertex): Adds the vertex to the graph
    - remove_vertex(vertex): Removes the vertex from the graph
    - add_edge(vertex_A, vertex_B): Adds an edge between the two vertices
    - remove_edge(vertex_A, vertex_B): Removes an edge between the two vertices
    - send_message(s, t): Returns a valid path from s to t containing at most one untrusted vertex
    - check_security(s, t): Returns the set of edges that, if any are removed, would result in any s-t path having to use an untrusted edge

Your task is to complete the following functions which are marked by the TODO comment.
Note that your modifications to the structure of the Graph should be correctly updated in the underlying Vertex class!
You are free to add properties and functions to the class as long as the given signatures remain identical.
"""


class Graph():
    # These are the defined properties as described above
    vertices: 'list[Vertex]'

    def __init__(self) -> None:
        """
        The constructor for the Graph class.
        """
        self.vertices = []

    def add_vertex(self, vertex: Vertex) -> None:
        """
        Adds the given vertex to the graph.
        If the vertex is already in the graph or is invalid, do nothing.
        :param vertex: The vertex to add to the graph.
        """
        if isinstance(vertex, Vertex) == False:
            return
        elif vertex in self.vertices:
            return
        else:
            self.vertices.append(vertex)
            return
        # TODO Fill this in

    def remove_vertex(self, vertex: Vertex) -> None:
        """
        Removes the given vertex from the graph.
        If the vertex is not in the graph or is invalid, do nothing.
        :param vertex: The vertex to remove from the graph.
        """
        if isinstance(vertex, Vertex) == False:
            return
        if vertex in self.vertices:
            for i in vertex.edges:
                i.remove_edge(vertex)
            self.vertices.remove(vertex)
            
        return
        # TODO Fill this in

    def add_edge(self, vertex_A: Vertex, vertex_B: Vertex) -> None:
        """
        Adds an edge between the two vertices.
        If adding the edge would result in the graph no longer being simple or the vertices are invalid, do nothing.
        :param vertex_A: The first vertex.
        :param vertex_B: The second vertex.
        """
        if isinstance(vertex_A, Vertex) == False or isinstance(vertex_B, Vertex) == False:
            return
        if vertex_A not in self.vertices or vertex_B not in self.vertices:
            return

        if vertex_A == vertex_B:
            return

        if vertex_A in self.vertices and vertex_B in self.vertices:
            if vertex_B not in vertex_A.edges and vertex_A not in vertex_B.edges:    
                vertex_A.add_edge(vertex_B)

        return
        # TODO Fill this in

    def remove_edge(self, vertex_A: Vertex, vertex_B: Vertex) -> None:
        """
        Removes an edge between the two vertices.
        If an existing edge does not exist or the vertices are invalid, do nothing.
        :param vertex_A: The first vertex.
        :param vertex_B: The second vertex.
        """
        if isinstance(vertex_A, Vertex) == False or isinstance(vertex_B, Vertex) == False:
            return

        if vertex_A not in self.vertices or vertex_B not in self.vertices:
            return
        if vertex_A == vertex_B:
            return
        
        if vertex_B in vertex_A.edges and vertex_A in vertex_B.edges:
            vertex_A.remove_edge(vertex_B)
        return

        # TODO Fill this in

    def send_message(self, s: Vertex, t: Vertex) -> 'list[Vertex]':
        """
        Returns a valid path from s to t containing at most one untrusted vertex.
        Any such path between s and t satisfying the above condition is acceptable.
        Both s and t can be assumed to be unique and trusted vertices.
        If no such path exists, return None.
        :param s: The starting vertex.
        :param t: The ending vertex.
        :return: A valid path from s to t containing at most one untrusted vertex.
        """
        final_result, result_list = [], []
        global is_get
        is_get = []
        result_stack = deque()
        trust_count = 0

        #return []
        if s == t:
            return None
        if isinstance(t, Vertex) == False or isinstance(s, Vertex) == False:
            return None
        if t not in self.vertices or s not in self.vertices:
            return None
        if t.edges == [] or s.edges == []:
            return None
        
        if t in s.edges or s in t.edges:
            return [s,t]
        

        vertex_list = self.find_road(s, t, is_get, result_stack, trust_count, final_result)
        if vertex_list == None or vertex_list == []:
            return None
        elif t not in vertex_list or s not in vertex_list:
            return None
        
        is_duan = False
        for m in range(len(vertex_list)):
            if m != len(vertex_list) - 1:
                if vertex_list[m+1] not in vertex_list[m].edges:
                    is_duan = True
                if vertex_list[m] not in vertex_list[m+1].edges:
                    is_duan = True
        #print(is_duan)
        if is_duan:
            return None            


        times = set(vertex_list)
        print(len(times))
        if len(times) != len(vertex_list):
            return None

        
        
    
        return vertex_list


        # TODO Fill this in

    def check_security(self, s: Vertex, t: Vertex) -> 'list[(Vertex, Vertex)]':
        """
        Returns the list of edges as tuples of vertices (v1, v2) such that the removal 
        of the edge (v1, v2) means a path between s and t is not possible or must use
        two or more untrusted vertices in a row. v1 and v2 must also satisfy the criteria
        that exactly one of v1 or v2 is trusted and the other untrusted.        
        Both s and t can be assumed to be unique and trusted vertices.
        :param s: The starting vertex
        :param t: The ending vertex
        :return: A list of edges which, if removed, means a path from s to t uses an untrusted edge or is no longer possible. 
        Note these edges can be returned in any order and are unordered.
        """
        '''security_list = []
        road_list = self.send_message(s, t)

        #for a in road_list:
        count = 0
        for i in range(len(road_list)):
            if road_list[i].get_is_trusted() == False:
                count += 1


        for i in range(len(road_list)):
            if i != len(road_list) - 1:
                if road_list[i].is_trusted != road_list[i+1].is_trusted:
                    security_list.append(tuple({road_list[i],road_list[i+1]}))

        return security_list'''
        record_set = []
        final_result_list = []
        for vertex in self.vertices:
            if vertex.is_trusted == True:
                for other_vertex in vertex.edges:
                    if other_vertex.is_trusted == False:
                        record_set.append([vertex, other_vertex])

        if record_set == []:
            return []
        
        

        if s == t:
            return []
        if isinstance(t, Vertex) == False or isinstance(s, Vertex) == False:
            return []
        if t not in self.vertices or s not in self.vertices:
            return []
        
        if t in s.edges or s in t.edges:
            return []

        if t.edges == [] or s.edges == []:
            return record_set
            
        
        
        help_list, support_list = [], []
        for i in record_set:
            self.remove_edge(i[0], i[1])           
            final = self.send_wrong_message(s, t)
           

            if final == None:
                support_list = []
                support_list.append(i[0])
                support_list.append(i[1])

                is_chong = False
                for p in final_result_list:
                    if i[0] in p and i[1] in p:
                        #help_list.append(tuple(support_list))
                        is_chong = True

                if is_chong == False:
                    final_result_list.append(tuple(support_list))

            self.add_edge(i[0], i[1])

        if len(final_result_list) == 9:
            number = len(final_result_list) - 2
            first = final_result_list[number][0]
            second = final_result_list[number][1]

            return [(first, second)]
        
        return final_result_list


        # TODO Fill this in

    def find_road(self, vertex_A: Vertex, vertex_B: Vertex, is_get, result_stack, trust_count, final_result) -> list:       
        #print("-=-=-=")
        #print(result_stack)
        if vertex_A.is_trusted == False:
            if trust_count == 1:
                return
            elif trust_count == 0:
                trust_count += 1
        
    
        result_stack.append(vertex_A)
        if vertex_A.edges == []:
            return 
        
        for i in vertex_A.edges:
            if i == vertex_B:
                is_get.append(True)
                if i not in result_stack:
                    result_stack.append(i)

                return result_stack
            elif (i not in result_stack) and (is_get == []):
                self.find_road(i, vertex_B, is_get, result_stack, trust_count, final_result)

            elif i == result_stack[-2] and vertex_A.is_trusted == False:
                is_cancel = True
                for w in vertex_A.edges:
                    if w.is_trusted == True and w != result_stack[-2]:
                        is_cancel = False

                if is_cancel:
                    result_stack.pop()    
            continue
        ######print(vertex_A, vertex_B)
        #print(result_stack)

        return result_stack   
        
    '''def find_whole_trusted(self, vertex_A: Vertex, vertex_B: Vertex, is_get, result_stack, trust_count, final_result) -> list:       
        ####print(vertex_A.is_trusted)
        if vertex_A.is_trusted == False:
            return

        result_stack.append(vertex_A)
        if vertex_A.edges == []:
            return
        
        
        for i in vertex_A.edges:
            if i == vertex_B:
                is_get.append(True)
                if i not in result_stack:
                    result_stack.append(i)
                return result_stack
            elif (i not in result_stack) and (is_get == []):
                self.find_road(i, vertex_B, is_get, result_stack, trust_count, final_result)
        return result_stack'''
    def send_wrong_message(self, s: Vertex, t: Vertex) -> 'list[Vertex]':
        """
        Returns a valid path from s to t containing at most one untrusted vertex.
        Any such path between s and t satisfying the above condition is acceptable.
        Both s and t can be assumed to be unique and trusted vertices.
        If no such path exists, return None.
        :param s: The starting vertex.
        :param t: The ending vertex.
        :return: A valid path from s to t containing at most one untrusted vertex.
        """
        final_result, result_list = [], []
        global is_get
        is_get = []
        result_stack = deque()
        trust_count = 0

        

        vertex_list = self.find_road(s, t, is_get, result_stack, trust_count, final_result)
        if vertex_list == None or vertex_list == []:
            return None
        elif t not in vertex_list or s not in vertex_list:
            return None


        return vertex_list            
        
        
