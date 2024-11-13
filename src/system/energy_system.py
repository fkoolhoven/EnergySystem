import dataclasses

from src.system.consumption.refrigerator import Refrigerator
from src.system.consumption.lights import Lights


@dataclasses.dataclass
class EnergySystem:
    refrigerator = Refrigerator()
    lights = Lights()

    def get_total_consumption(self, time):
        return {
            f"{self.refrigerator.name}": self.refrigerator.get_consumption(time),
            f"{self.lights.name}": self.lights.get_consumption(time),
        }
