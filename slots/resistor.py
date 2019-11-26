from sys import getsizeof


class Resistor:

    __slots__ = ("power_watts", "tolerance_percent", "resistance_ohms")

    def __init__(self, resistance_ohms, tolerance_percent, power_watts):
        self.power_watts = power_watts
        self.tolerance_percent = tolerance_percent
        self.resistance_ohms = resistance_ohms


if __name__ == "__main__":
    resistor = Resistor(1, 0.5, 23)
    print(getsizeof(resistor))
