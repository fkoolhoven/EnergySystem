from flask import Flask, request

from src.globals import API_ROOT
from src.system.energy_system import EnergySystem

app = Flask(__name__)
system = EnergySystem()


@app.get(f"/{API_ROOT}/consumption")
def consumption():
    time = system.convert_str_to_time(request.args.get("time"))
    return system.get_consumption(time)


@app.get(f"/{API_ROOT}/production")
def production():
    time = system.convert_str_to_time(request.args.get("time"))
    return system.get_production(time)


@app.get(f"/{API_ROOT}/storage")
def storage():
    time = system.convert_str_to_time(request.args.get("time"))
    return system.get_storage(time)


@app.get(f"/{API_ROOT}/status")
def status():
    return system.get_status()


if __name__ == "__main__":
    system.simulate_system()
    app.run()
