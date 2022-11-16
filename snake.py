import arcade


class Snake:

    def __init__(self, x_pos=SCREEN_WIDTH/2, y_pos=SCREEN_HEIGHT/2, vel=3, size=15) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_change = 0
        self.y_change = 0
        self.size = size
        self.vel = vel
        self.direction =

    def draw(self):
        arcade.draw_point(self.x_pos, self.y_pos,
                          arcade.color.AMARANTH, self.size)

    def update(self):

        self.x_pos += self.x_change
        self.y_pos += self.y_change

    def change_direction(self):

        if
