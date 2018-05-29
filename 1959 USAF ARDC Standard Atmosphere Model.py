print("This is a Python program that computes atmospheric parameters such as air density, pressure and temperature based on the 1959 USAF ARDC Stanard Atmosphere Model.")
print('''
    Copyright (C) 2018 Nicholas Kang
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.\n''')
print("Feel free to contact the author at zt.kang@gmail.com or PM 'Nicholas Kang' in Orbiter Forum.")

geopotential_altitude = [-5000, 0, 11000, 25000, 47000, 53000, 79000, 90000, 105000, 160000, 170000, 200000, 700000]
temperature = [320.66, 288.16, 216.66, 216.66, 282.66, 282.66, 165.66, 165.66, 225.66, 1325.66, 1425.66, 1575.66, 3325.66]
lapse_rate = [-0.0065, -0.0065, 0, 0.0030, 0, -0.0045, 0, 0.0040, 0.02, 0.01, 0.0050, 0.0035]

if len(geopotential_altitude) == len(temperature) == (len(lapse_rate) + 1):
    pass

else:
    print('geopot_altitude_list_mag = {}, temperature_list_mag = {}, lapse_rate_list_mag = {}'.format(len(geopotential_altitude), len(temperature), len(lapse_rate)))
    print("Length of lists not the same. Database error.")

def temp(x):
    'Calculate temperature of air given the geopotential altitude of the atmosphere in range -5000 m to 700000 m (-5 km to 700 km) ONLY'
    if x < -5000 or x > 700000:
        print("Input value out of range. Min accepted value = -5000; Max accepted value = 700000.")
    else:
        for i in geopotential_altitude:
            if x == i:
                print("The temperature of the atmosphere at a geopotential altitude of {} m is {} degree Kelvin.".format(x, temperature[geopotential_altitude.index(i)]))
                break
            elif x < geopotential_altitude[geopotential_altitude.index(i) + 1]:
                if lapse_rate[geopotential_altitude.index(i)] == 0:
                    print("The temperature of the atmosphere at a geopotential altitude of {} m is {} degree Kelvin.".format(x, temperature[geopotential_altitude.index(i)]))
                else:
                    T = (lapse_rate[geopotential_altitude.index(i)])*(x - i) + temperature[geopotential_altitude.index(i)]
                    print("The temperature of the atmosphere at a geopotential altitude of {} m is {} degree Kelvin.".format(x, T))
                break


                
            

