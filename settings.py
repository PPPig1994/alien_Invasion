class Settings:
    def __init__(self):
        # 游戏屏幕设置
        self.screen_width = 960
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # 飞船速度设置
        self.ship_speed = 1.5
        # 子弹设置,创建3像素，高15像素的深灰色子弹
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
