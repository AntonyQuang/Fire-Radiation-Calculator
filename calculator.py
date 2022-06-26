from tkinter import *
from tkinter.ttk import *
from pprint import pprint
from math import sqrt, ceil, pi
import pandas as pd


# widths_fields = ["End windows' outer width, m",
#                  "End windows' inner width, m",
#                  "Centre windows' outer width, m",
#                  "Doors' outer width, m",
#                  "Doors' inner width, m"]
#
# heights_fields = ["End windows' height, m",
#                   "Centre windows' height, m",
#                   "Windows' midpoint height from floor, m",
#                   "Doors' height, m",
#                   "Doors' midpoint height from floor, m"]
#
# fire_fields = ["Maximum Fire Size, MW",
#                "Heat Release Rate per Unit Area, kW/m\u00B2",
#                "Convection Fraction (0 to 1)"]
#
# fire_combo_fields = ["Fire Growth Rate, \u03B1, kW/s\u00B2"]

# all_inputs = [title_entries, widths_entries, heights_entries, fire_entries, fire_growth_entries]

def calculate(processed_inputs):
    # Separating the inputs
    titles = processed_inputs[0]
    widths = processed_inputs[1]
    heights = processed_inputs[2]
    fire_parameters = processed_inputs[3]
    fire_growth = processed_inputs[4]

    # Setting out Titles
    calc_title = titles["Calculation Title"]

    # Setting out fire constants
    fire_growth_rates = {"Slow": 0.0029, "Medium": 0.0117, "Fast": 0.047, "Ultra-fast": 0.188}
    alpha = fire_growth_rates[fire_growth["Fire Growth Rate, \u03B1, kW/s\u00B2"]]
    print(alpha)
    max_hrr = fire_parameters["Maximum Fire Size, MW"] * 1000
    hrrpua = fire_parameters["Heat Release Rate per Unit Area, kW/m\u00B2"]
    conv_fraction = fire_parameters["Convection Fraction (0 to 1)"]

    # Setting out width constants
    end_outer_w = widths["End windows' outer width, m"]
    end_inner_w = widths["End windows' inner width, m"]
    centre_w = widths["Centre windows' outer width, m"]
    doors_outers_w = widths["Doors' outer width, m"]
    doors_inner_w = widths["Doors' inner width, m"]

    # Setting out height constants
    end_height = heights["End windows' height, m"]
    centre_height = heights["Centre windows' height, m"]
    doors_height = heights["Doors' height, m"]
    window_midheight = heights["Windows' midpoint height from floor, m"]
    doors_midheight = heights["Doors' midpoint height from floor, m"]

    # Setting out time constants

    dt = 1
    time_period = ceil(sqrt(max_hrr / alpha))

    # Setting out misc constants
    sigma = 5.67 * 10 ** -11  # Stefan-Boltzmann constant is approximately 5.67 x 10 -11 (kW · m -2 · K -4 ).

    columns = ["Time, s",
               "Time, min",
               "HRR, kW",
               "Diameter, m",
               "z0",
               "Windows Temperature, K",
               "Doors Temperature, K",
               "Maximum Windows Heat, kW/m2",
               "Maximum Doors Heat, kW/m2"]

    time_s = []
    time_m = []
    hrr = []
    diameter = []
    z0 = []
    windows_temp = []
    doors_temp = []
    max_windows_heat = []
    max_doors_heat = []

    for i in range(time_period):
        time_s.append(i)
        time_m.append(time_s[i]/60)
        hrr.append(alpha*time_s[i]**2)
        diameter.append(2*sqrt(hrr[i]/(pi*hrrpua)))
        z0.append(-1.02*diameter[i]+0.083*hrr[i]**(2/5))
        windows_temp.append(293+25*(conv_fraction*hrr[i])**(2/3)*(window_midheight-z0[i])**(-5/3))
        doors_temp.append(293+25*(conv_fraction*hrr[i])**(2/3)*(doors_midheight-z0[i])**(-5/3))
        max_windows_heat.append(1*sigma*windows_temp[i]**4)
        max_doors_heat.append(1*sigma*doors_temp[i]**4)

