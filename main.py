"""
The Rover class handles everything concerning the rover.
Meaning it handles the initialization of new rovers.

A rover is initialized with two integers (its x- and y-values)
a direction (N, E, S, W) and what plateau coordinate.

The reason I added Plateau_position to the initialization is mainly to check that the
rover does not move out of the cardinal point of the plateau where i assumed that (5, 5) -- (x, y).

since the rover can  move up and left and right I added the function to perform this movement,
also the check_position method which checks that the rover does not go outside the plateau,
and the start_moving function which takes in the command which the rover would move with.
"""

class Rover:
    """
    Creates a Rover-object.
    """
    def __init__(self, plateau_position, location):
        """
        Initialize a rover
        """
        self.positionX = list(map(int, location.split()[0]))[0]
        self.positionY = list(map(int, location.split()[1]))[0]
        self.cardinalPoint = location.split()[2].upper()
        self.plateauX = list(map(int, plateau_position.split()[0]))[0]
        self.plateauY = list(map(int, plateau_position.split()[1]))[0]

    def check_position_of_rover_in_x(self, x):
        """
        Checks if positionX is within acceptable
        bounds (higher than 0 and lower than
        Plateau surface)
        """
        if x < 0 or x > self.plateauX:
            raise ValueError("The rover's x-value is out of bounds. it"
                             "should fall between 0 and {}".format(self.plateauX))
        self.positionX = x

    def check_position_of_rover_in_y(self, y):
        """
        Checks if positionY is within acceptable
        bounds (higher than 0 and lower than
        Plateau surface)
        """
        if y < 0 or y > self.plateauY:
            raise ValueError("The rover's y-value is out of bounds. it"
                             "should fall between 0 and {}".format(self.plateauY))
        self.positionY = y

    def rotate_90_left(self):
        """
        Checks the position of the cardinal point and make
        it turn left 90 degree
        """
        if self.cardinalPoint == 'N':
            self.cardinalPoint = 'W'
        elif self.cardinalPoint == 'W':
            self.cardinalPoint = 'S'
        elif self.cardinalPoint == 'S':
            self.cardinalPoint = 'E'
        elif self.cardinalPoint == 'E':
            self.cardinalPoint = 'N'
        else:
            raise ValueError("ValueError: Invalid cardinal point choices are N W S E")

    def rotate_90_right(self):
        """
        Checks the position of the cardinal point and make
        it turn right 90 degree
        """
        if self.cardinalPoint == 'N':
            self.cardinalPoint = 'E'
        elif self.cardinalPoint == 'E':
            self.cardinalPoint = 'S'
        elif self.cardinalPoint == 'S':
            self.cardinalPoint = 'W'
        elif self.cardinalPoint == 'W':
            self.cardinalPoint = 'N'
        else:
            raise ValueError("ValueError: Invalid cardinal point choices are N W S E")

    def move_forward(self):
        """
        Checks the position of the cardinal points and move it by 1
        """
        if self.cardinalPoint == 'N':
            sum_y = self.positionY + 1
            self.check_position_of_rover_in_y(sum_y)

        elif self.cardinalPoint == "E":
            sum_x = self.positionX + 1
            self.check_position_of_rover_in_x(sum_x)

        elif self.cardinalPoint == "S":
            sum_y = self.positionY - 1
            self.check_position_of_rover_in_y(sum_y)

        elif self.cardinalPoint == "W":
            sum_x = self.positionX - 1
            self.check_position_of_rover_in_x(sum_x)

        else:
            raise ValueError("ValueError: Invalid cardinal point choices are N W S E")

    def start_moving(self, move_command):
        """
        This checks the command (l, r, m) if otherwise throws and error and
        performs the appropriate action depending on the command
        :param move_command: this is the command giving to the rover

        """
        commands = list(move_command.split())
        for command in commands:
            if command.upper() == 'L':
                self.rotate_90_left()
            elif command.upper() == 'R':
                self.rotate_90_right()
            elif command.upper() == 'M':
                self.move_forward()
            else:
                raise ValueError("ValueError: Invalid cardinal point choices are L R M")


if __name__ == '__main__':
    rover = Rover('5 5', '3 3 E')
    rover.start_moving("M M R M M R M R R M")
    print(rover.positionX, rover.positionY, rover.cardinalPoint)



