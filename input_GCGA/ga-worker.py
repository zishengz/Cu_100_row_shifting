from gocia.ga.popGrandCanon import PopulationGrandCanonical
from gocia.utils.vasp import pos2pot, do_multiStep_opt
import os
import numpy as np
import input

from random import randint

pop = PopulationGrandCanonical(
    gadb='../gcga.db',
    substrate='../substrate.vasp',
    popSize = input.popSize,
    subsPot = input.subsPot,
    chemPotDict = input.chemPotDict,
    zLim = input.zLim
    )

# Child Generation
kid = None
while kid is None:
    kid = pop.gen_offspring_box(
        mutRate=0.3,
        xyzLims=np.array([[0,15.336],[0,15.336],[13.5,18.5]]),
        bondRejList = [['H','H']],
        constrainTop=False,
         permuteOn=True,
         transOn=True,
         transVec=[[-2,2,-3,3,-6,6],[-2,2,-3,3,-6,6]]
        )
kid.preopt_hooke(cutoff=1.2, toler=0.1)
kid.print()
kid.write('POSCAR')

# VASP INPUT PREPARATION
pos2pot(input.pp_path)
os.system('cp POSCAR inp.vasp')
os.system('cp ../KPOINTS .')

# VASP CALCULATIONS
do_multiStep_opt(3, input.vasp_cmd, input.zLim)

# ADD DATA& ClEAN UP
pop.add_vaspResult()
pop.natural_selection()


