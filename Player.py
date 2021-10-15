import pyxel
from settings import *
from Bullet import *
from math import sin, cos, radians


class Player:
    def __init__(self):
        self.x = player["beginningx"] / 2
        self.y = player["beginningy"] / 2
        self.speed = 0
        self.rotation = player["beginning_rotation"]
        self.newrotation = player["beginning_rotation"]
        self.points = 0

    def draw(self):
        pyxel.rect(self.x, self.y, 2, 2, pyxel.COLOR_ORANGE)

    def move(self):
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            self.newrotation += 0.5
            self.rotation = self.newrotation if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W) else self.rotation
        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
            self.newrotation -= 0.5
            self.rotation = self.newrotation if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W) else self.rotation
        elif pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W):
            self.rotation = self.newrotation
            self.speed = 20

        self.x += self.speed * cos(radians(self.rotation)) * game["frame"]
        self.y += self.speed * sin(radians(self.rotation)) * game["frame"]

    def teleport(self):
        if self.x < 0:
            self.x = game["width"]
        elif self.x > game["width"]:
            self.x = 0
        elif self.y < 0:
            self.y = game["height"]
        elif self.y > game["height"]:
            self.y = 0

    def shot(self):
        if pyxel.btnp(pyxel.KEY_SPACE) and (game["elapsed_time"] - bullet["last_shot"]) >= bullet["limit_time"]:
            bullet["bullets"].append(Bullet(self.x, self.y, self.rotation))
            bullet["last_shot"] = game["elapsed_time"]


    def verify_collision(self):
        for a in asteroid["asteroids"]:
            if sqrt((a.x - self.x) ** 2 + (a.y - self.y) ** 2) < a.size:
                return True
            else: return False

