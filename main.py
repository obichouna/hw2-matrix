from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 0 ]
m1 = new_matrix()
add_edge(m1, 100, 175, 0, 250, 100, 0)
add_edge(m1, 400, 175, 0, 250, 100, 0)

add_edge(m1, 250, 400, 0, 250, 100, 0)
add_edge(m1, 400, 175, 0, 250, 400, 0)
add_edge(m1, 100, 175, 0, 250, 400, 0)
draw_lines(m1, screen, color )
display(screen)
save_extension(screen, 'img.png')
