class Seed:
    def __init__(self, coordinates):
        self.x, self.y = coordinates
        self.sprite = 0
        self.active = True
        self.rect = self.sprite.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y

    def draw(self, screen):
        if self.active:
            screen.blit(self.sprite, self.rect)