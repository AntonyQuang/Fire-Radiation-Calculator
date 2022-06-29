from tkinter import messagebox
from math import sqrt, ceil, pi, atan
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


def view_factor_calc(width, height, distance):
    x = width / distance
    y = height / distance
    coeff_1 = x / (sqrt(1 + x ** 2))
    coeff_2 = y / (sqrt(1 + y ** 2))
    atan_arg_1 = y / (sqrt(1 + x ** 2))
    atan_arg_2 = x / (sqrt(1 + y ** 2))

    view_factor = (coeff_1 * atan(atan_arg_1) + coeff_2 * atan(atan_arg_2)) / (2*pi)

    # The AECOM way: Which is wrong!!
    # x = width / distance / 2
    # y = height / distance / 2
    # a = sqrt(1 + x ** 2)
    # b = sqrt(1 + y ** 2)
    # coeff_1 = x / a
    # coeff_2 = y / b
    # atan_arg_1 = y / a
    # atan_arg_2 = x / b
    #
    # view_factor = 2 * (coeff_1 * atan(atan_arg_1) + coeff_2 * atan(atan_arg_2)) / 3.14159265358979
    return view_factor


def windows_view_factor_calc(end_outer_w, end_inner_w, centre_w,
                             end_h, centre_h,
                             distance):
    windows_view_factor = view_factor_calc(end_outer_w, end_h, distance) - \
                          view_factor_calc(end_inner_w, end_h, distance) + \
                          view_factor_calc(centre_w, centre_h, distance)
    return windows_view_factor


def doors_view_factor_calc(doors_outers_w, doors_inner_w,
                           doors_h,
                           distance):
    doors_view_factor = view_factor_calc(doors_outers_w, doors_h, distance) - \
                        view_factor_calc(doors_inner_w, doors_h, distance)
    return doors_view_factor


def radiation_calc(end_outer_w, end_inner_w, centre_w, doors_outers_w, doors_inner_w,
                   end_h, centre_h, doors_h,
                   max_windows_heat, max_doors_heat,
                   distance):
    windows_view_factor = windows_view_factor_calc(end_outer_w, end_inner_w, centre_w,
                                                   end_h, centre_h,
                                                   distance)

    doors_view_factor = doors_view_factor_calc(doors_outers_w, doors_inner_w,
                                               doors_h,
                                               distance)

    radiation = max_windows_heat * windows_view_factor + max_doors_heat * doors_view_factor
    return radiation


