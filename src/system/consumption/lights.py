import dataclasses
import datetime


@dataclasses.dataclass
class Lights:
    name: str = "Lights"
    consumption: int = 60
    number_of_lights: int = 5
    lights_on: datetime.time = datetime.time(hour=17, minute=30)
    lights_off: datetime.time = datetime.time(hour=23, minute=45)

    def get_consumption(self, time: datetime.time):
        if self.lights_on <= time <= self.lights_off:
            return self.consumption * self.number_of_lights
        return 0
