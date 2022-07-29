# INITIAL WORKER SCRIPT FOR
# GCGA with Surface Charging

from gocia.utils.vasp import pos2pot, do_multiStep_opt, do_surfChrg_batch, get_parabola
from gocia.geom.build import get_sym_mirror
from ase.io import read, write
import os
import numpy as np
import input

# VASP INPUT PREPARATION
pos2pot(input.pp_path)
os.system('cp POSCAR inp.vasp')
os.system('cp ../KPOINTS .')

# SURFACE CHARGING CALCULATION
delta_NELECT = [-1, -0.5, 0, +0.5, 1]
slab_sym = get_sym_mirror(read('POSCAR'),  9.3073649327149877, 60)
write('POSCAR', slab_sym)
do_surfChrg_batch(input.pp_path, delta_NELECT, input.vasp_cmd)
if len(np.loadtxt('./sc.dat')) == len(delta_NELECT):
    get_parabola()
else:
    exit()
