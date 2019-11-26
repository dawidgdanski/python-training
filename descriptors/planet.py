from weakref import WeakKeyDictionary


class Positive:
    def __init__(self) -> None:
        self._instance_data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self._instance_data[instance]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f'Value {value} is not positive')
        print(f"SETTING VALUE {value}")
        self._instance_data[instance] = value

    def __delete__(self, instance):
        raise AttributeError('Cannot delete attribute')


class Planet:
    def __init__(self, name, radius_metres, mass_kilograms, orbital_period_seconds, surface_temperature_kelvin):
        self.name = name
        self.radius_metres = radius_metres
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    radius_meters = Positive()
    mass_kilograms = Positive()
    orbital_period_seconds = Positive()
    surface_temperature_kelvin = Positive()


if __name__ == "__main__":
    planet = Planet(name="Pluto", radius_metres=123, mass_kilograms=234,
                    orbital_period_seconds=1239324,
                    surface_temperature_kelvin=34)
    planet2 = Planet(name="Pluto", radius_metres=0, mass_kilograms=234,
                     orbital_period_seconds=1239324,
                     surface_temperature_kelvin=34)
    value = 23
    planet.radius_meters = value
    print(planet.radius_meters)
