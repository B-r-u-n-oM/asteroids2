import pyxel
from settings import *
from Bullet import *
from math import sin, cos, radians


class Player:
    def __init__(self):
        self.x = player["beginningx"] / 2
        self.y = player["beginningy"] / 2
        self.tricoordinates = {
            "x1": 0, "y1": 0, "x2": 0, "y2": 0, "x3": 0, "y3": 0
        }
        self.trisize = player["trisize"]
        self.speed = player["beginning_speed"]
        self.rotation = player["beginning_rotation"]
        self.newrotation = player["beginning_rotation"]
        self.points = player["beginning_points"]
        self.lives = player["max_lives"]
        self.nickname = player["nickname"]
        self.lastcollision = player["lastcollision"]

    def draw(self):
        pyxel.trib(
            self.tricoordinates["x1"], self.tricoordinates["y1"],
            self.tricoordinates["x2"], self.tricoordinates["y2"],
            self.tricoordinates["x3"], self.tricoordinates["y3"],
            pyxel.COLOR_ORANGE)

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

        self.tricoordinates["x1"] = self.x + cos(radians(self.newrotation)) * (self.trisize/2) / cos(radians(30))
        self.tricoordinates["y1"] = self.y + sin(radians(self.newrotation)) * (self.trisize/2) / cos(radians(30))
        self.tricoordinates["x2"] = self.x + cos(radians(self.newrotation + 120)) * (self.trisize/2) / cos(radians(30))
        self.tricoordinates["y2"] = self.y + sin(radians(self.newrotation + 120)) * (self.trisize/2) / cos(radians(30))
        self.tricoordinates["x3"] = self.x + cos(radians(self.newrotation + 240)) * (self.trisize/2) / cos(radians(30))
        self.tricoordinates["y3"] = self.y + sin(radians(self.newrotation + 240)) * (self.trisize/2) / cos(radians(30))

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
                self.lives -= 1
                self.respawn()

    def respawn(self):

        self.x = player["beginningx"] / 2
        self.y = player["beginningy"] / 2
        self.tricoordinates = {
            "x1": 0, "y1": 0, "x2": 0, "y2": 0, "x3": 0, "y3": 0
        }
        self.speed = player["beginning_speed"]
        self.rotation = player["beginning_rotation"]
        self.newrotation = player["beginning_rotation"]

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
            self.nickname += "a"
        elif pyxel.btnp(pyxel.KEY_B):
            self.nickname += "b"
        elif pyxel.btnp(pyxel.KEY_C):
            self.nickname += "c"
        elif pyxel.btnp(pyxel.KEY_D):
            self.nickname += "d"
        elif pyxel.btnp(pyxel.KEY_E):
            self.nickname += "e"
        elif pyxel.btnp(pyxel.KEY_F):
            self.nickname += "f"
        elif pyxel.btnp(pyxel.KEY_G):
            self.nickname += "g"
        elif pyxel.btnp(pyxel.KEY_H):
            self.nickname += "h"
        elif pyxel.btnp(pyxel.KEY_I):
            self.nickname += "i"
        elif pyxel.btnp(pyxel.KEY_J):
            self.nickname += "j"
        elif pyxel.btnp(pyxel.KEY_K):
            self.nickname += "k"
        elif pyxel.btnp(pyxel.KEY_L):
            self.nickname += "l"
        elif pyxel.btnp(pyxel.KEY_M):
            self.nickname += "m"
        elif pyxel.btnp(pyxel.KEY_N):
            self.nickname += "n"
        elif pyxel.btnp(pyxel.KEY_O):
            self.nickname += "o"
        elif pyxel.btnp(pyxel.KEY_P):
            self.nickname += "p"
        elif pyxel.btnp(pyxel.KEY_Q):
            self.nickname += "q"
        elif pyxel.btnp(pyxel.KEY_R):
            self.nickname += "r"
        elif pyxel.btnp(pyxel.KEY_S):
            self.nickname += "s"
        elif pyxel.btnp(pyxel.KEY_T):
            self.nickname += "t"
        elif pyxel.btnp(pyxel.KEY_U):
            self.nickname += "u"
        elif pyxel.btnp(pyxel.KEY_V):
            self.nickname += "v"
        elif pyxel.btnp(pyxel.KEY_W):
            self.nickname += "w"
        elif pyxel.btnp(pyxel.KEY_X):
            self.nickname += "x"
        elif pyxel.btnp(pyxel.KEY_Y):
            self.nickname += "y"
        elif pyxel.btnp(pyxel.KEY_Z):
            self.nickname += "z"
        elif pyxel.btnp(pyxel.KEY_0):
            self.nickname += "0"
        elif pyxel.btnp(pyxel.KEY_1):
            self.nickname += "1"
        elif pyxel.btnp(pyxel.KEY_2):
            self.nickname += "2"
        elif pyxel.btnp(pyxel.KEY_3):
            self.nickname += "3"
        elif pyxel.btnp(pyxel.KEY_4):
            self.nickname += "4"
        elif pyxel.btnp(pyxel.KEY_5):
            self.nickname += "5"
        elif pyxel.btnp(pyxel.KEY_6):
            self.nickname += "6"
        elif pyxel.btnp(pyxel.KEY_7):
            self.nickname += "7"
        elif pyxel.btnp(pyxel.KEY_8):
            self.nickname += "8"
        elif pyxel.btnp(pyxel.KEY_9):
            self.nickname += "9"

