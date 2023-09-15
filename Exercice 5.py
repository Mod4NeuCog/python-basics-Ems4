#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:11:43 2023

@author: deneuvilleemma
"""


def compute_membrane_potential(spike_value, weight, current_membrane_potential=0.0):
  
    new_membrane_potential = current_membrane_potential + (spike_value * weight)

    # Check if the membrane potential reaches -65mV
    if new_membrane_potential >= -65:
        return 5, new_membrane_potential
    else:
        return 0, new_membrane_potential


# input a spike value 
spike_value = float(input("Enter a spike value: "))

#input the weight parameter
weight = float(input("Enter the weight parameter: "))

# Compute the new membrane potential
output, new_potential = compute_membrane_potential(spike_value, weight)

print("Output:", output)
print("New Membrane Potential:", new_potential)


