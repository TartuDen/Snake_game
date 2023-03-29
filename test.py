

import turtle
import unittest
from main import create_snake, move_forward

class TestSnakeGame(unittest.TestCase):
    
    def test_create_snake(self):
        # Test creating a snake of length 3
        snake = create_snake(3)
        self.assertEqual(len(snake), 3)
        
        # Test creating a snake of length 5
        snake = create_snake(5)
        self.assertEqual(len(snake), 5)
    
    def test_move_forward(self):
        # Test moving the snake forward
        move_forward()
        pos_list = [s.position() for s in snake]
        self.assertEqual(pos_list[0], (20, 0))
        self.assertEqual(pos_list[1], (0, 0))
        self.assertEqual(pos_list[2], (-20, 0))
    
if __name__ == '__main__':
    screen=turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Python Snake")
    turtle.listen()

    snake=create_snake()

    turtle.onkey(move_forward, "Right")

    unittest.main(exit=False)
    
    screen.exitonclick()
