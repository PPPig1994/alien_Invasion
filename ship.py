import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        # ai_game是指向当前的AlienInvasion实例
        """初始化飞船设置初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # 对于每艘飞船，都将其放置在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        # 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.x += 1
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            # self.rect.x -= 1
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
