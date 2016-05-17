
# coding: utf-8

# In[50]:

import numpy as np

# input parameters
units  = 'cm'     # units of measurement
R_l    = 5200     # load
R_p    = 1200     # plate resistance
R_s    = 8        # speaker impedance
f_l    = 40       # lowest frequency
f_h    = 22000    # highest frequency
P_out  = 5        # output power
I_0    = 48       # quiescent current
S      = 4.2      # area of the core
D_flux = 13       # mean distance of the magnetic flux

# assumed parameters
B      = 2000     # core maximum flux density
mu     = 5e-3     # core permeability (steel)
eta    = 0.9      # transformer efficiency
alpha  = 0.9      # core fill factor
beta   = 0.8      # core window fill factor

# prevent wrong units to be specified
if units != 'cm' and units != 'in':
    raise Exception('Wrong units. Use \'cm\' or \'in\'', units)

# primary inductance
L_p = ((R_l * R_p) / (R_l + R_p)) / (2 * np.pi * f_l)

# leakage inductance
L_l = (R_l + R_p) / (2 * np.pi * f_h)

# turns ratio between the primary and the seconday windings
n = np.sqrt(R_l / R_s)

# minimum area of the core
S_min = 1.8 * np.sqrt(P_out)

if units == 'in':
    S_min = S_min / 6.46
        
# primary turns (without the air gap)
if units == 'cm':
    N_pri_factor = 28.21
else:
    N_pri_factor = 17.70
    
N_pri = N_pri_factor * np.sqrt((L_p * D_flux) / (alpha * mu * S))
        
# air gap
if units == 'cm':
    delta_factor = 1.6e-6
else:
    delta_factor = 6.3e-7
    
delta = delta_factor * N_pri * I_0

# effective core permeability
mu_eff = (mu * D_flux) / (D_flux + (mu * 1e4 * delta))

if units == 'in':
    mu_eff = mu_eff * 1.367

# corrected number of primary winding turns
N_pri_gap = N_pri_factor * np.sqrt((L_p * D_flux) / (alpha * mu_eff * S))

# secondary turns
N_sec = N_pri_gap / n

# print the results
print('Minimum primary inductance (H): {0:.3f}'.format(L_p))
print('Maximum leakage inductance (H): {0:.3f}\n'.format(L_l))
print('Turns ratio: {0:.2f}'.format(n))
print('Minimum core area size ({0}^2): {1:.2f}'.format(units, S_min))
print('Your core {0} this application!\n'       .format('should work well in' if S_min < S 
              else 'most likely is too small for'))
print('Number of primary turns: {0:.0f}'.format(np.ceil(N_pri_gap)))
print('Number of secondary turns: {0:.0f}'.format(np.ceil(N_sec)))

