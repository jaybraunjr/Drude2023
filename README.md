# Under development for easy use. 
* Need to clean and streamline Jupyter notebooks
  

###  Files Overview

- **`TRIO.str`**  
  topology stream file containing force field parameters for the triacylglycerol.

- **Other files**  
  Scripts and inputs used to:
  - Run CHARMM simulations  
  - Extract pressure tensor components  
  - Calculate surface tension from pressure data  
  - Perform block averaging and statistical analysis

Surface tension is computed using the standard formula:

`γ = (Lz / 2) × [Pzz − (Pxx + Pyy)/2]`

* Will soon include GMX to CHARMM scripts
