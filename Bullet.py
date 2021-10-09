import pyxel
from settings import *
from math import sin, cos, radians


class Bullet:
    def __init__(self, x, y, rotation):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.speed = bullet["speed"]

    def move(self):
        self.x += self.speed * cos(radians(self.rotation)) * game["frame"]
        self.y += self.speed * sin(radians(self.rotation)) * game["frame"]

    def draw(self):
        pyxel.rect(self.x, self.y, 1, 1, pyxel.COLOR_RED)

    def check_limit(self):
        if (self.x < 0 or self.x > game["width"]) or (self.y < 0 or self.y > game["height"]):
            bullet["bullets"].remove(self)

    ###################
"""    

        def verifyBulletCollision():
            for bullet in bullets:
                for ast in asteroids:
                    if (sqrt((bullet[0] - ast[0]) ** 2 + (bullet[1] - ast[1]) ** 2)) < ast[3]:
                        if ast[3] == min(asteroidRadius):
                            bullets.remove(bullet)
                            asteroids.remove(ast)
                        else:
                            x = asteroids.pop(asteroids.index(ast))
                            asteroids.append([x[0], x[1], x[2] - 45, min(asteroidRadius)])
                            asteroids.append([x[0], x[1], x[2] + 45, min(asteroidRadius)])
        ###
"""
