#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def square_root(a: float) -> float:
   a = a ** (1/2)
   #corrigé: return math.sqrt(a)
   return a


def square(a: float) -> float:
    return a**2


def average(a: float, b: float, c: float) -> float:
    #ça dit que a, b, c sont des float et que la réponse est float
    return (a + b + c)/3
# en s'en fou de type de a b et c, mais le diviser par trois le rend en float
# test: va avoir la bonne reponse et ce que notre programme donne
#pas obligé faire test, donc regarder corrigé ou essayer de le rouler


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    return math.radians(angle_degs + (angle_mins + (angle_secs / 60)) / 60)
#1 degré = 60 minutes angulaires (1° = 60')
#1 minute angulaire = 60 secondes angulaires (1' = 60'')
#Pas les minutes de l'Horloge! c'est anglualire.

#Convertir en degrés, minutes, secondes un angle fourni au départ en radians
def to_degrees(angle_rads: float) -> tuple:#s'attend a ce qu'on retourne un tuple mais qu'on rentre un float.mais python ne force pas que ce soit un float
    degrees_angle = math.degrees(angle_rads) #math.degrees(x): Convertit l'angle x de radians en degrés.
    minutes_angle = (angle_rad*10 800)/math.pi
    seconds_angle = minute_angle/60
    return degrees_angle, minutes_angle, seconds_angle
#corrigé:
#    degrees = math.degrees(angle_rads)
    # min = (abs(degrees) - int(abs(degrees))) * 60
    # sec = (min - int(min)) * 60
    #return int(degrees), int(min), sec

#Convertir en degrés Celsius une température exprimée au départ en degrés Fahrenheit et vice-versa
def to_celsius(temperature: float) -> float:
    fahrenheit = (temperature * (9/5)) + 32
    return fahrenheit


def to_farenheit(temperature: float) -> float:
    celsius = (temperature -32) * (5/9)
    return celsius
#le prof a dit que mieux est de retourner une variable


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")

    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
