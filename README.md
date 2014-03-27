# Jurij

A simple Python application for drawing graphs, useful for teaching and experiments.

To run the program, start `gui.py` from command line or the Python IDLE interface.

The program files are as follows:

* `jurij.py` is the main program which just starts the application
*  `jurij/__init__.py` just imports everything else in `jurij`
* `jurij/graph.py` the graph data structure and basic operations
* `jurij/group.py` finitely-generated groups (used for Cayley graphs)
* `jurij/library.py` basic graphs
* `jurij/view.py` a simple graph viewer with a spring embedder

## How to use the graph viewer

To draw a graph, enter its Python definition in the input field and
press the *Draw!*  button. Examples of definitions:

* `cycle(5)`
* `path(30)`
* `complete_graph(7)`
* `cone(cycle(10))`
* `product(path(3), cycle(4))`
* `igraph(5,2,1)`
* `cayley_graph(symmetric_group(4))`
* `cayley_graph(Group([1,2], operation=(lambda x,y: (x+y)%13)))`
* `cayley_graph(permutation_group([(1,0,2,3), (0,3,1,2)]))`

You can also enter a specific graph by giving a list of edges or an
adjancency dictionary, for example:

      [(1,2), (2,3), (2,4), (3,4)]

or

      {1 : [2], 2 : [3,4], 3 : [4], 4 : []}

For further information on what is available see the modules `jurij.graph`,
`jurij.group` and `jurij.library`.