def separation_distance_calc(end_outer_w, end_inner_w, centre_w, doors_outers_w, doors_inner_w,
                             end_h, centre_h, doors_h,
                             max_windows_heat, max_doors_heat):
    max_iterations = 1000
    error = 0.0001
    iterations = 0

    lower_guess = 1 * 10 ** -100
    # radiation depends on the distance, which we are guessing now
    # to get radiation you need the overall view factors
    # to get the overall view factors you need the aggregate view factor

    radiation = radiation_calc(end_outer_w, end_inner_w, centre_w, doors_outers_w, doors_inner_w,
                               end_h, centre_h, doors_h,
                               max_windows_heat, max_doors_heat,
                               lower_guess)

    if radiation < 2.5:
        return 0

    upper_guess = 20

    radiation = radiation_calc(end_outer_w, end_inner_w, centre_w, doors_outers_w, doors_inner_w,
                               end_h, centre_h, doors_h,
                               max_windows_heat, max_doors_heat,
                               upper_guess)

    if radiation > 2.5:
        return "Error: 20m separation distance exceeded, fire too big?"

    while upper_guess - lower_guess > error and iterations < max_iterations:

        iterations += 1

        new_guess = (upper_guess + lower_guess) / 2

        radiation = radiation_calc(end_outer_w, end_inner_w, centre_w, doors_outers_w, doors_inner_w,
                                   end_h, centre_h, doors_h,
                                   max_windows_heat, max_doors_heat,
                                   new_guess)

        if radiation < 2.5:
            # you are too far away to feel the critical heat flux, so you can't guess any further/greater than this
            upper_guess = new_guess
        else:
            lower_guess = new_guess

    return lower_guess


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
    fire_growth_rates = {"Slow": 0.00293, "Medium": 0.01172, "Fast": 0.0469, "Ultra-fast": 0.1876}
    alpha = fire_growth_rates[fire_growth["Fire Growth Rate, \u03B1, kW/s\u00B2"]]
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
    end_h = heights["End windows' height, m"]
    centre_h = heights["Centre windows' height, m"]
    doors_h = heights["Doors' height, m"]
    window_mid_h = heights["Windows' midpoint height from floor, m"]
    doors_mid_h = heights["Doors' midpoint height from floor, m"]

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
               "Maximum Doors Heat, kW/m2",
               "Separation Distance, m"]

    time_s = []
    time_m = []
    hrr = []
    diameter = []
    z0 = []
    windows_temp = []
    doors_temp = []
    max_windows_heat = []
    max_doors_heat = []
    separation_distance = []

    for i in range(time_period):
        time_s.append(i)
        time_m.append(time_s[i] / 60)
        hrr.append(alpha * time_s[i] ** 2)
        diameter.append(2 * sqrt(hrr[i] / (pi * hrrpua)))
        z0.append(-1.02 * diameter[i] + 0.083 * hrr[i] ** (2 / 5))
        windows_temp.append(293 + 25 * (conv_fraction * hrr[i]) ** (2 / 3) * (window_mid_h - z0[i]) ** (-5 / 3))
        doors_temp.append(293 + 25 * (conv_fraction * hrr[i]) ** (2 / 3) * (doors_mid_h - z0[i]) ** (-5 / 3))
        max_windows_heat.append(1 * sigma * windows_temp[i] ** 4)
        max_doors_heat.append(1 * sigma * doors_temp[i] ** 4)
        separation_distance_calculated = separation_distance_calc(end_outer_w, end_inner_w, centre_w,
                                                                  doors_outers_w, doors_inner_w,
                                                                  end_h, centre_h, doors_h,
                                                                  max_windows_heat[i], max_doors_heat[i]
                                                                  )
        separation_distance.append(separation_distance_calculated)

    # Creating an entry for the max_hrr

    hrr.append(max_hrr)
    time_s.append(ceil(sqrt(max_hrr / alpha)))
    time_m.append(time_s[-1]/60)
    diameter.append(2 * sqrt(hrr[-1] / (pi * hrrpua)))
    z0.append(-1.02 * diameter[-1] + 0.083 * hrr[-1] ** (2 / 5))
    windows_temp.append(293 + 25 * (conv_fraction * hrr[-1]) ** (2 / 3) * (window_mid_h - z0[-1]) ** (-5 / 3))
    doors_temp.append(293 + 25 * (conv_fraction * hrr[-1]) ** (2 / 3) * (doors_mid_h - z0[-1]) ** (-5 / 3))
    max_windows_heat.append(1 * sigma * windows_temp[-1] ** 4)
    max_doors_heat.append(1 * sigma * doors_temp[-1] ** 4)
    separation_distance_calculated = separation_distance_calc(end_outer_w, end_inner_w, centre_w,
                                                              doors_outers_w, doors_inner_w,
                                                              end_h, centre_h, doors_h,
                                                              max_windows_heat[-1], max_doors_heat[-1]
                                                              )
    separation_distance.append(separation_distance_calculated)
    
    df = pd.DataFrame({"Time, s": time_s,
                       "Time, min": time_m,
                       "HRR, kW": hrr,
                       "Diameter, m": diameter,
                       "z0": z0,
                       "Windows Temperature, K": windows_temp,
                       "Doors Temperature, K": doors_temp,
                       "Maximum Windows Heat, kW/m2": max_windows_heat,
                       "Maximum Doors Heat, kW/m2": max_doors_heat,
                       "Separation Distance, m": separation_distance})

    df.to_excel(f'{calc_title}.xlsx', sheet_name="Results", index=False)
    messagebox.showinfo(title="Calculations Completed", message="A spreadsheet of the calculations have been created.")