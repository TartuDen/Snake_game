import unittest
from main import create_snake, update_snake
import turtle


class TestSnake(unittest.TestCase):

    def setUp(self):
        self.screen = turtle.Screen()
        self.width = 600
        self.height = 600
        self.screen.setup(width=self.width, height=self.height)
        self.screen.bgcolor("black")

    def test_create_snake(self):
        snake_list = create_snake(length=3)
        self.assertEqual(len(snake_list), 3)
        for turtle_ in snake_list:
            self.assertEqual(turtle_.color()[0], "white")

    def test_update_snake(self):
        start_pos = (-20, 0)
        snake_list = create_snake(length=3)
        update_snake(snake_list, start_pos)
        self.assertEqual(len(snake_list), 4)
        self.assertEqual(snake_list[-1].position(), start_pos)
        self.assertEqual(snake_list[-1].color()[0], "white")

    def tearDown(self):
        self.screen.bye()


if __name__ == '__main__':
    unittest.main()
