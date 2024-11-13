import dataclasses

from src.system.consumption.refrigerator import Refrigerator


@dataclasses.dataclass
class EnergySystem:
    refrigerator = Refrigerator()

    def get_consumption(self):
        # calculate consumption of all devices
        return {f"{self.refrigerator.name}": self.refrigerator.get_consumption()}
