import time
import car, controller

class World:
    name = ""
    b = 1000
    hertz = 0.005
    time = 0
    car = None
    controller = None
    complete = False

    def __init__(self, name):
        self.name = name
        self.car = car.Car()
        self.controller = \
            controller.Controller(self.car, self.b)
        
    def loop(self):
        while not self.complete:
            self.controller.run()
            self.time += self.hertz
            self.check_complete()
            #self.print_world()
            time.sleep(self.hertz)
        
    def print_world(self):
        print("NAME: {}, ERROR: {:.2f}, FORCE: {:.2f}, ACC: {:.2f}, SPEED: {:.2f}, POS: {:.2f}" \
            .format(self.name,
                    self.controller.last_errors[1],
                    self.car.force,
                    self.car.current_acceleration,
                    self.car.current_speed,
                    self.car.position))

    def check_complete(self):
        last_errors = self.controller.last_errors
        if (int(last_errors[0]) == 0 and int(last_errors[1]) == 0):
            self.complete = True
            print("COMPLETED IN: {}".format(self.time))
