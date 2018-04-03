import random

health = 50

#1=easy, 2=medium, and 3=hard.
difficulty = 1

#calculate the amount of health that will be added to the player's health.
#used int() to convert float into and int to get rid of the decimal point.
potion_health = int(random.randint(25,50) / difficulty)

health = health + potion_health

print(health)
