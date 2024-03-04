def main():
    elementsNames = ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr', 'Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra', 'Sc', 'Y', 'Ti', 'Zr', 'Hf', 'Rf', 'V', 'Nb', 'Ta', 'Db', 'Cr', 'Mo', 'W', 'Sg', 'Mn', 'Tc', 'Re', 'Bh', 'Fe', 'Ru', 'Os', 'Hs', 'Co', 'Rh', 'Ir', 'Mt', 'Ni', 'Pd', 'Pt', 'Ds', 'Cu', 'Ag', 'Au', 'Rg', 'Zn', 'Cd', 'Hg', 'Cn', 'B', 'Al', 'Ga', 'In', 'Tl', 'Uut', 'C', 'Si', 'Ge', 'Sn', 'Pb', 'Fl', 'N', 'P', 'As', 'Sb', 'Bi', 'Uup', 'O', 'S', 'Se', 'Te', 'Po', 'Lv', 'F', 'Cl', 'Br', 'I', 'At', 'Uus', 'He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn', 'Uuo', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']
    elementsMasses = [1.008, 6.941, 22.990, 39.098, 84.468, 132.905, 223.020, 9.012, 24.305, 40.078, 87.62, 137.328, 226.025, 44.956, 88.906, 47.88, 91.224, 178.49, 261, 50.942, 92.906, 180.948, 262, 51.996, 95.95, 183.84, 266, 54.938, 98.907, 186.207, 264, 55.845, 101.07, 190.23, 269, 58.933, 102.906, 192.217, 268, 58.693, 106.42, 195.085, 269, 63.546, 107.868, 196.967, 272, 65.38, 112.414, 200.592, 277, 10.811, 26.982, 69.723, 114.818, 204.383, -1, 12.011, 28.086, 72.631, 118.711, 207.2, 289, 14.007, 30.974, 74.922, 121.760, 208.980, -1, 15.999, 32.066, 78.971, 127.6, 208.982, 298, 18.998, 35.453, 79.904, 126.904, 209.987, -1, 4.003, 20.180, 39.948, 84.798, 131.249, 222.018, -1, 138.905, 140.116, 140.908, 144.243, 144.913, 150.36, 151.964, 157.25, 158.925, 162.500, 164.930, 167.259, 168.934, 173.055, 174.967, 227.028, 232.038, 231.036, 238.029, 237.048, 244.064, 243.061, 247.070, 247.070, 251.080, 254, 257.095, 258.1, 259.101, 262]
    calc = -1
    while True:
        for i in range(100):
            print('\n')
        print("Molar Mass Calculator\n")
        if calc == -1:
            print()
        elif calc == -2:
            print('one or more objects have an unknown mass')
        else:
            print(calc + 1)
        s = input('\ninput ex. BeCs2 ==>')
        savechar = ''
        savenum = ''
        calc = -1
        for i in s:
            if i.isupper():
                if savechar != '':
                    if savenum == '':
                        savenum = '1'
                    if elementsMasses[elementsNames.index(savechar)] == -1:
                        calc = -2
                        break
                    calc += elementsMasses[elementsNames.index(savechar)] * int(savenum)
                savechar = i
                savenum = ''
            else:
                if i.isdigit():
                    savenum += i
                else:
                    savechar += i
        if savechar != '':
            if savenum == '':
                savenum = '1'
            if elementsMasses[elementsNames.index(savechar)] == -1:
                calc = -2
                continue
            calc += elementsMasses[elementsNames.index(savechar)] * int(savenum)
main()
