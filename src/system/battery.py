import dataclasses

from src.globals import BATTERY_ALERT_THRESHOLD


@dataclasses.dataclass
class Battery:
    name: str = "Battery"
    max_capacity: float = 1000.0  # in Wh (1000 W per hour)
    charge_level: float = 1000.0
    status: str = "Battery is full"

    def set_status(self):
        if self.charge_level <= 0:
            self.status = "Battery is empty"
        elif self.charge_level >= self.max_capacity:
            self.status = "Battery is full"
        elif self.charge_level < BATTERY_ALERT_THRESHOLD:
            self.status = "Battery is running low"
        else:
            self.status = "No alert"

    def store_energy(self, energy):
        if self.charge_level + energy >= self.max_capacity:
            self.charge_level = self.max_capacity
        else:
            self.charge_level += energy
        self.set_status()

    def use_energy(self, energy):
        if self.charge_level - energy <= 0:
            self.charge_level = 0
        else:
            self.charge_level -= energy
        self.set_status()

    def get_storage(self):
        return self.charge_level
