# rmsd2
 
# PyMOL command to calculate rmsd similarities between the presented structures


# Usage:
# rmsd2("bakterie", "bakterie2", "zielenice")
from pymol import cmd

def rmsd2(*selection):
    s = str(selection)
    output = open("rmsd2.txt", "w")

    for loc1 in range(1, len(selection)):
        output.write(selection[loc1])
        output.write(":\t")
        data = cmd.align(selection[loc1], selection[0])
        output.write(str(data[0]))
        output.write("\n")
    output.close()
cmd.extend('rmsd2',rmsd2)