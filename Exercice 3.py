#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 14:58:20 2023

@author: deneuvilleemma
"""
# neuron1.py

# Ask the user to input a spike value
spike_value = float(input("Enter a spike value: "))

membrane_potential = 0.0

membrane_potential += spike_value

    # Check if the membrane potential reaches -65mV
if membrane_potential >= -65:
        print("5")
else:
    print("0")


# neuron2.py
import sys

    # Read the output from neuron1.py from stdin
output_from_neuron1 = sys.stdin.readline().strip()

if not output_from_neuron1:
    print("No input from neuron1.py")
else : 
    output_value = float(output_from_neuron1)

membrane_potential = 0.0

# Ask the user to input a spike value for neuron2
spike_value = float(input("Enter a spike value for neuron2: "))

# Update the membrane potential using the input spike value
membrane_potential += spike_value
# Check if the membrane potential reaches -65mV
if membrane_potential >= -65:
    print("5")
else:
    print("0")
   

