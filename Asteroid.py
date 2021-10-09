import pyxel
from settings import *
from math import sin, cos, radians, sqrt
from random import randint, choice


class Asteroid:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 0
        self.rotation = -randint(0, 360)
        self.size = choice(asteroid["radius"])


    def set_location(self):
        if choice(["horizontal", "vertical"]) == "vertical":
            self.x = choice([-self.size, game["width"] + self.size])
            self.y = randint(-self.size, game["height"] + self.size)
        elif choice(["horizontal", "vertical"]) == "horizontal":
            self.x = randint(-self.size, game["height"] + self.size)
            self.y = choice([-self.size, game["width"] + self.size])

        if (elapsedTime - lastAst) >= asteroidLimitTime:
            asteroids.append([astx, asty, astrot, astradius])
            lastAst = elapsedTime

    def move(self):
        self.x += self.speed * cos(radians(self.rotation)) * game["frame"]
        self.y += self.speed * sin(radians(self.rotation)) * game["frame"]

    def draw(self):
        pyxel.circ(self.x, self.y, self.size, pyxel.COLOR_WHITE)

    def check_limit(self):
        if (self.x < -self.size or self.x > game["width"] + self.size) or (self.y < -self.size or self.y > game["height"] + self.size):
            asteroid["asteroids"].remove(self)

