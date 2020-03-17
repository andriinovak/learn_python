
def drive_ten(up=False):
    my_car = CarGame()
    my_car.drive_rigth(10, 1)
    if up:
        my_car.drive_up(10, 1)


class CarGame:
    def __init__(self):
        self.position = {"x": 0, "y": 0}

    def drive_left(self, speed, time):
        self.position["x"] = self.position["x"] - speed * time
        # return self.position

    def drive_rigth(self, speed, time):
        self.position["x"] = self.position["x"] + speed * time
        return self.position

    def drive_up(self, speed, time):
        self.position["y"] = self.position["y"] + speed * time
        return self.position

    def drive_down(self, speed, time):
        self.position["y"] = self.position["y"] - speed * time
        return self.position
