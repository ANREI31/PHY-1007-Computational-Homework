import numpy as np
from scipy.constants import mu_0, pi

from src.fields import VectorField

import time
import warnings


class BiotSavartEquationSolver:
    """
    A Biot–Savart law solver used to compute the resultant magnetic field B in 2D-space generated by a constant current
    field I (for example due to wires).
    """

    def solve(self, electric_current: VectorField) -> VectorField:
        """
        Solve the Biot–Savart equation to compute the magnetic field given an electric current field.

        Parameters
        ----------
        electric_current : VectorField
            A vector field I : ℝ² → ℝ³ ; (x, y) → (I_x(x, y), I_y(x, y), I_z(x, y)), where I_x(x, y), I_y(x, y) and
            I_z(x, y) are the 3 components of the electric current vector at a given point (x, y) in space. Note that
            I_z = 0 is always True in our 2D world.

        Returns
        -------
        magnetic_field : VectorField
            A vector field B : ℝ² → ℝ³ ; (x, y) → (B_x(x, y), B_y(x, y), B_z(x, y)), where B_x(x, y), B_y(x, y) and
            B_z(x, y) are the 3 components of the magnetic vector at a given point (x, y) in space. Note that
            B_x = B_y = 0 is always True in our 2D world.
        """

        u0 = 1e-7 # u0/4pi
        n, m, _ = electric_current.shape

        magnetic_field = np.zeros(electric_current.shape)

        indices_i, indices_j = np.indices((n, m))

        for i in range(n):
            for j in range(m):
                if electric_current[i, j].any(): # On dit qu'il n'y pas de champ magnétique dans les fils
                    continue

                r = np.stack([-indices_i+i, -indices_j+j, np.zeros((n, m))], axis=2)
                rnorm = np.sqrt(np.sum(np.square(r), axis=2))

                with warnings.catch_warnings(): # Pour pas que Numpy nous fasse chier avec ses RuntimeWarning
                    warnings.simplefilter("ignore")
                    rhat = r/rnorm[:, :, None]
                    bmatrix = np.cross(electric_current, rhat, axis=2)/np.square(rnorm)[:, :, None]

                bmatrix[np.isnan(bmatrix)] = 0
                magnetic_field[i, j] = np.sum(bmatrix, axis=(0, 1))*u0

        return VectorField(magnetic_field)
