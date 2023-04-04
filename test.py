import unittest
from snake import Snake
from food import Food
import turtle


class TestSnake(unittest.TestCase):

    def setUp(self):
        self.screen = turtle.Screen()
        self.width = 600
        self.height = 600
        self.screen.setup(width=self.width, height=self.height)
        self.screen.bgcolor("black")
        self.screen.title("Python Snake")
        self.food = Food()
        self.snake_list = [(0, 0), (-20, 0), (-40, 0)]

    def test_update_snake(self):
        Snake(self.width, self.height, self.snake_list, self.food).update_snake((20, 0))
        self.assertEqual(len(self.snake_list), 4)

    def test_create_snake(self):
        self.assertEqual(len(Snake(self.width, self.height, [], self.food).create_snake()), 3)

    def tearDown(self):
        self.screen.bye()

if __name__ == '__main__':
    unittest.main()
