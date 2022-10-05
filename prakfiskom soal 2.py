import numpy as np
import matplotlib.pyplot as plt

#Gunakan oerasi perhitungan fisika matematika untuk menghitung jarak fokus lensa (f)ndalam cm pada persamaan pembuat lensa 1/f = (n-1)[1/R1+1R2] dengan indek  n bias medium
n = 1.50
R1 = 20 
R2 = 18 
F = (n-1)*(1/R1+1/R2)
F = 1/F

print(F)
