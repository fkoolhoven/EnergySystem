import dataclasses

from src.system.battery import Battery
from src.system.consumption.lights import Lights
from src.system.consumption.refrigerator import Refrigerator
from src.system.production.wind_turbine import WindTurbine


@dataclasses.dataclass
class EnergySystem:
    refrigerator = Refrigerator()
    lights = Lights()
    wind_turbine = WindTurbine()
    battery = Battery()

    def get_total_consumption(self, time):
        return {
            f"{self.refrigerator.name}": self.refrigerator.get_consumption(time),
            f"{self.lights.name}": self.lights.get_consumption(time),
        }

    def get_total_production(self, time):
        return {
            f"{self.wind_turbine.name}": self.wind_turbine.get_production(time),
        }

    def get_total_storage(self, time):
        return {
            f"{self.battery.name}": self.battery.get_storage(time),
        }
