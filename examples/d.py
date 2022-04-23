import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World


if __name__ == "__main__":
    world = World(shape=(101, 101))

    wires = [
        Wire(start=(51, 6), stop=(56, 6), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(56, 6), stop=(56, 11), current=Current(x=0, y=1), voltage=-4.5),
        Wire(start=(56, 11), stop=(71, 11), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(71, 11), stop=(71, 16), current=Current(x=0, y=1), voltage=-4.5),
        Wire(start=(71, 16), stop=(76, 16), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(76, 16), stop=(76, 21), current=Current(x=0, y=1), voltage=-4.5),
        Wire(start=(76, 21), stop=(81, 21), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(81, 21), stop=(81, 31), current=Current(x=0, y=1), voltage=-4.5),
        Wire(start=(81, 31), stop=(66, 31), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(66, 31), stop=(66, 26), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(66, 26), stop=(61, 26), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(61, 26), stop=(61, 21), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(61, 21), stop=(56, 21), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(56, 21), stop=(56, 41), current=Current(x=0, y=1), voltage=-4.5),
        #Début Milieu
        Wire(start=(56, 41), stop=(61, 41), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(61, 41), stop=(61, 46), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(61, 46), stop=(66, 46), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(66, 46), stop=(66, 51), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(66, 51), stop=(71, 51), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(71, 51), stop=(71, 56), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(71, 56), stop=(76, 56), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(76, 56), stop=(76, 76), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(76, 76), stop=(71, 76), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(71, 76), stop=(71, 81), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(71, 81), stop=(66, 81), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(66, 81), stop=(66, 86), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(66, 86), stop=(61, 86), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(61, 86), stop=(61, 91), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(61, 91), stop=(41, 91), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(41, 91), stop=(41, 86), current=Current(x=0, y=-1), voltage=4.5),
        Wire(start=(41, 86), stop=(36, 86), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(36, 86), stop=(36, 81), current=Current(x=0, y=-1), voltage=4.5),
        Wire(start=(36, 81), stop=(31, 81), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(31, 81), stop=(31, 76), current=Current(x=0, y=-1), voltage=4.5),
        Wire(start=(31, 76), stop=(26, 76), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(26, 76), stop=(26, 56), current=Current(x=0, y=-1), voltage=4.5),
        Wire(start=(26, 56), stop=(31, 56), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(31, 56), stop=(31, 51), current=Current(x=0, y=-1), voltage=4.5),
        Wire(start=(31, 51), stop=(36, 51), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(36, 51), stop=(36, 46), current=Current(x=0, y=-1), voltage=4.5),
        Wire(start=(36, 46), stop=(41, 46), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(41, 46), stop=(41, 41), current=Current(x=0, y=-1), voltage=4.5),
        Wire(start=(41, 41), stop=(46, 41), current=Current(x=1, y=0), voltage=4.5),
        #Fin milieu
        Wire(start=(46, 41), stop=(46, 31), current=Current(x=0, y=-1), voltage=1),
        #Début feuille
        Wire(start=(46, 31), stop=(36, 31), current=Current(x=-1, y=0), voltage=1),
        Wire(start=(36, 31), stop=(36, 36), current=Current(x=0, y=1), voltage=1),
        Wire(start=(36, 36), stop=(31, 36), current=Current(x=-1, y=0), voltage=1),
        Wire(start=(31, 36), stop=(31, 41), current=Current(x=0, y=1), voltage=1),
        Wire(start=(31, 41), stop=(16, 41), current=Current(x=-1, y=0), voltage=1),
        Wire(start=(16, 41), stop=(16, 31), current=Current(x=0, y=-1), voltage=1),
        Wire(start=(16, 31), stop=(21, 31), current=Current(x=1, y=0), voltage=1),
        Wire(start=(21, 31), stop=(21, 26), current=Current(x=0, y=-1), voltage=1),
        Wire(start=(21, 26), stop=(26, 26), current=Current(x=1, y=0), voltage=1),
        Wire(start=(26, 26), stop=(26, 21), current=Current(x=0, y=-1), voltage=1),
        Wire(start=(26, 21), stop=(46, 21), current=Current(x=1, y=0), voltage=1),
        #Fin feuille
        Wire(start=(46, 21), stop=(46, 6), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(46, 6), stop=(51, 6), current=Current(x=1, y=0), voltage=-4.5),
    ]   

    circuit = Circuit(wires=wires)

    world.place(circuit)

    world.compute()

    world.show_all()

"""
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    def get_world_t(t, abs_u=4.5):
        world = World(shape=(73, 73))

        v = abs_u*np.cos(t)
        i = abs_u*np.sin(t)

        wires = [
            Wire(start=(11, 11), stop=(11, 62), current=Current(x=0, y=i), voltage=v),
            Wire(start=(11, 62), stop=(36, 62), current=Current(x=i, y=0), voltage=v),
            Wire(start=(36, 62), stop=(62, 62), current=Current(x=i, y=0), voltage=-v),
            Wire(start=(62, 62), stop=(62, 11), current=Current(x=0, y=-i), voltage=-v),
            Wire(start=(62, 11), stop=(36, 11), current=Current(x=-i, y=0), voltage=-v),
            Wire(start=(36, 11), stop=(11, 11), current=Current(x=-i, y=0), voltage=v),
        ]

        circuit = Circuit(wires=wires)

        world.place(circuit)

        world.compute()

        return world
    
    for i in np.linspace(0, 2*np.pi, 20):
        w = get_world_t(i)
        w.show_wires_voltage(clim=(-4.5, 4.5), filename='img/voltage/'+f"{i}.png")
        w.show_potential(clim=(-4.5, 4.5), filename='img/potential/'+f"{i}.png")
        w.show_electric_field(clim=(0, 3.1), filename='img/electric/'+f"{i}.png")
        w.show_magnetic_field(clim=(-4e-7, 4e-7), filename='img/magnetic/'+f"{i}.png")
        w.show_energy_flux(clim=(0, 4), filename='img/energy/'+f"{i}.png")
"""
