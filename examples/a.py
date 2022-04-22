import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World


if __name__ == "__main__":
    world = World(shape=(81, 81))

    wires = [
        Wire(start=(0, 0), stop=(0, 51), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(0, 51), stop=(25, 51), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(25, 51), stop=(51, 51), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(51, 51), stop=(51, 0), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(51, 0), stop=(25, 0), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(25, 0), stop=(0, 0), current=Current(x=-1, y=0), voltage=4.5),

    ]

    circuit = Circuit(wires=wires)

    world.place(circuit)

    world.compute()

    world.show_all()
