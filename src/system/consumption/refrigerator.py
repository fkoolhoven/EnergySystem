import dataclasses


@dataclasses.dataclass
class Refrigerator:
    name: str = "Refrigerator"
    consumption: int = 350

    def get_consumption(self, time):
        return self.consumption
