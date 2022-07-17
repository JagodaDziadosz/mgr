# rmsd
# -------
 
# PyMOL comand for calculating the rmsd similarity matrix between the presented structures

# Usage:
# rmsd("bakterie", "bakterie2", "zielenice")
from pymol import cmd

def rmsd(*selection):
    s = str(selection)
    cmd.hide("cartoon", "all")
    output = open("rmsd.txt", "w")

    for loc in range(0, len(selection)):
        if loc == len(selection) - 1:
            output.write(selection[loc])
        else:
            output.write(selection[loc])
            output.write(",")
    output.write("\n")

    for loc1 in range(0, len(selection)):

        output.write(selection[loc1])
        output.write(",")
        for loc2 in range(0, len(selection)):
            if loc2 == len(selection)-1:
                if loc1 == loc2:
                    output.write("0")
                else:
                    data = cmd.align(selection[loc1], selection[loc2])
                    output.write(str(data[0]))
            else:
                if loc1 == loc2:
                    output.write("0")
                    output.write(",")
                else:
                    data = cmd.align(selection[loc1], selection[loc2])
                    output.write(str(data[0]))
                    output.write(",")
        output.write("\n")
    output.close()
cmd.extend('rmsd',rmsd)
