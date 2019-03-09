from math import isinf
from sys import float_info

class Equation:
    def __init__(s, t, n, i, fx, fy):
        s.t, s.n, s.i = t, n, i
        s.fx, s.fy = fx, fy
        s.xs, s.ys = [], []
        s.oxs, s.oys = [], []
        
    def set_start_time(s, t):
        s.t = t
        
    def create(s):
        s.xs, s.ys = [s.t], [s.t]
        while len(s.xs) < s.n:
            s.xs.append(s.fx(s.xs[-1], s.ys[-1], s.t))
            if isinf(s.xs[-1]):
                s.xs.pop()
                break 
            s.ys.append(s.fy(s.xs[-2], s.ys[-1], s.t))
            if isinf(s.ys[-1]):
                s.xs.pop()
                s.ys.pop()
                break
        minx, maxx = min(s.xs), max(s.xs)
        miny, maxy = min(s.ys), max(s.ys)
        s.xs = [map(i, minx, maxx, .1*width, .9*width) for i in s.xs]
        s.ys = [map(i, miny, maxy, .9*height, .1*height) for i in s.ys]
            
    def update(s):
        s.oxs, s.oys = s.xs[:], s.ys[:]
        s.t += s.i
        s.create()
        
    def show_pattern(s):
        noFill()
        stroke(51, 150)
        beginShape()
        for x, y in zip(s.xs, s.ys):
            vertex(x, y)
        endShape()
        
    def show_change(s):
        h = 0
        for pos in zip(s.oxs, s.oys, s.xs, s.ys):
            stroke(h, 255, 255)
            line(*pos)
            h = (h+1)%256
