
class Controller:

    car = None
    goal = None

    p_weight = 0.5
    i_weight = 0.01
    d_weight = 4.7

    last_errors = [0, 0] # error0, error1

    def __init__(self, car, b):
        print("controller created")
        self.car = car
        self.goal = b

    def run(self):
        car_pos = self.car.sense()
        error = self.goal - car_pos
        self.last_errors[0] = self.last_errors[1]
        self.last_errors[1] = error

        p_value = self.calc_p(error)
        i_value = self.calc_i()
        d_value = self.cald_d()

        force = self.normalize(p_value + i_value + d_value)

        self.car.drive(force)

    def calc_p(self, error):
        weight_error = error * self.p_weight
        return weight_error
    
    def calc_i(self):
        error = self.last_errors[1] + self.last_errors[0]
        weight_error = error * self.i_weight
        return weight_error

    def cald_d(self):
        error = self.last_errors[1] - self.last_errors[0]
        weight_error = error * self.d_weight
        return weight_error

    def normalize(self, value):
        force = value
        if (value > 100): force = 100
        elif (value < -100): force = -100
        return force
