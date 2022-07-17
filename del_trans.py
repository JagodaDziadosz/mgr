# del_trans
 
# PyMOL command to delate transit peptyd
 
# Usage:
# # del_trans("Dwu_1_0",(56,180), "Bakterie",(5,134))

from pymol import cmd

def del_trans(*selection):

    for loc in range(0, len(selection)-1, 2):
        cmd.remove(f"{selection[loc]} and (not resi {selection[loc+1][0]}-{selection[loc+1][1]})")
cmd.extend('del_trans',del_trans)