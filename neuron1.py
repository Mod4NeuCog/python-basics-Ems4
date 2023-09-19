#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:30:59 2023

@author: deneuvilleemma
"""
# neuron1.py

import sys 

def compute_membrane_potential(spike_value, current_membrane_potential=0.0):
    new_membrane_potential = current_membrane_potential + spike_value

    if new_membrane_potential >= -65:
        return 1, new_membrane_potential
    else:
        return 0, new_membrane_potential

spike_value = float(sys.argv[1]) 
output, new_potential = compute_membrane_potential(spike_value)

print("Output:", output)
print("New Membrane Potential:", new_potential)
