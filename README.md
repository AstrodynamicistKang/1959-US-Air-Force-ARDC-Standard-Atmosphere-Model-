# 1959-US-Air-Force-ARDC-Standard-Atmosphere-Model-
A Python program that computes atmospheric parameters such as atmospheric pressure, density and temperature based on the 1959 US Air Force ARDC (Air Research and Development Command) atmospheric model

## Supported features/functions

Currently supported features (with functions defined in Markdown syntax highlight):

1. Computing:
    - Air temperature, ```
                      temp(x)
                      ```
    - Air pressure, ```
                   pres(x)
                   ``` 
    - Air density, ```
                  dens(x)
                  ```
 
2. Converting:
    - Geopotential altitude to geometric altitude, ```
                                                   pot2met(x)
                                                   ```
    - Geometric altitude to geopotential altitude, ```
                                                   met2pot(x)
                                                   ```

Note on the units of the arguments accepted, i.e. x in the above case:

| Functions | Input unit | Output Unit |
| --- | --- | --- |
| temp(x) | m, meters | K, Kelvin |
| pres(x) | m, meters | Pa, Pascal |
| dens(x) | m, meters | kg m^-3 |
| pot2met(x) | any length unit | same length unit as input |
| met2pot(x) | any length unit | same length unit as input |

## Formulae

Kindly refer to the USAF ARDC documentation to learn more about the derivation of the formulae used in the program.

