# movie_alignment
# -------
 
# PyMOL command to display changes in proteins in the given order
 
#
# Usage:
# movie_alignment (selection)
#
from pymol import cmd


def movie_alignment(*selection):
    s = str(selection)
    print(s)
    cmd.hide("cartoon", "all")
    scene_numbers = len(selection)*60
    cmd.mset('1x'+str(scene_numbers))
    for loc in range(1, len(selection)+1):
        cmd.hide("surface", "all")
        cmd.show("surface", selection[loc-1])
        cmd.scene(str(loc), "store")
        cmd.turn("y", 60)
        cmd.scene(str(loc) + ".5", "store")
        if loc < len(selection):
            cmd.show("surface", selection[loc])
            cmd.align(selection[loc], selection[loc-1])
            cmd.turn("y", 60)
            cmd.scene(str(loc) + ".9", "store")
    
    for loc in range(1, len(selection)+1):
        cmd.mview(action='store', first=loc*60-59, scene=str(loc))
        cmd.mview(action='store', first=loc*60 - 30, scene=str(loc) + ".5")
        if loc < len(selection):
            cmd.mview(action='store', first=loc*600, scene=str(loc) + ".9")
    cmd.mplay()
cmd.extend('movie_alignment',movie_alignment)