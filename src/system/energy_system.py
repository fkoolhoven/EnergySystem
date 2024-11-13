import dataclasses
import datetime

from src.system.battery import Battery
from src.system.consumption.heating import Heating
from src.system.consumption.lights import Lights
from src.system.consumption.refrigerator import Refrigerator
from src.system.production.wind_turbine import WindTurbine


@dataclasses.dataclass
class EnergySystem:
    battery = Battery()
    wind_turbine = WindTurbine()
    refrigerator = Refrigerator()
    lights = Lights()
    heating = Heating()

    def convert_str_to_time(self, time):
        if time:
            return datetime.datetime.strptime(time, "%H:%M").time()
        return datetime.datetime.now().time()

    def get_consumption(self, time):
        return {
            f"{self.refrigerator.name}": self.refrigerator.get_consumption(time),
            f"{self.lights.name}": self.lights.get_consumption(time),
            f"{self.heating.name}": self.heating.get_consumption(time),
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
            f"{self.battery.name}": self.battery.get_storage(),
        }

    def get_status(self):
        return {
            "Status": self.battery.status,
        }

    def simulate_system(self, start_time: str = "00:00"):
        try:
            start_time = self.convert_str_to_time(start_time)
        except ValueError:
            start_time = datetime.datetime.now().time()
        time = start_time
        hours_simulated = 0
        while hours_simulated < 24:
            print(f"Time: {time}")
            print(self.get_storage(time))
            print(f"{self.get_status()}\n")
            time = time.replace(hour=(time.hour + 1) % 24)
            hours_simulated += 1
