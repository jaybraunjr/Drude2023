# Step 2: Read "save.psf"
with open('save.psf', 'r') as file:
    save_psf_lines = file.readlines()

# Step 3: Update "save.psf"
for i, line in enumerate(save_psf_lines):
    if line.strip() and line[0].isdigit():
        parts = line.split()
        if len(parts) > 5:
            atom_name = parts[4]
            correct_atom_type = trio_psf_dict.get(atom_name, parts[5])  # Use existing type if not found in the dictionary
            # Reconstructing the line with the correct atom type, preserving formatting
            updated_line = f"{parts[0]:>10s} {parts[1]:>4s} {parts[2]:>4s} {parts[3]:>8s} {parts[4]:>8s} {correct_atom_type:<8s} {parts[6]:>12s} {parts[7]:>12s}\n"
            save_psf_lines[i] = updated_line

# Step 4: Write the Updated "save.psf"
with open('corrected_save.psf', 'w') as file:
    file.writelines(save_psf_lines)

# Processing the provided snippet of "trio.psf" to create a dictionary mapping atom names to atom types
trio_psf_snippet = """
         1 SYS      1        TRIO     C118     CTL3    -0.270000       12.0110           
         2 SYS      1        TRIO     H18A     HAL3     0.090000        1.0080           
         3 SYS      1        TRIO     H18B     HAL3     0.090000        1.0080           
         4 SYS      1        TRIO     H18C     HAL3     0.090000        1.0080           
         5 SYS      1        TRIO     C117     CTL2    -0.180000       12.0110           
         6 SYS      1        TRIO     H17A     HAL2     0.090000        1.0080           
         7 SYS      1        TRIO     H17B     HAL2     0.090000        1.0080           
         8 SYS      1        TRIO     C116     CTL2    -0.180000       12.0110           
         9 SYS      1        TRIO     H16A     HAL2     0.090000        1.0080           
        10 SYS      1        TRIO     H16B     HAL2     0.090000        1.0080           
        11 SYS      1        TRIO     C115     CTL2    -0.180000       12.0110           
        12 SYS      1        TRIO     H15A     HAL2     0.090000        1.0080           
        13 SYS      1        TRIO     H15B     HAL2     0.090000        1.0080           
        14 SYS      1        TRIO     C114     CTL2    -0.180000       12.0110           
        15 SYS      1        TRIO     H14A     HAL2     0.090000        1.0080           
        16 SYS      1        TRIO     H14B     HAL2     0.090000        1.0080           
        17 SYS      1        TRIO     C113     CTL2    -0.180000       12.0110           
        18 SYS      1        TRIO     H13A     HAL2     0.090000        1.0080           
        19 SYS      1        TRIO     H13B     HAL2     0.090000        1.0080           
        20 SYS      1        TRIO     C112     CTL2    -0.180000       12.0110           
        21 SYS      1        TRIO     H12A     HAL2     0.090000        1.0080           
        22 SYS      1        TRIO     H12B     HAL2     0.090000        1.0080           
        23 SYS      1        TRIO     C111     CTL2    -0.180000       12.0110           
        24 SYS      1        TRIO     H11A     HAL2     0.090000        1.0080           
        25 SYS      1        TRIO     H11B     HAL2     0.090000        1.0080           
        26 SYS      1        TRIO     C110     CEL1    -0.150000       12.0110           
        27 SYS      1        TRIO     H10A     HEL1     0.150000        1.0080           
        28 SYS      1        TRIO     C19      CEL1    -0.150000       12.0110           
        29 SYS      1        TRIO     H9A      HEL1     0.150000        1.0080           
        30 SYS      1        TRIO     C18      CTL2    -0.180000       12.0110           
        31 SYS      1        TRIO     H8A      HAL2     0.090000        1.0080           
        32 SYS      1        TRIO     H8B      HAL2     0.090000        1.0080           
        33 SYS      1        TRIO     C17      CTL2    -0.180000       12.0110           
        34 SYS      1        TRIO     H7A      HAL2     0.090000        1.0080           
        35 SYS      1        TRIO     H7B      HAL2     0.090000        1.0080           
        36 SYS      1        TRIO     C16      CTL2    -0.180000       12.0110           
        37 SYS      1        TRIO     H6A      HAL2     0.090000        1.0080           
        38 SYS      1        TRIO     H6B      HAL2     0.090000        1.0080           
        39 SYS      1        TRIO     C15      CTL2    -0.180000       12.0110           
        40 SYS      1        TRIO     H5A      HAL2     0.090000        1.0080           
        41 SYS      1        TRIO     H5B      HAL2     0.090000        1.0080           
        42 SYS      1        TRIO     C14      CTL2    -0.180000       12.0110           
        43 SYS      1        TRIO     H4A      HAL2     0.090000        1.0080           
        44 SYS      1        TRIO     H4B      HAL2     0.090000        1.0080           
        45 SYS      1        TRIO     C13      CTL2    -0.180000       12.0110           
        46 SYS      1        TRIO     H3A      HAL2     0.090000        1.0080           
        47 SYS      1        TRIO     H3B      HAL2     0.090000        1.0080           
        48 SYS      1        TRIO     C1       CTL2     0.080000       12.0110           
        49 SYS      1        TRIO     HA       HAL2     0.090000        1.0080           
        50 SYS      1        TRIO     HB       HAL2     0.090000        1.0080           
        51 SYS      1        TRIO     O11      OSL     -0.490000       15.9994           
        52 SYS      1        TRIO     C11      CL       0.900000       12.0110           
        53 SYS      1        TRIO     O12      OBL     -0.630000       15.9994           
        54 SYS      1        TRIO     C12      CTL2    -0.220000       12.0110           
        55 SYS      1        TRIO     H2A      HAL2     0.090000        1.0080           
        56 SYS      1        TRIO     H2B      HAL2     0.090000        1.0080           
        57 SYS      1        TRIO     C2       CTL1     0.170000       12.0110           
        58 SYS      1        TRIO     HS       HAL1     0.090000        1.0080           
        59 SYS      1        TRIO     O21      OSL     -0.490000       15.9994           
        60 SYS      1        TRIO     C21      CL       0.900000       12.0110           
        61 SYS      1        TRIO     O22      OBL     -0.630000       15.9994           
        62 SYS      1        TRIO     C22      CTL2    -0.220000       12.0110           
        63 SYS      1        TRIO     H2R      HAL2     0.090000        1.0080           
        64 SYS      1        TRIO     H2S      HAL2     0.090000        1.0080           
        65 SYS      1        TRIO     C3       CTL2     0.080000       12.0110           
        66 SYS      1        TRIO     HX       HAL2     0.090000        1.0080           
        67 SYS      1        TRIO     HY       HAL2     0.090000        1.0080           
        68 SYS      1        TRIO     O31      OSL     -0.490000       15.9994           
        69 SYS      1        TRIO     C31      CL       0.900000       12.0110           
        70 SYS      1        TRIO     O32      OBL     -0.630000       15.9994           
        71 SYS      1        TRIO     C32      CTL2    -0.220000       12.0110           
        72 SYS      1        TRIO     H2X      HAL2     0.090000        1.0080           
        73 SYS      1        TRIO     H2Y      HAL2     0.090000        1.0080           
        74 SYS      1        TRIO     C23      CTL2    -0.180000       12.0110           
        75 SYS      1        TRIO     H3R      HAL2     0.090000        1.0080           
        76 SYS      1        TRIO     H3S      HAL2     0.090000        1.0080           
        77 SYS      1        TRIO     C24      CTL2    -0.180000       12.0110           
        78 SYS      1        TRIO     H4R      HAL2     0.090000        1.0080           
        79 SYS      1        TRIO     H4S      HAL2     0.090000        1.0080           
        80 SYS      1        TRIO     C25      CTL2    -0.180000       12.0110           
        81 SYS      1        TRIO     H5R      HAL2     0.090000        1.0080           
        82 SYS      1        TRIO     H5S      HAL2     0.090000        1.0080           
        83 SYS      1        TRIO     C26      CTL2    -0.180000       12.0110           
        84 SYS      1        TRIO     H6R      HAL2     0.090000        1.0080           
        85 SYS      1        TRIO     H6S      HAL2     0.090000        1.0080           
        86 SYS      1        TRIO     C27      CTL2    -0.180000       12.0110           
        87 SYS      1        TRIO     H7R      HAL2     0.090000        1.0080           
        88 SYS      1        TRIO     H7S      HAL2     0.090000        1.0080           
        89 SYS      1        TRIO     C28      CTL2    -0.180000       12.0110           
        90 SYS      1        TRIO     H8R      HAL2     0.090000        1.0080           
        91 SYS      1        TRIO     H8S      HAL2     0.090000        1.0080           
        92 SYS      1        TRIO     C29      CEL1    -0.150000       12.0110           
        93 SYS      1        TRIO     H9R      HEL1     0.150000        1.0080           
        94 SYS      1        TRIO     C210     CEL1    -0.150000       12.0110           
        95 SYS      1        TRIO     H10R     HEL1     0.150000        1.0080           
        96 SYS      1        TRIO     C211     CTL2    -0.180000       12.0110           
        97 SYS      1        TRIO     H11R     HAL2     0.090000        1.0080           
        98 SYS      1        TRIO     H11S     HAL2     0.090000        1.0080           
        99 SYS      1        TRIO     C212     CTL2    -0.180000       12.0110           
       100 SYS      1        TRIO     H12R     HAL2     0.090000        1.0080           
       101 SYS      1        TRIO     H12S     HAL2     0.090000        1.0080           
       102 SYS      1        TRIO     C213     CTL2    -0.180000       12.0110           
       103 SYS      1        TRIO     H13R     HAL2     0.090000        1.0080           
       104 SYS      1        TRIO     H13S     HAL2     0.090000        1.0080           
       105 SYS      1        TRIO     C214     CTL2    -0.180000       12.0110           
       106 SYS      1        TRIO     H14R     HAL2     0.090000        1.0080           
       107 SYS      1        TRIO     H14S     HAL2     0.090000        1.0080           
       108 SYS      1        TRIO     C215     CTL2    -0.180000       12.0110           
       109 SYS      1        TRIO     H15R     HAL2     0.090000        1.0080           
       110 SYS      1        TRIO     H15S     HAL2     0.090000        1.0080           
       111 SYS      1        TRIO     C216     CTL2    -0.180000       12.0110           
       112 SYS      1        TRIO     H16R     HAL2     0.090000        1.0080           
       113 SYS      1        TRIO     H16S     HAL2     0.090000        1.0080           
       114 SYS      1        TRIO     C217     CTL2    -0.180000       12.0110           
       115 SYS      1        TRIO     H17R     HAL2     0.090000        1.0080           
       116 SYS      1        TRIO     H17S     HAL2     0.090000        1.0080           
       117 SYS      1        TRIO     C218     CTL3    -0.270000       12.0110           
       118 SYS      1        TRIO     H18R     HAL3     0.090000        1.0080           
       119 SYS      1        TRIO     H18S     HAL3     0.090000        1.0080           
       120 SYS      1        TRIO     H18T     HAL3     0.090000        1.0080           
       121 SYS      1        TRIO     C33      CTL2    -0.180000       12.0110           
       122 SYS      1        TRIO     H3X      HAL2     0.090000        1.0080           
       123 SYS      1        TRIO     H3Y      HAL2     0.090000        1.0080           
       124 SYS      1        TRIO     C34      CTL2    -0.180000       12.0110           
       125 SYS      1        TRIO     H4X      HAL2     0.090000        1.0080           
       126 SYS      1        TRIO     H4Y      HAL2     0.090000        1.0080           
       127 SYS      1        TRIO     C35      CTL2    -0.180000       12.0110           
       128 SYS      1        TRIO     H5X      HAL2     0.090000        1.0080           
       129 SYS      1        TRIO     H5Y      HAL2     0.090000        1.0080           
       130 SYS      1        TRIO     C36      CTL2    -0.180000       12.0110           
       131 SYS      1        TRIO     H6X      HAL2     0.090000        1.0080           
       132 SYS      1        TRIO     H6Y      HAL2     0.090000        1.0080           
       133 SYS      1        TRIO     C37      CTL2    -0.180000       12.0110           
       134 SYS      1        TRIO     H7X      HAL2     0.090000        1.0080           
       135 SYS      1        TRIO     H7Y      HAL2     0.090000        1.0080           
       136 SYS      1        TRIO     C38      CTL2    -0.180000       12.0110           
       137 SYS      1        TRIO     H8X      HAL2     0.090000        1.0080           
       138 SYS      1        TRIO     H8Y      HAL2     0.090000        1.0080           
       139 SYS      1        TRIO     C39      CEL1    -0.150000       12.0110           
       140 SYS      1        TRIO     H9X      HEL1     0.150000        1.0080           
       141 SYS      1        TRIO     C310     CEL1    -0.150000       12.0110           
       142 SYS      1        TRIO     H10X     HEL1     0.150000        1.0080           
       143 SYS      1        TRIO     C311     CTL2    -0.180000       12.0110           
       144 SYS      1        TRIO     H11X     HAL2     0.090000        1.0080           
       145 SYS      1        TRIO     H11Y     HAL2     0.090000        1.0080           
       146 SYS      1        TRIO     C312     CTL2    -0.180000       12.0110           
       147 SYS      1        TRIO     H12X     HAL2     0.090000        1.0080           
       148 SYS      1        TRIO     H12Y     HAL2     0.090000        1.0080           
       149 SYS      1        TRIO     C313     CTL2    -0.180000       12.0110           
       150 SYS      1        TRIO     H13X     HAL2     0.090000        1.0080           
       151 SYS      1        TRIO     H13Y     HAL2     0.090000        1.0080           
       152 SYS      1        TRIO     C314     CTL2    -0.180000       12.0110           
       153 SYS      1        TRIO     H14X     HAL2     0.090000        1.0080           
       154 SYS      1        TRIO     H14Y     HAL2     0.090000        1.0080           
       155 SYS      1        TRIO     C315     CTL2    -0.180000       12.0110           
       156 SYS      1        TRIO     H15X     HAL2     0.090000        1.0080           
       157 SYS      1        TRIO     H15Y     HAL2     0.090000        1.0080           
       158 SYS      1        TRIO     C316     CTL2    -0.180000       12.0110           
       159 SYS      1        TRIO     H16X     HAL2     0.090000        1.0080           
       160 SYS      1        TRIO     H16Y     HAL2     0.090000        1.0080           
       161 SYS      1        TRIO     C317     CTL2    -0.180000       12.0110           
       162 SYS      1        TRIO     H17X     HAL2     0.090000        1.0080           
       163 SYS      1        TRIO     H17Y     HAL2     0.090000        1.0080           
       164 SYS      1        TRIO     C318     CTL3    -0.270000       12.0110           
       165 SYS      1        TRIO     H18X     HAL3     0.090000        1.0080           
       166 SYS      1        TRIO     H18Y     HAL3     0.090000        1.0080           
       167 SYS      1        TRIO     H18Z     HAL3     0.090000        1.0080             
"""

