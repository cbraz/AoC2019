#!/usr/bin/env python3


def calculate_fuel_requirement(mass):
    req = (int(mass / 3)) - 2
    #print(req)
    if req <= 0:
        return 0
    if req > 0:
        req += calculate_fuel_requirement(req)
    return req


def calculate_total_fuel_requirements():
    total = 0
    with open('module_mass.txt') as mm:
        for mass in mm:
            #print('mass',int(mass))
            total += calculate_fuel_requirement(int(mass))
            #print(total)
    return total


if __name__ == '__main__':
    #print(calculate_fuel_requirement(1969))
    print(calculate_total_fuel_requirements())
