import dataclasses
import datetime

from src.globals import DAY_TEMPERATURE, NIGHT_TEMPERATURE


@dataclasses.dataclass
class Heating:
    name: str = "Heating"
    target_temperature: float = 20.0
    base_consumption: int = 200  # in W

    def get_consumption(self, time: datetime.time):
        # Calculate the temperature based on the time of day
        if datetime.time(8, 0) <= time < datetime.time(16, 50):
            current_temperature = DAY_TEMPERATURE
        else:
            current_temperature = NIGHT_TEMPERATURE

        # Consumption increases as difference between the two temperatures increases
        temperature_difference = self.target_temperature - current_temperature
        additional_consumption = temperature_difference**1.2 * 80
        consumption = self.base_consumption + additional_consumption
        return consumption
