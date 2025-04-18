#!/usr/bin/python3
from pet import Pet

dog = Pet('sport')

dog.eat() #reduces hunger by 3 points (but not below 0), and increases happiness by 1.

dog.sleep() #increases energy by 5 points (but not above 10).

dog.play() #decreases energy by 2, increases happiness by 2, and increases hunger by 1.

dog.train('hopping') 
dog.train('skipping') 

dog.get_status()
dog.show_tricks()