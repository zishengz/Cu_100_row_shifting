
from gocia.ga.popGrandCanon import PopulationGrandCanonical
from gocia.hpc.slurm import SLURM
from time import sleep
import os
import datetime

import input

print(os.getpid())
nworker = 50
totConf = 1500
minConf = 1000

print('read in population')
pop = PopulationGrandCanonical(
    gadb='gcga.db',
    substrate='substrate.vasp',
    popSize = input.popSize,
    convergeCrit=input.popSize*10,
    subsPot = input.subsPot,
    chemPotDict = input.chemPotDict,
    zLim = input.zLim
    )

print('initializing queue')
queue = SLURM('zisheng')

pop.initializeDB()
pop.natural_selection()

kidnum = 0
while not pop.is_converged() or kidnum < minConf:
    while len(queue) < nworker:
        if 'STOP' in os.listdir():
            print('STOP REQUESTED')
            exit()
        if kidnum > totConf:
            print('MAX # SAMPLE REACHED')
            exit()
        kidnum += 1
        print('Job %i\t@%s'%\
            (kidnum, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        queue.submit('./perlmutter-vasp.sh %06d'%kidnum)
        sleep(10)
    sleep(60)
    queue.update()
    queue.write()

if pop.is_converged():
    print('CONVERGED!')
else:
    print('TERMINATED!')
