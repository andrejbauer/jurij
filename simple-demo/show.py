# -*- encoding: utf-8 -*-

# Show an embedded graph.

import tkinter
import math

class Picture():
    def __init__(self, width=300, height=300, title=None):
        self.window = tkinter.Tk()
        self.window.title(title)
        self.canvas = tkinter.Canvas(self.window, width=width, height=height)
        self.canvas.pack()

    def show(self):
        self.window.mainloop()

    
def bounding_box(m):
    '''The bounding box of a graph map.'''
    if m == []:
        return (0,1,0,1)
    else:
        (minx,maxx) = (float('inf'), float('-inf'))
        (miny,maxy) = (float('inf'), float('-inf'))
        for (x,y) in m.values():
            minx = min(minx,x)
            maxx = max(maxx,x)
            miny = min(miny,y)
            maxy = max(maxy,y)
        return (minx,maxx,miny,maxy)

def map_circular(g):
    '''Map the vertices of a graph onto the unit circle.'''
    n = g.size()
    m = {}
    for (k,v) in enumerate(g.vertices()):
        m[v] = (0.5 + 0.5 * math.cos(2.0 * math.pi * float(k) / float(n)),
                0.5 + 0.5 * math.sin(2.0 * math.pi * float(k) / float(n)))
    return m

def map_nice(g, iterations=3000):
    m = map_circular(g)
    for i in range(iterations):
        for u in g.vertices():
            (x,y) = m[u]
            for v in g.vertices():
                if not u == v:
                    (a,b) = m[v]
                    d = (x-a)*(x-a) + (y-b)*(y-b)
                    x -= 0.01 * (a - x)/d;
                    y -= 0.01 * (b - y)/d;
            m[u] = (x,y)
            for (u,v) in g.edges():
                (x,y) = m[u]
                (a,b) = m[v]
                (dx, dy) = (0.01 * (a-x), 0.01 * (b-y))
                m[u] = (x + dx, y + dy)
                m[v] = (a - dx, b - dy)
    return m

def show(g, width=300, height=300, title="Unknown graph"):
    pic = Picture(width=width, height=height, title=title)
    e = map_nice(g)
    (xmin,xmax,ymin,ymax) = bounding_box(e)
    dx = xmax - xmin
    dy = ymax - ymin
    for (u,v) in g.edges():
        (x1,y1) = e[u]
        (x2,y2) = e[v]
        pic.canvas.create_line(int(10 + (x1-xmin)/dx*(width-20)),
                               int(10 + (ymax-y1)/dy*(height-20)),
                               int(10 + (x2-xmin)/dx*(width-20)),
                               int(10 + (ymax-y2)/dy*(height-20)))
    for v in g.vertices():
        (x,y) = e[v]
        x = int(10 + (x-xmin)/dx*(width-20))
        y = int(10 + (ymax-y)/dy*(height-20))
        pic.canvas.create_oval(x-4,y-4,x+4,y+4,fill="white")
    pic.show()
