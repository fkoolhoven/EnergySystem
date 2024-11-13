import datetime

from flask import Flask, request

from src.globals import API_ROOT
from src.system.energy_system import EnergySystem

app = Flask(__name__)
system = EnergySystem()


def get_time(request):
    time = request.args.get("time")
    if time:
        return datetime.datetime.strptime(time, "%H:%M").time()
    # Should check for bad request here
    return datetime.datetime.now().time()


@app.get(f"/{API_ROOT}/consumption")
def consumption():
    time = get_time(request)
    return system.get_consumption(time)


@app.get(f"/{API_ROOT}/production")
def production():
    time = get_time(request)
    return system.get_production(time)


@app.get(f"/{API_ROOT}/storage")
def storage():
    time = get_time(request)
    return system.get_storage(time)


@app.get(f"/{API_ROOT}/status")
def status():
    return system.get_status()


if __name__ == "__main__":
    app.run()
