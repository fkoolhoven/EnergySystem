### Getting Started
If you can't use Makefile, copy paste the commands from [the Makefile](https://github.com/fkoolhoven/EnergySystem/blob/master/Makefile) to the terminal.

To clone the repo:
```c
git clone https://github.com/fkoolhoven/EnergySystem.git
```
To install:
```c
make install
```

To run the app:
```c
make run
```
This will first run a 24 hour simulation of the energy system, before running the app. Simulation output is written to the stdout.

To run tests:
```c
make test
```

### Dependencies
- **Flask**: web framework to create the API
- **pytest**: testing framework
- **ruff**: formatter/linter - isn't strictly necessary to run the app but you can run ```make format``` to use it
- **setuptools**: to easily install the project
