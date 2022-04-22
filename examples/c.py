import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World


if __name__ == "__main__":
    world = World(shape=(146, 73))

    wires = [
        Wire(start=(11, 11), stop=(11, 62), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(11, 62), stop=(118, 62), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(118, 62), stop=(124, 62), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(124, 62), stop=(124, 11), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(124, 11), stop=(118, 11), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(118, 11), stop=(11, 11), current=Current(x=-1, y=0), voltage=4.5),
    ]

    circuit = Circuit(wires=wires)

    world.place(circuit)

    world.compute()

    world.show_all()
