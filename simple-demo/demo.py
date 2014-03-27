#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from graph import *
from show import *

# The graphs to be shown
for (t, g) in (
    ('K7', complete_graph(7)),
    ('K5', complete_graph(5)),
    ('Cube', cayley_graph({(1,0,2,3,4,5), (0,1,3,2,4,5), (0,1,2,3,5,4)})),
    ('C10', cayley_graph({1}, composition=(lambda x, y: (x+y)%10))),
    ('C6', cayley_graph({1}, composition=(lambda x, y: (x+y)%6))),
    ('What is this?', cayley_graph({1,5}, composition=(lambda x, y: (x+y)%10))),
    ):
    show(g, title=t)

