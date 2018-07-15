# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 20:52:20 2018

@author: Jatin Goel
"""


import re


class InvalidInputError(ValueError):
    """Custom Error class for raising exception in case of Invalid Input."""

    def __init__(self, message):
        super(InvalidInputError).__init__(message)


class Node:
    """Class for representing a single Node in the Graph."""

    def __init__(self, value):
        """Initializes a Node.

            Args:
                value (int):     value to be initialized for the Node

            Returns:
                object:     instance of the **Node** class for the given value

        """
        self._value = value

    def __repr__(self):
        """Returns the string representation for the instance of this class."""
        return f'Node: [{self.value}]'

    @property
    def value(self):
        """Returns the value that the Node holds."""
        return self._value


class NAND:
    """Class for doing the NAND logical operation on the 2 given Nodes."""

    def __init__(self, input_a, input_b):
        """Initializes an instance of the NAND class

            Args:
                input_a     (Node):     input A to the NAND Gate

                input_b     (Node):     input B to the NAND Gate

            Returns:
                object:     instance of the **NAND** class

        """
        self._input_a = input_a
        self._input_b = input_b
        self._output = None

    def __repr__(self):
        """Returns the string representation of the instance of this class."""
        return (
            f'NAND Gate with inputs A: [{self.input_a}] and B: '
            f'[{self.input_b}], with the output: [{self.output}]'
        )

    def _compute(self):
        """Computes the output of the NAND operation on the inputs A and B."""
        if self._output is None:
            and_result = ~(self.input_a.value & self.input_b.value)
            # returns the output after the AND operation on the 2 inputs
            # and then the 2's complement on it, returning signed decimal value

            # convert the signed decimal to unsigned decimal
            bits = 4

            while True:
                if abs(and_result) < 2 ** bits:
                    break
                else:
                    bits *= 2

            value = 2 ** bits - abs(and_result)

            self._output = Node(value)

    @property
    def input_a(self):
        """Returns the Node consisting of input A to the NAND Gate."""
        return self._input_a

    @property
    def input_b(self):
        """Returns the Node consisting of input B to the NAND Gate."""
        return self._input_b

    @property
    def output(self):
        """Returns the Node consisting of the output to the NAND Gate."""
        self._compute()
        return self._output

    def reset(self):
        """Reset the output of NAND Gate to None."""
        self._output = None


class Graph:
    """Class for representing a Directed Acyclic Graph."""

    def __init__(self):
        """Initializes the Graph.

            Args:
                None

            Returns:
                object:     instance of the **Graph** class

        """
        self._nodes = set()
        self._edges = {}

    def __str__(self):
        """Returns the Graph in pretty format."""
        res = f'{self.__repr__()}\n\nEdges:\n'

        for i in self.edges:
            if self.edges[i]:
                for j in self.edges[i]:
                    res = f'{res}\t{i}\t-->\t{j}\n'

            else:
                res = f'{res}\t{i}\t-->\tNo Edges\n'

        return res

    def __repr__(self):
        """Returns the string representation of the instance of this class."""
        return f"Instance of the Graph class with nodes: [{self.nodes}]"

    @property
    def nodes(self):
        """Returns the set of all Nodes present in the Graph."""
        return self._nodes

    @property
    def edges(self):
        """Returns the dictionary of edges in the Graph."""
        return self._edges

    def has_node(self, node):
        """Checks whether the given node is present in the Graph or not.

            Args:
                node (Node):    instance of the Node class
                to check for presence

            Returns:
                bool:   boolean whether the node is present in the Graph or not

        """
        for i in self.nodes:
            if i.value == node.value:
                return True

        return False

    def get_node(self, value):
        """Returns the Node in the graph which holds the give value.

            Args:
                value   (int):  value of the Node

            Returns:
                object  (Node):     instance of the Node class which holds
                the given value

            Raises:
                ValueError:
                    if no Node exists with the given value

        """
        for node in self.nodes:
            if node.value == value:
                return node

        raise ValueError('No Node exists with the given value')

    def add_node(self, node, ignore_errors=False):
        """Adds a node to the Graph.

            Args:
                node            (Node):     instance of the Node class to add

                ignore_errors   (bool):     boolean flag to speficy whether to
                raise ValueError if the Node already exists or ignore it

                    default:    False

            Returns:
                None:   if the node was added successfully

            Raises:
                ValueError:
                    if node already exists in the Graph

        """
        if self.has_node(node):
            if ignore_errors is False:
                raise ValueError('Node already exists')
        else:
            self._nodes.add(node)
            self._edges[node] = set()

    def add_edge(self, edge):
        """Adds a new edge to the Graph.

            Args:
                edge (NAND):    instance of the NAND class to add

            Returns:
                None:   if the edge was added successfully

            Raises:
                ValueError:
                    if node A / node B of the edge does not exists in the Graph

        """
        source = edge.input_a
        destination = edge.input_b

        if not (self.has_node(source) and self.has_node(destination)):
            raise ValueError('Nodes not present in the Graph!')
        else:
            if destination not in self.edges[source]:
                self.edges[source].add(destination)


def parse_input(input_string):
    """Parses the given input string and generates a Graph.

        Supported Format:

            !(C.D).!(!(A.B).C)

        where,

        x1.x2   --  2 inputs to the Gate

        !       --  NAND operation

    """
    graph = Graph()

    nand_expression = r'!\((\d*).(\d*)\)'
    match = re.search(nand_expression, input_string)

    output_str = ''

    while match:
        node1, node2 = map(lambda x: Node(int(x)), match.groups(0))

        # check if a Node with same value already exists
        try:
            node1 = graph.get_node(node1.value)
        except ValueError:
            pass

        try:
            node2 = graph.get_node(node2.value)
        except ValueError:
            pass

        nand1 = NAND(node1, node2)

        graph.add_node(node1, ignore_errors=True)
        graph.add_node(node2, ignore_errors=True)
        graph.add_edge(nand1)
        graph.add_node(nand1.output, ignore_errors=True)

        input_string = input_string.replace(
            match.group(), str(nand1.output.value)
        )
        match = re.search(nand_expression, input_string)
        output_str = f'{output_str}\n\t{input_string}\n'

    output = list(map(int, input_string.split('.')))

    if len(output) > 2:
        raise InvalidInputError('Input is not in the expected format')

    if len(output) == 2:
        output = output[0] & output[1]
    else:
        output = output[0]

    print(output_str)
    print('\t', output, '\n')

    return graph, output


if __name__ == '__main__':

    INPUT_STRINGS = [
        '!(!(1.2).3)',
        '!(1.2).3',
        '!(10.20).!(30.40)'
    ]

    for INPUT_STRING in INPUT_STRINGS:
        print(f'Input String: {INPUT_STRING}\n')

        GRAPH, OUTPUT = parse_input(INPUT_STRING)

        print('Graph Instance: ', GRAPH, sep='\n')

        print('Output: ', OUTPUT, '\n\n')
