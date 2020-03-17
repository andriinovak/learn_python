
import unittest
from car_2d import CarGame, drive_ten
import car_2d
from unittest.mock import MagicMock, patch


class TestDriveTen(unittest.TestCase):

    def test_drive_ten_right(self):
        with patch.method(car_2d.CarGame, "drive_right") as mock:
            drive_ten()
        mock.assert_called()
        # CarGame = MagicMock()
        # drive_ten()
        # MagicMock(CarGame.drive_right.assert_called())


class TestMyGame(unittest.TestCase):

    def setUpClass():
        TestMyGame.my_car = CarGame()

    def tearDown(self):
        self.my_car.position = {'x': 0, 'y': 0}

    def test_def_drive_left(self):
        self.my_car.drive_left(10, 1)
        result = self.my_car.position
        self.assertEqual(result, {'x': -10, 'y': 0})

    def test_def_drive_right(self):
        self.assertEqual(self.my_car.drive_rigth(20, 2), {'x': 40, 'y': 0})

    def test_def_drive_up(self):
        self.assertEqual(self.my_car.drive_up(30, 3), {'x': 0, 'y': 90})

    def test_def_drive_down(self):
        self.assertEqual(self.my_car.drive_down(40, 4), {'x': 0, 'y': -160})

    def test_for_type_error(self):
        with self.assertRaises(TypeError):
            self.my_car.drive_up('a', 'a')


if __name__ == "__main__":
    unittest.main()
