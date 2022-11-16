import arcade
from snake import Snake

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVE_KEYS = [arcade.key.LEFT, arcade.key.RIGHT, arcade.key.UP, arcade.key.DOWN]


class GameWindow(arcade.Window):

    def __init__(self, width, height, title) -> None:

        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.snake = Snake(x_pos=300, y_pos=50)

    def on_draw(self) -> None:

        arcade.start_render()
        self.snake.draw()

    def update(self, delta_time: float):

        self.snake.update()

    def on_key_press(self, key: int, modifiers: int):

        if key in MOVE_KEYS:
            self.snake.change_direction(key)
        if key == arcade.key.LEFT:
            self.snake.y_change = 0
            self.snake.x_change = -1 * self.snake.vel
        elif key == arcade.key.RIGHT:
            self.snake.y_change = 0
            self.snake.x_change = self.snake.vel
        elif key == arcade.key.UP:
            print('up')
            self.snake.x_change = 0
            self.snake.y_change = self.snake.vel
        elif key == arcade.key.DOWN:
            print('down')
            self.snake.x_change = 0
            self.snake.y_change = -1 * self.snake.vel
        elif key == arcade.key.P:
            print('PPPPPP')


def main():

    game_window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Snake boi")
    game_window.run()


if __name__ == '__main__':
    main()
