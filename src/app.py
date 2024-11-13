from flask import Flask

from src.globals import API_ROOT
from src.system.energy_system import EnergySystem

app = Flask(__name__)
system = EnergySystem()


@app.get(f"/{API_ROOT}/consumption")
def consumption():
    return system.get_consumption()


if __name__ == "__main__":
    app.run()
