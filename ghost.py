import pygame as pg
from time import time
from character import Character
from constants import RIGHT, LEFT, DOWN, UP, BLUE_RELEASE_TIME, RED_RELEASE_TIME, ORANGE_RELEASE_TIME,\
    PINK_RELEASE_TIME, DEATH_RELEASE_TIME, EMPTY, SEED, BIG_SEED, SPACE_BLOCKS, TELEPORT,\
    PACMAN, FEAR_DURATION, LAST_EPISODE_FEAR, CHARACTER_SPEED
import queue


class Ghost(Character):
    def __init__(self, coordinates, ghost_type, wall_size, teleport_coordinates):
        super().__init__(coordinates, wall_size)

        self.teleport_coordinates = teleport_coordinates
        self.alive = True
        self.type = ghost_type  # #blue, red, orange, pink
        self.released = False
        self.is_it_start = True
        self.starting_time = None
        self.already_died = False

        if self.type == 'blue':
            self.time_to_release = BLUE_RELEASE_TIME
        elif self.type == 'red':
            self.time_to_release = RED_RELEASE_TIME
        elif self.type == 'orange':
            self.time_to_release = ORANGE_RELEASE_TIME
        else:
            self.time_to_release = PINK_RELEASE_TIME

        path_part = 'ghost_' + self.type
        left1 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_left1.png')
        left2 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_left2.png')
        right1 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_right1.png')
        right2 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_right2.png')
        down1 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_down1.png')
        down2 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_down2.png')
        up1 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_up1.png')
        up2 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_up2.png')
        self.normal_sprites = [[left1, left2], [right1, right2], [up1, up2], [down1, down2]]
        for i in range(len(self.normal_sprites)):
            for j in range(len(self.normal_sprites[i])):
                self.normal_sprites[i][j] = pg.transform.scale(self.normal_sprites[i][j], \
                                            (int(wall_size + SPACE_BLOCKS * 2), int(wall_size + SPACE_BLOCKS * 2)))
        self.sprite_matrix = self.normal_sprites
        self.rect.width = self.rect.height = wall_size + SPACE_BLOCKS * 2
        blue1 = pg.image.load('sprites/fear/fear_blue1.png')
        blue2 = pg.image.load('sprites/fear/fear_blue2.png')
        white1 = pg.image.load('sprites/fear/fear_white1.png')
        white2 = pg.image.load('sprites/fear/fear_white2.png')
        self.fear_sprites = [[blue1, blue2], [blue1, blue2], [blue1, blue2], [blue1, blue2]]
        self.fear_sprites2 = [[blue1, blue2, white1, white2], [blue1, blue2, white1, white2],\
                        [blue1, blue2, white1, white2], [blue1, blue2, white1, white2]]
        for i in range(len(self.fear_sprites)):
            for j in range(len(self.fear_sprites[i])):
                self.fear_sprites[i][j] = pg.transform.scale(self.fear_sprites[i][j], \
                                            (int(wall_size + SPACE_BLOCKS * 2), int(wall_size + SPACE_BLOCKS * 2)))
        for i in range(len(self.fear_sprites2)):
            for j in range(len(self.fear_sprites2[i])):
                self.fear_sprites2[i][j] = pg.transform.scale(self.fear_sprites2[i][j], \
                                            (int(wall_size + SPACE_BLOCKS * 2), int(wall_size + SPACE_BLOCKS * 2)))

        down = pg.image.load('sprites/eyes/eyes_down.png')
        right = pg.image.load('sprites/eyes/eyes_right.png')
        left = pg.image.load('sprites/eyes/eyes_left.png')
        up = pg.image.load('sprites/eyes/eyes_up.png')
        self.eyes_sprites = [[left], [right], [up], [down]]
        for i in range(len(self.eyes_sprites)):
            for j in range(len(self.eyes_sprites[i])):
                self.eyes_sprites[i][j] = pg.transform.scale(self.eyes_sprites[i][j], \
                                            (int(wall_size + SPACE_BLOCKS * 2), int(wall_size + SPACE_BLOCKS * 2)))

    def change_sprites(self, needed_condition):
        self.current_sprite = 0
        if needed_condition == 'normal':
            self.sprite_matrix = self.normal_sprites
        elif needed_condition == 'fear':
            self.sprite_matrix = self.fear_sprites
        elif needed_condition == 'fear2':
            self.sprite_matrix = self.fear_sprites2
        elif needed_condition == 'death':
            self.sprite_matrix = self.eyes_sprites

    def get_possible_directions(self, map):
        old_direction = self.direction

        possible_directions = []
        for direction in [LEFT, UP, RIGHT, DOWN]:
            self.direction = direction
            self.move()
            if not self.check_collision_with_walls(map.walls):
                possible_directions.append(direction)
            self.move_back()

        self.direction = old_direction
        return possible_directions

    def bfs(self, destination_coordinates, map, possible_directions):
        main_queue = queue.Queue()
        self_coordinates = map.return_coordinates(self)
        matrix = map.matrix
        i, j = self_coordinates
        used = [[False] * len(matrix[0]) for n in range(len(matrix))]
        used[i][j] = True
        directions = [[-1] * len(matrix[0]) for n in range(len(matrix))]
        adjacent_queue = queue.Queue()
        push_available_directions(self_coordinates, matrix, adjacent_queue, used)
        while not adjacent_queue.empty():
            new_i, new_j = adjacent_queue.get()
            if new_j > j:
                direction = RIGHT
            elif new_j < j:
                direction = LEFT
            elif new_i > i:
                direction = DOWN
            else:
                direction = UP
            directions[new_i][new_j] = direction
            main_queue.put((new_i, new_j))
        while not main_queue.empty():
            i, j = main_queue.get()
            if not used[i][j]:
                used[i][j] = True
                push_available_directions((i, j), matrix, adjacent_queue, used)
                push_available_directions((i, j), matrix, main_queue, used)
                while not adjacent_queue.empty():
                    new_i, new_j = adjacent_queue.get()
                    if not used[new_i][new_j]:
                        directions[new_i][new_j] = directions[i][j]

        i, j = destination_coordinates

        if directions[i][j] in possible_directions:
            return directions[i][j]
        else:
            return self.direction

    def move_to_wall(self, game):
        for i in range(self.speed - 1):
            if self.direction == RIGHT:
                self.rect.x += 1
                if self.check_collision_with_walls(game.map.walls):
                    self.rect.x -= 1
                    break
            elif self.direction == LEFT:
                self.rect.x -= 1
                if self.check_collision_with_walls(game.map.walls):
                    self.rect.x += 1
                    break
            elif self.direction == UP:
                self.rect.y -= 1
                if self.check_collision_with_walls(game.map.walls):
                    self.rect.y += 1
                    break
            else:
                self.rect.y += 1
                if self.check_collision_with_walls(game.map.walls):
                    self.rect.y -= 1
                    break

    def logic(self, pacman, game):
        if self.released:

            if self.alive:
                possible_directions = self.get_possible_directions(game.map)
                old_direction = self.direction
                self.direction = self.bfs(game.map.return_coordinates(pacman), game.map, possible_directions)
                if game.fear and not self.already_died:
                    possible_directions.remove(self.direction)
                    if old_direction in possible_directions:
                        self.direction = old_direction
                    else:
                        self.direction = possible_directions[0]

                    # #проверка, надо ли поменять спрайты на мигающего призрака
                    if FEAR_DURATION - game.time_fear <= LAST_EPISODE_FEAR and self.sprite_matrix != self.fear_sprites2:
                        self.change_sprites('fear2')
                if self.try_move(game.map):
                    self.move()
                else:
                    self.move_to_wall(game)
            else:
                teleport_coordinates = game.map.return_teleport_coordinates()
                self_coordinates = game.map.return_coordinates(self)
                if self_coordinates == teleport_coordinates:
                    self.rect.x, self.rect.y = self.starting_coordinates
                    self.released = False
                    self.time_to_release = DEATH_RELEASE_TIME
                    self.direction = DOWN
                    self.change_sprites('normal')
                else:
                    possible_directions = self.get_possible_directions(game.map)
                    self.direction = self.bfs(teleport_coordinates, game.map, possible_directions)
                    if self.try_move(game.map):
                        self.move()
                    else:
                        self.move_to_wall(game)
        else:
            self.speed = CHARACTER_SPEED
            if self.starting_time is None:
                self.starting_time = time()
            else:
                current_time = time()
                time_passed = current_time - self.starting_time
                if time_passed >= self.time_to_release:
                    if not self.alive:
                        self.already_died = True
                    self.alive = True
                    self.released = True
                    self.time_to_release = 0
                    self.starting_time = None
                    self.rect.x, self.rect.y = self.teleport_coordinates


