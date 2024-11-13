import dataclasses

from src.globals import BATTERY_ALERT_THRESHOLD

@dataclasses.dataclass
class Battery:
    name: str = "Battery"
    # max capacity in Wh (1000 W per hour)
    max_capacity: float = 1000.0
    charge_level: float = 1000.0
    alert: str = "Battery is full"

    def store_energy(self, energy):
        if self.charge_level + energy > self.max_capacity:
            self.charge_level = self.max_capacity
            self.alert = "Battery is full"
        else:
            self.charge_level += energy
            if self.charge_level >= BATTERY_ALERT_THRESHOLD:
                self.alert = "No alert"

    def use_energy(self, energy):
        if self.charge_level - energy < 0:
            self.charge_level = 0
            self.alert = "Battery is empty"
        else:
            self.charge_level -= energy
            if self.charge_level < BATTERY_ALERT_THRESHOLD:
                self.alert = "Battery is running low"

    def get_storage(self, time):
        return self.charge_level