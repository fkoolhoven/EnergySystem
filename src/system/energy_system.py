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

    def get_consumption(self, time):
        return {
            f"{self.refrigerator.name}": self.refrigerator.get_consumption(time),
            f"{self.lights.name}": self.lights.get_consumption(time),
        }

    def get_production(self, time):
        return {
            f"{self.wind_turbine.name}": self.wind_turbine.get_production(time),
        }

    def update_energy_storage(self, time):
        production = self.get_production(time)
        consumption = self.get_consumption(time)
        total_production = sum(production.values())
        total_consumption = sum(consumption.values())
        if total_production > total_consumption:
            self.battery.store_energy(total_production - total_consumption)
        else:
            self.battery.use_energy(total_consumption - total_production)

    def get_storage(self, time):
        self.update_energy_storage(time)
        return {
            f"{self.battery.name}": self.battery.get_storage(time),
        }

    def get_status(self):
        return self.battery.status
