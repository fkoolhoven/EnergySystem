import dataclasses
import random
import math

from src.globals import MIN_WIND_SPEED, MAX_WIND_SPEED, MIN_AIR_DENSITY, MAX_AIR_DENSITY


@dataclasses.dataclass
class WindTurbine:
    name: str = "Wind Turbine"
    rotor_radius: float = 40.0

    def calculate_production(air_density, swept_area, wind_speed):
        return 0.5 * air_density * swept_area * wind_speed

    def get_production(self, time):
        # air density in kg/m^3
        air_density = random.randint(MIN_AIR_DENSITY, MAX_AIR_DENSITY)
        # wind speed in meters per second
        wind_speed = random.randint(MIN_WIND_SPEED, MAX_WIND_SPEED)
        # swept area in m^2
        swept_area = math.pi * self.rotor_radius**2
        return self.calculate_production(air_density, swept_area, wind_speed)
