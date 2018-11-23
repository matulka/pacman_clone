import pygame
from math import pi
from constants import Black, White
from wall_map import Wall, Map

gameover = False
size = width_scr, height_scr = 700, 700
screen = None
map = Map()


def init():
    global screen
    pygame.init()
    screen = pygame.display.set_mode(size)


def handle_events():
    global gameover
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True


def init_map():
    map.clear() #Надо или нет?
    global width_scr, height_scr
    left, top, width, height = 0, 50, width_scr, 5

    #Верхние и нижние границы
    wall_top_main = Wall(left, top, width_scr, height)
    wall_bottom_main = Wall(left, height_scr-height-top, width_scr, height)
    map.add_ell(wall_top_main)
    map.add_ell(wall_bottom_main)

    #Левая первая сверху и правая первая сверху
    wall_top_left = Wall(left, top+height, height, (height_scr-2*top)/4)
    wall_top_right = Wall(width_scr-height, top+height, height, (height_scr-2*top)/4)
    map.add_ell(wall_top_left)
    map.add_ell(wall_top_right)

    #Маленькие пар топ и боттом слева справа
    wall_center_left = Wall(left + height, top+(height_scr-2*top)/4, width_scr/6, height)
    wall_center_right = Wall(width_scr-width_scr/6, top+(height_scr-2*top)/4, width_scr/6, height)
    map.add_ell(wall_center_left)
    map.add_ell(wall_center_right)

    #Пар верх низ после того что выше сразу
    wall_par_top_left = Wall(left+height+width_scr/6, top+height+(height_scr-2*top)/4-5, height, (height_scr-2*top)/7)
    wall_par_top_right = Wall(width_scr-(left+height+(width_scr/6)), top+height+(height_scr-2*top)/4-5, height,
                              (height_scr-2*top)/7)
    map.add_ell(wall_par_top_right)
    map.add_ell(wall_par_top_left)

    #паралель 3 паре
    wall_center_left_1 = Wall(left, (height_scr-2*top)/4+(height_scr-2*top)/7+top+height-5, width_scr / 6 + 10,
                              height)
    wall_center_right_1 = Wall(width_scr-width_scr/6-5,
                              (height_scr - 2 * top) / 4 + (height_scr - 2 * top) / 7 + top + height - 5,
                              width_scr / 6 + 10,
                              height)
    map.add_ell(wall_center_left_1)
    map.add_ell(wall_center_right_1)

    #
    wall_center_left_2 = Wall(left, (height_scr - 2 * top) / 4 + (height_scr - 2 * top) / 7 + top + height - 5 +
                              height_scr/13,
                              width_scr / 6 + 10,
                              height)
    wall_center_right_2 = Wall(width_scr - width_scr / 6 - 5,
                               (height_scr - 2 * top) / 4 + (height_scr - 2 * top) / 7 + top + height - 5 +
                               height_scr/13,
                               width_scr / 6 + 10,
                               height)
    map.add_ell(wall_center_left_2)
    map.add_ell(wall_center_right_2)


    #
    wall_par_top_left_1 = Wall(left + height + width_scr / 6, (height_scr - 2 * top) / 4 + (height_scr - 2 * top) / 7
                               + top + height - 5 +
                              height_scr/13, height,
                             (height_scr - 2 * top) / 7)
    wall_par_top_right_1 = Wall(width_scr - (left + height + (width_scr / 6)),
                                (height_scr - 2 * top) / 4 + (height_scr - 2 * top) / 7 + top + height - 5 +
                                height_scr / 13, height,
                              (height_scr - 2 * top) / 7)
    map.add_ell(wall_par_top_right_1)
    map.add_ell(wall_par_top_left_1)

    #
    wall_center_left_3 = Wall(left,
                              ((height_scr - 2 * top) / 4 + (height_scr - 2 * top) / 7 + top + height - 5 +
                              height_scr / 13)+((height_scr - 2 * top) / 7)-2,
                              width_scr / 6 + 10,
                              height)
    wall_center_right_3 = Wall(width_scr - width_scr / 6 - 5,
                               ((height_scr - 2 * top) / 4 + (height_scr - 2 * top) / 7 + top + height - 5 +
                                height_scr / 13) + ((height_scr - 2 * top) / 7) - 2,
                               width_scr / 6 + 10,
                               height)
    map.add_ell(wall_center_left_3)
    map.add_ell(wall_center_right_3)



    #
    wall_top_left_2 = Wall(left, ((height_scr - 2 * top) / 4 + (height_scr - 2 * top) / 7 + top + height - 5 +
                              height_scr / 13)+((height_scr - 2 * top) / 7)-2, height,
                              ((height_scr - height - top)-(((height_scr - 2 * top) / 4 +
                                                             (height_scr - 2 * top) / 7 + top + height - 5 +
                              height_scr / 13)+((height_scr - 2 * top) / 7)-2)+3)/2-10)
    wall_top_right_2 = Wall(width_scr-left-height, ((height_scr - 2 * top) / 4 + (height_scr - 2 * top) / 7 + top
                                                    + height - 5 +
                                  height_scr / 13) + ((height_scr - 2 * top) / 7) - 2, height,
                           ((height_scr - height - top) - (((height_scr - 2 * top) / 4 +
                                                            (height_scr - 2 * top) / 7 + top + height - 5 +
                                                            height_scr / 13) + (
                                                                       (height_scr - 2 * top) / 7) - 2) + 3) / 2 - 10)
    map.add_ell(wall_top_left_2)
    map.add_ell(wall_top_right_2)

    #
    wall_center_left_4 = Wall(left,
                              ((height_scr - 2 * top) / 4 + (height_scr - 2 * top) / 7 + top + height - 5 +
                               height_scr / 13) + ((height_scr - 2 * top) / 7) - 2 + (height_scr - 2 * top) / 6,
                              (width_scr / 6 + 10)/3,
                              height)
    wall_center_right_4 = Wall(width_scr-((width_scr / 6 + 10)/3-1),
                              ((height_scr - 2 * top) / 4 + (height_scr - 2 * top) / 7 + top + height - 5 +
                               height_scr / 13) + ((height_scr - 2 * top) / 7) - 2 + (height_scr - 2 * top) / 6,
                              (width_scr / 6 + 10) / 3,
                              height)
    map.add_ell(wall_center_left_4)
    map.add_ell(wall_center_right_4)

    #pygame.draw.arc(screen, (255, 255, 255, 255), [-100, 75, 700, 100], -pi / 6, pi / 6, 5)


def main():
    global gameover
    init()
    while not gameover:
        handle_events()
        screen.fill(Black)
        init_map()
        map.draw()
        pygame.display.flip()
        pygame.time.wait(20)

main()