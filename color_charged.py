# color_charged
# -------
 
# PyMOL command to color protein molecules according pKI scale

# Amino acid scale: Normalized consensus hydrophobicity scale

# Amino acid scale values:
#
# Ala:  0.620
# Arg: -2.530
# Asn: -0.780
# Asp: -0.900
# Cys:  0.290
# Gln: -0.850
# Glu: -0.740
# Gly:  0.480
# His: -0.400
# Ile:  1.380
# Leu:  1.060
# Lys: -1.500
# Met:  0.640
# Phe:  1.190
# Pro:  0.120
# Ser: -0.180
# Thr: -0.050
# Trp:  0.810
# Tyr:  0.260
# Val:  1.080
#
# Usage:
# color_charged (selection)
#
from pymol import cmd
 
def color_charged(selection='all'):
        s = str(selection)
        print(s)
        cmd.set_color('color_ile',[0.899,0.969,0.969])
        cmd.set_color('color_phe',[0.899,0.969,0.969])
        cmd.set_color('color_val',[0.899,0.969,0.969])
        cmd.set_color('color_leu',[0.899,0.969,0.969])
        cmd.set_color('color_trp',[0.899,0.969,0.969])
        cmd.set_color('color_met',[0.899,0.969,0.969])
        cmd.set_color('color_ala',[0.899,0.969,0.969])
        cmd.set_color('color_gly',[0.899,0.969,0.969])
        cmd.set_color('color_cys',[0.899,0.969,0.969])
        cmd.set_color('color_tyr',[0.899,0.969,0.969])
        cmd.set_color('color_pro',[0.899,0.969,0.969])
        cmd.set_color('color_thr',[0.899,0.969,0.969])
        cmd.set_color('color_ser',[0.899,0.969,0.969])
        cmd.set_color('color_his',[0.980,0.539,0.539])
        cmd.set_color('color_glu',[0.156,0.156,0.992])
        cmd.set_color('color_asn',[0.899,0.969,0.969])
        cmd.set_color('color_gln',[0.899,0.969,0.969])
        cmd.set_color('color_asp',[0.062,0.062,0.996])
        cmd.set_color('color_lys',[0.992,0.156,0.156])
        cmd.set_color('color_arg',[0.996,0.062,0.062])
        cmd.color("color_ile","("+s+" and resn ile)")
        cmd.color("color_phe","("+s+" and resn phe)")
        cmd.color("color_val","("+s+" and resn val)")
        cmd.color("color_leu","("+s+" and resn leu)")
        cmd.color("color_trp","("+s+" and resn trp)")
        cmd.color("color_met","("+s+" and resn met)")
        cmd.color("color_ala","("+s+" and resn ala)")
        cmd.color("color_gly","("+s+" and resn gly)")
        cmd.color("color_cys","("+s+" and resn cys)")
        cmd.color("color_tyr","("+s+" and resn tyr)")
        cmd.color("color_pro","("+s+" and resn pro)")
        cmd.color("color_thr","("+s+" and resn thr)")
        cmd.color("color_ser","("+s+" and resn ser)")
        cmd.color("color_his","("+s+" and resn his)")
        cmd.color("color_glu","("+s+" and resn glu)")
        cmd.color("color_asn","("+s+" and resn asn)")
        cmd.color("color_gln","("+s+" and resn gln)")
        cmd.color("color_asp","("+s+" and resn asp)")
        cmd.color("color_lys","("+s+" and resn lys)")
        cmd.color("color_arg","("+s+" and resn arg)")
cmd.extend('color_charged',color_charged)


def color_charged2(selection='all'):
        s = str(selection)
        print(s)
        cmd.set_color('color_his',[0.980,0.539,0.539])
        cmd.set_color('color_glu',[0.156,0.156,0.992])
        cmd.set_color('color_asp',[0.062,0.062,0.996])
        cmd.set_color('color_lys',[0.992,0.156,0.156])
        cmd.set_color('color_arg',[0.996,0.062,0.062])
        cmd.color("color_his","("+s+" and resn his)")
        cmd.color("color_glu","("+s+" and resn glu)")
        cmd.color("color_asp","("+s+" and resn asp)")
        cmd.color("color_lys","("+s+" and resn lys)")
        cmd.color("color_arg","("+s+" and resn arg)")
cmd.extend('color_charged2',color_charged2)