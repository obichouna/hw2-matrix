from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
m1 = new_matrix()
m2 = new_matrix()


draw_lines(matrix, screen, color )
display(screen)
save_extension(screen, 'img.png')
