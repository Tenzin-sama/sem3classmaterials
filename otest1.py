# hexaval1 = hex(143)
# hexaval2 = hex(170)
# hexaval3 = hex(220)
# print(hexaval1,hexaval2,hexaval3)
# print(hex(143170220))
# print(hex(1))
""" """
"""
light blue: #dae3f3
blue: #507bc8
dark blue: #203864

light green: #c5e0b4
green: #5a8a26
dark green: #385723
button outline: #253917
"""
r, g, b = 32, 56, 100
hexaval = ""
colour = [r,g,b]
for i in colour:
    hexaval += str(hex(i))[2]+str(hex(i))[3]
print(hexaval)
""" Hex converter """
input()