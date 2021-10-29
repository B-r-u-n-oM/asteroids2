import pyxel
from settings import *
from Bullet import *
from math import sin, cos, radians, sqrt
from random import randint, choice


class Enemy:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rotation = 0
        self.color = enemy["color"]
        self.speed = enemy["speed"]
        self.trisize = enemy["trisize"]
        self.tricoordinates = {
            "x1": 0, "y1": 0, "x2": 0, "y2": 0, "x3": 0, "y3": 0
        }
        self.spawn()

    def set_location(self):
        if choice(["H", "V"]) == "V":
            self.x = choice([-self.trisize, game["width"] + self.trisize])
            self.y = randint(-self.trisize, game["height"] + self.trisize)
            if self.x == -self.trisize:
                self.rotation = randint(-79, 79)
            else:
                self.rotation = randint(101, 259)
        elif choice(["H", "V"]) == "H":
            self.x = randint(-self.trisize, game["height"] + self.trisize)
            self.y = choice([-self.trisize, game["width"] + self.trisize])
            if self.y == -self.trisize:
                self.rotation = randint(10, 169)
            else:
                self.rotation = randint(191, 349)
        if self.x == 0 and self.y == 0: self.set_location()

    def spawn(self):
        self.set_location()
        if (game["elapsed_time"] - enemy["last_spawn"]) >= enemy["limit_time"]:
            enemy["enemies"].append(self)
            enemy["last_spawn"] = game["elapsed_time"]

    def check_limit(self):
        if (self.x < -self.trisize or self.x > game["width"] + self.trisize) or (self.y < -self.trisize or self.y > game["height"] + self.trisize):
            enemy["enemies"].remove(self)

    def draw(self):
        pyxel.trib(
            self.tricoordinates["x1"], self.tricoordinates["y1"],
            self.tricoordinates["x2"], self.tricoordinates["y2"],
            self.tricoordinates["x3"], self.tricoordinates["y3"],
            self.color)

    def move(self):
        self.x += self.speed * cos(radians(self.rotation)) * game["frame"]
        self.y += self.speed * sin(radians(self.rotation)) * game["frame"]

        self.tricoordinates["x1"] = self.x + cos(radians(self.rotation)) * (self.trisize/2) / cos(radians(30))
        self.tricoordinates["y1"] = self.y + sin(radians(self.rotation)) * (self.trisize/2) / cos(radians(30))
        self.tricoordinates["x2"] = self.x + cos(radians(self.rotation + 120)) * (self.trisize/2) / cos(radians(30))
        self.tricoordinates["y2"] = self.y + sin(radians(self.rotation + 120)) * (self.trisize/2) / cos(radians(30))
        self.tricoordinates["x3"] = self.x + cos(radians(self.rotation + 240)) * (self.trisize/2) / cos(radians(30))
        self.tricoordinates["y3"] = self.y + sin(radians(self.rotation + 240)) * (self.trisize/2) / cos(radians(30))

    def shot(self):
        #if (game["elapsed_time"] - bullet["last_shot"]) >= bullet["limit_time"]:
        bullet["bullets"].append(Bullet(self.x, self.y, self.rotation))
        bullet["last_shot"] = game["elapsed_time"]

    """def verify_collision(self):
        if self.controls_active:
            for a in asteroid["asteroids"]:
                if sqrt((a.x - self.x) ** 2 + (a.y - self.y) ** 2) < a.trisize + self.trisize/2:
                    self.lives -= 1
                    self.last_death = game["elapsed_time"]
                    self.controls_active = False
                    self.reset(hard_reset=False)"""