def push_direction(coordinates, map_scheme, bfs_queue, used):
    i, j = coordinates
    if map_scheme[i][j] in [SEED, BIG_SEED, TELEPORT, EMPTY, PACMAN] and not used[i][j]:
        bfs_queue.put((i, j))


def push_available_directions(coordinates, map_scheme, bfs_queue, used):
    i, j = coordinates
    if j == 0:
        push_direction((i, j + 1), map_scheme, bfs_queue, used)
        if i != 0:
            push_direction((i - 1, j), map_scheme, bfs_queue, used)
        if i < len(map_scheme) - 1:
            push_direction((i + 1, j), map_scheme, bfs_queue, used)
    elif i == 0:
        push_direction((i + 1, j), map_scheme, bfs_queue, used)
        push_direction((i, j - 1), map_scheme, bfs_queue, used)
        if j < len(map_scheme[0]) - 1:
            push_direction((i, j + 1), map_scheme, bfs_queue, used)
    elif j == len(map_scheme[0]) - 1:
        push_direction((i, j - 1), map_scheme, bfs_queue, used)
        if i < len(map_scheme) - 1:
            push_direction((i + 1, j), map_scheme, bfs_queue, used)
        push_direction((i - 1, j), map_scheme, bfs_queue, used)
    elif i == len(map_scheme) - 1:
        push_direction((i, j - 1), map_scheme, bfs_queue, used)
        push_direction((i - 1, j), map_scheme, bfs_queue, used)
        push_direction((i, j + 1), map_scheme, bfs_queue, used)
    else:
        push_direction((i, j - 1), map_scheme, bfs_queue, used)
        push_direction((i, j + 1), map_scheme, bfs_queue, used)
        push_direction((i - 1, j), map_scheme, bfs_queue, used)
        push_direction((i + 1, j), map_scheme, bfs_queue, used)