# Splitting the string into lines and processing each line to create the dictionary
trio_psf_dict = {}
for line in trio_psf_snippet.strip().split('\n'):
    parts = line.split()
    if len(parts) > 5:
        atom_name, atom_type = parts[4], parts[5]
        trio_psf_dict[atom_name] = atom_type

trio_psf_dict

# Step 1: Read "save.psf"
with open('save.psf', 'r') as file:
    save_psf_lines = file.readlines()

# Step 2: Update "save.psf"
for i, line in enumerate(save_psf_lines):
    print(line)
    if line.strip() and line[0].isdigit():
        parts = line.split()
        if len(parts) >= 6:
            atom_name = parts[4]
            original_atom_type = parts[5]
            correct_atom_type = trio_psf_dict.get(atom_name, original_atom_type)  # Default to existing type if not found
            # Debugging: Print original and new atom types for the line
            print(f"Line {i}: Original Atom Type = {original_atom_type}, New Atom Type = {correct_atom_type}")
            # Reconstruct the line with the correct atom type
            updated_line = f"{parts[0]:>10s} {parts[1]:>4s} {parts[2]:>4s} {parts[3]:>8s} {parts[4]:>8s} {correct_atom_type:<8s} {parts[6]:>12s} {parts[7]:>12s}\n"
            save_psf_lines[i] = updated_line

# Step 3: Write the Updated "save.psf"
with open('corrected_save.psf', 'w') as file:
    file.writelines(save_psf_lines)

