import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船设置初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # 对于每艘飞船，都将其放置在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False

    def update(self):
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
