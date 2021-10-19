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
        self.lives = player["max_lives"]
        self.nickname = ""

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
            if sqrt((a.x - self.x) ** 2 + (a.y - self.y) ** 2) < a.size: self.lives -= 1

    def setnickname(self):
        if len(self.nickname) > 15:
            self.nickname = list(self.nickname)
            self.nickname.pop()
            self.nickname = "".join(self.nickname)
        elif pyxel.btnp(pyxel.KEY_BACKSPACE):
            if len(self.nickname):
                self.nickname = list(self.nickname)
                self.nickname.pop()
                self.nickname = "".join(self.nickname)
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.nickname += " "
        elif pyxel.btnp(pyxel.KEY_A):
            self.nickname += "A"
        elif pyxel.btnp(pyxel.KEY_B):
            self.nickname += "B"
        elif pyxel.btnp(pyxel.KEY_C):
            self.nickname += "C"
        elif pyxel.btnp(pyxel.KEY_D):
            self.nickname += "D"
        elif pyxel.btnp(pyxel.KEY_E):
            self.nickname += "E"
        elif pyxel.btnp(pyxel.KEY_F):
            self.nickname += "F"
        elif pyxel.btnp(pyxel.KEY_G):
            self.nickname += "G"
        elif pyxel.btnp(pyxel.KEY_H):
            self.nickname += "H"
        elif pyxel.btnp(pyxel.KEY_I):
            self.nickname += "I"
        elif pyxel.btnp(pyxel.KEY_J):
            self.nickname += "J"
        elif pyxel.btnp(pyxel.KEY_K):
            self.nickname += "K"
        elif pyxel.btnp(pyxel.KEY_L):
            self.nickname += "L"
        elif pyxel.btnp(pyxel.KEY_M):
            self.nickname += "M"
        elif pyxel.btnp(pyxel.KEY_N):
            self.nickname += "N"
        elif pyxel.btnp(pyxel.KEY_O):
            self.nickname += "O"
        elif pyxel.btnp(pyxel.KEY_P):
            self.nickname += "P"
        elif pyxel.btnp(pyxel.KEY_Q):
            self.nickname += "Q"
        elif pyxel.btnp(pyxel.KEY_R):
            self.nickname += "R"
        elif pyxel.btnp(pyxel.KEY_S):
            self.nickname += "S"
        elif pyxel.btnp(pyxel.KEY_T):
            self.nickname += "T"
        elif pyxel.btnp(pyxel.KEY_U):
            self.nickname += "U"
        elif pyxel.btnp(pyxel.KEY_V):
            self.nickname += "V"
        elif pyxel.btnp(pyxel.KEY_W):
            self.nickname += "W"
        elif pyxel.btnp(pyxel.KEY_X):
            self.nickname += "X"
        elif pyxel.btnp(pyxel.KEY_Y):
            self.nickname += "Y"
        elif pyxel.btnp(pyxel.KEY_Z):
            self.nickname += "Z"

