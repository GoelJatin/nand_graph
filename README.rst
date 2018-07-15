Graph
=====

Module for parsing a string expression and converting it into a Graph,
and doing NAND / AND operations on the inputs.

Supported Expressions
---------------------

The Expression must be given in a proper format.

**!(A.B)** --> NAND operation on inputs A and B

**C.D**    --> AND operation on inputs C and D

Usage
-----

To convert an expression into a Graph:

#. Import the module graph
#. Call the method **parse_input** and pass the string as the parameter
