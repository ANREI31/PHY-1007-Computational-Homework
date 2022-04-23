import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World


if __name__ == "__main__":
    world = World(shape=(73, 73))

    wires = [
        Wire(start=(11, 11), stop=(11, 62), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(11, 62), stop=(36, 62), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(36, 62), stop=(62, 62), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(62, 62), stop=(62, 11), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(62, 11), stop=(36, 11), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(36, 11), stop=(11, 11), current=Current(x=-1, y=0), voltage=4.5),

    ]

    circuit = Circuit(wires=wires)

    world.place(circuit)

    world.compute()

    world.show_wires_voltage( x_label="x [m]", y_label="y [m]", title="Initial Voltage [V]")
    world.show_potential(     x_label="x [m]", y_label="y [m]", title="Potential [V]")
    world.show_electric_field(x_label="x [m]", y_label="y [m]", title="Electrical field [N/C]")
    world.show_magnetic_field(x_label="x [m]", y_label="y [m]", title="Magnetic field [T]")
    world.show_energy_flux(   x_label="x [m]", y_label="y [m]", title="Energy flux [W/m^2]")
