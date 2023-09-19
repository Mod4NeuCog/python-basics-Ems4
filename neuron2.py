#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:32:29 2023

@author: deneuvilleemma
"""

# neuron2.py
import sys

def compute_membrane_potential(spike_value, current_membrane_potential=0.0):
    new_membrane_potential = current_membrane_potential + spike_value

    if new_membrane_potential >= 65:
        return 1, new_membrane_potential
    else:
        return 0, new_membrane_potential

output_from_neuron1 = sys.stdin.readline().strip() 

if not output_from_neuron1:
    print("No input from neuron1.py")
else:
    output_value = float(output_from_neuron1)
    spike_value = float(input("Enter a spike value for neuron2: "))
    output, new_potential = compute_membrane_potential(spike_value)
    print("Output:", output)
    print("New Membrane Potential:", new_potential)


