# Under development for easy use. 
* Need to clean and streamline Jupyter notebooks

###  Files Overview

This repository includes all necessary files to compute surface tension from molecular dynamics simulations.

- **`lipid_drude.str`**  
  CHARMM topology stream file containing force field parameters for the lipid system (Drude polarizable model).

- **Other files (`.inp`, `.py`, `.sh`, `.ipynb`)**  
  Scripts and inputs used to:
  - Run CHARMM simulations  
  - Extract pressure tensor components  
  - Calculate surface tension from pressure data  
  - Perform block averaging and statistical analysis

Surface tension is computed using the standard formula:

`γ = (Lz / 2) × [Pzz − (Pxx + Pyy)/2]`
