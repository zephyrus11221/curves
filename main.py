from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
edges1 = []
transform = new_matrix()

#parse_file( 'script', edges, transform, screen, color )

for i in range(51):
    add_curve(edges,
              0, 0,
              250-i*5, 0+i*5,
              250+i*5, 500-i*5,
              500, 500-i*5,
              .002,  'bezier')
    add_curve(edges,
              500, 0,
              500-i*5, 250-i*5,
              0+i*5, 250+i*5,
              0+i*5, 500,
              .002,  'bezier')
    add_curve(edges,
              500, 500,
              250+i*5, 500-i*5,
              250-i*5, 0+i*5,
              0, 0+i*5,
              .002,  'bezier')
    add_curve(edges,
              0, 500,
              0+i*5, 250+i*5,
              500-i*5, 250-i*5, 
              500-i*5, 0,
              .002,  'bezier')

    add_curve(edges1,
              0, 0,
              0, 250+i*5,
              500, 250-i*5,
              500, 250-i*5,
              .002, 'bezier')
    add_curve(edges1,
              500, 0,
              250-i*5, 0,
              250+i*5, 500,
              250+i*5, 500,
              .002, 'bezier')
    add_curve(edges1,
              500, 500,
              500, 250-i*5,
              0, 250+i*5,
              0, 250+i*5,
              .002, 'bezier')
    add_curve(edges1,
              0, 500,
              250+i*5, 500,
              250-i*5, 0,
              250-i*5, 0,
              .002, 'bezier')    
    
    color = [20, 150-i*3, 100]
    draw_lines(edges, screen, color)
    color = [20+i, 0+i, 100]
    draw_lines(edges1, screen, color)
    edges = []
    edges1 = []

save_extension(screen, 'pic.png')
display(screen)


