import unittest
# import unittest. The unittest module provides a rich set of tools for constructing and running tests.
from main import Rover
# import Rover from main file. The methods in the rover class would be tested.

class TestRoverMethods(unittest.TestCase):

    def setUp(self):
        """
            This is just to set up the test class since
            we would be testing for more than one method here
            and the set up for the method are repetitive.
        """
        self.rover = Rover('5 5', '3 3 E')

    def test_check_position_of_rover_x(self):
        """
        Test to check if value passed in check_position_of_rover_in_x is equal to self.rover.positionX
        """
        sum_x = 3
        self.rover.check_position_of_rover_in_x(sum_x)
        self.assertEqual(self.rover.positionX, sum_x), "should be 3"

    def test_check_position_of_rover_y(self):
        """
        Test to check if value passed in check_position_of_rover_in_x is equal to self.rover.positionX
        """
        sum_y = 3
        self.rover.check_position_of_rover_in_y(sum_y)
        self.assertEqual(self.rover.positionX, sum_y), "should be 3"

    def test_check_position_of_rover_in_x_not_greater_than_plateau(self):
        """
        Test to check if the rover's throw an error when it falls on an unacceptable x position
        """
        sum_x = 6
        self.assertRaises(ValueError, self.rover.check_position_of_rover_in_x, sum_x), "should not be greater than 5"

    def test_check_position_of_rover_in_y_not_greater_than_plateau(self):
        """
        Test to check if the rover's throw an error when it falls on an unacceptable x position
        """
        sum_y = 6
        self.assertRaises(ValueError, self.rover.check_position_of_rover_in_x, sum_y), "should not be greater than 5"

    def test_rotate_90_left(self):
        """
        Test to check that the rotate_90_left method
        returns the accurate cardinal point
        """
        self.rover.rotate_90_left()
        self.assertEqual(self.rover.cardinalPoint, 'N'), "should be N"

    def test_rotate_90_right(self):
        """
        Test to check that the rotate_90_right method
        returns the accurate cardinal point
        """
        self.rover.rotate_90_right()
        self.assertEqual(self.rover.cardinalPoint, 'S'), "should be S"

    def test_move_forward(self):
        """
        Test to check that the move_forward method
        returns the accurate cardinal point
        """
        self.rover.move_forward()
        self.assertEqual(self.rover.positionX, 4), "should be 4"
        self.assertEqual(self.rover.positionY, 3), "should be 3"

    def test_start_moving(self):
        """
        Test to check if we get the correct coordinate point
        """
        self.rover.start_moving('M M R M M R M R R M')
        coordinate = "{} {} {}".format(self.rover.positionX, self.rover.positionY, self.rover.cardinalPoint)
        self.assertEqual(coordinate, "5 1 E"), "should be 5 1 E"
