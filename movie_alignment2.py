# movie_alignment2
# -------
 
# PyMOL command to display changes in proteins in the given order
 
#
# Usage:
# movie_alignment2("bakterie", "bakterie2", "zielenice")

from pymol import cmd

def movie_alignment2(*selection):
    s = str(selection)
    print(s)
    cmd.hide("cartoon", "all")
    scene_numbers = len(selection)*30
    cmd.mset('1x'+str(scene_numbers))
    for loc in range(1, len(selection)+1):
        if loc < len(selection):
            cmd.align(selection[loc], selection[loc-1])

    radius = 0
    for loc in range(1, len(selection)+1):
        cmd.hide("surface", "all")
        cmd.show("surface", selection[loc-1])
        cmd.scene(str(loc) + ".1", "store")
        radius += 30

        cmd.rotate('y', 10)
        cmd.scene(str(loc) + ".2", "store")

    for loc in range(1, len(selection)+1):
        cmd.mview(action='store', first=loc*30-29, scene=str(loc) + ".1")
        cmd.mview(action='store', first=loc*30, scene=str(loc) + ".2")
    cmd.mplay()
cmd.extend('movie_alignment2',movie_alignment2)