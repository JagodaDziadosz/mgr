# bond_color
 
# PyMOL command to display changes in proteins in the given order
# Usage:
# bond_color("bakterie", "bakterie2)
from pymol import cmd

def dist(*selection):
    chain_list = cmd.find_pairs("c. B", "c. C")
    print(chain_list)
cmd.extend('dist', dist)

def bond_color(*selection):
    output = open(f"{selection[0]}_resn_bond.txt", "w")

    output.write(f"organism,chain,loc,resn,oneletter,number_at,atom\n")
    chains = cmd.get_chains(selection[0])
    print(chains)
    chain_list = cmd.find_pairs(f"c. {chains[0]}", f"c. {chains[1]}")
    dict_atoms = {}

    for chain in chains:
        dict_atoms[f"{chain}_ch"] = []

    for pairs in chain_list:
        dict_atoms[f"{chains[0]}_ch"].append(pairs[0][1])
        dict_atoms[f"{chains[1]}_ch"].append(pairs[1][1])
    
#     print(dict_atoms)

    cmd.set_color(f'color_{chains[0]}',[0.010,0.010,1.000])
    cmd.set_color(f'color_{chains[1]}',[1.000,0.010,0.010])
    for chain in chains:
        sele = ""
        stored.list = []
        for atom in dict_atoms[f"{chain}_ch"]:
            cmd.color(f"color_{chain}",f"byres c. {chain} and rank {atom}")
            cmd.show("sticks", f"byres c. {chain} and rank {atom}")
            cmd.iterate(f"byres c. {chain} and rank {atom}","stored.list.append((resi,resn,oneletter,rank,name))")
            output.write(f"{selection[0]},{chain},{stored.list[-1][0]},{stored.list[-1][1]},{stored.list[-1][2]},{stored.list[-1][3]},{stored.list[-1][4]}\n")
            stored.list = []
            
    output.close()

cmd.extend('bond_color', bond_color)