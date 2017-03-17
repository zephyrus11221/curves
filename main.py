from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

#parse_file( 'script', edges, transform, screen, color )

for i in range(51):
    add_curve(edges, 0, 0, 250-i*5, 0+i*5, 250+i*5, 500-i*5, 500, 500-i*5, .002,  'bezier')
    color = [20, 150-i*3, 100]
    draw_lines(edges, screen, color)
    edges = []
display(screen)


