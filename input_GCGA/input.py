
u_she = -0.5

popSize = 25

subsPot =  -428.2772

chemPotDict = {
    # E(H2,gas)/2 - ln(10)*k_B*T*pH - \delta(ZPE&TS) - eU
    'H': -6.9784/2 - 2.302585093*8.61733E-05 * 298.15 * 1 - 0.24 - u_she,
}

zLim = [13.5, 18.5]

pp_path='/global/homes/z/zisheng/Software/vasp_pot/potpaw_PBE'

# SLURM: NERSC-PERLMUTTER
vasp_cmd = 'time srun -n4 -c32 --cpu-bind=cores --gpu-bind=single:1 -G 4 vasp_gam > out'
