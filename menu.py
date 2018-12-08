import pygame
from constants import BLACK, GREEN, BLUE, RED, MENU_HEIGHT, MENU_WIDTH, WHITE
from button import Button
from mainloop import Game

BUTTON_STYLE = {
    "hover_color": BLUE,
    "clicked_color": GREEN,
}

class Menu:

    def __init__(self):
        self.W = MENU_HEIGHT
        self.H = MENU_WIDTH
        self.screen = pygame.display.set_mode((self.W, self.H))
        self.gameover = False
        self.phase = 0
        pygame.font.init()
        self.my_font = pygame.font.Font('BebasNeueBold.ttf', 60)
        self.prepare()

    def prepare(self):

        self.start_button = Button((100, 0, 200, 100), RED, self.start_game, text="Начать игру", **BUTTON_STYLE)
        self.setting_button = Button((100, 100, 200, 100), RED, self.go_settings, text="Настройки", **BUTTON_STYLE)
        self.about_button = Button((100, 200, 200, 100), RED, self.go_about, text="О нас", **BUTTON_STYLE)
        self.exit_button = Button((100, 300, 200, 100), RED, self.go_exit, text="Выйти", **BUTTON_STYLE)
        self.go_backk = Button((0, 350, 100, 50), RED, self.go_back, text="Назад", **BUTTON_STYLE)

    def start_game(self):
        self.phase = 1

    def go_settings(self):
        self.phase = 2

    def go_about(self):
        self.phase = 3

    def go_exit(self):
        self.phase = 4

    def go_back(self):
        self.phase = 0

    def main_loop(self):
        while not self.gameover:
            self.process_events()
            self.process_logic()
            self.process_drawing()
            pygame.time.wait(10)

    def process_events(self):
        for event in pygame.event.get():  # цикл обработки событий
            if event.type == pygame.QUIT:  # проверка на событие выхода
                self.gameover = True


            elif self.phase == 0:
                self.start_button.check_event(event)
                self.setting_button.check_event(event)
                self.about_button.check_event(event)
                self.exit_button.check_event(event)

            elif self.phase == 2 or self.phase == 3:
                self.go_backk.check_event(event)

    def process_logic(self):
        if self.phase == 0:
            pass

    def process_drawing(self):
        self.screen.fill(BLACK)  # Заливка черным цветом

        if self.phase == 0:
            self.start_button.update(self.screen)
            self.setting_button.update(self.screen)
            self.about_button.update(self.screen)
            self.exit_button.update(self.screen)

        elif self.phase == 1:
            g = Game()
            g.main_loop()

        elif self.phase == 2:
            text = self.my_font.render('Настройки', False, BLUE)
            self.screen.blit(text, (100, 100))
            self.go_backk.update(self.screen)

        elif self.phase == 3:
            text = self.my_font.render('О нас', False, BLUE)
            self.screen.blit(text, (150, 100))
            self.go_backk.update(self.screen)

        elif self.phase == 4:
            self.gameover = True

        pygame.display.flip()