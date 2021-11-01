import pyxel
from Player import *
from Asteroid import *
from Enemy import *
from settings import *


class Game:
    def __init__(self):
        self.player = Player()
        self.width = game["width"]
        self.height = game["height"]
        self.caption = game["caption"]
        self.fps = game["fps"]
        pyxel.init(self.width, self.height, caption=self.caption, fps=self.fps, quit_key=pyxel.KEY_ESCAPE)
        pyxel.load("Minuet_in_G.pyxres")
        #pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def count_execution_time(self):
        game["elapsed_time"] += game["frame"]

    def addnewrecord(self, nickname, points):
        records = [line.split(",") for line in open("records.csv")]
        records.append([len(records) + 1, nickname, points])
        records.sort(key=lambda x: -int(x[2]))
        records = records[:5]
        with open("records.csv", 'w') as data:
            for r in records:
                r[0] = records.index(r) + 1
                r[2] = str(r[2])
                r[2] = r[2] + "\n" if "\n" not in r[2] else r[2]
                line = str(r[0]) + "," + str(r[1]) + "," + r[2]
                data.write(line)

    def drawhome(self):
        pyxel.text(game["width"] / 2 - len("Welcome to the") * 2, game["height"] / 3, "Welcome to the",
                   pyxel.COLOR_WHITE)
        pyxel.text(game["width"] / 2 - len("Asteroids Game!") * 2, game["height"] / 2, "Asteroids Game!",
                   pyxel.COLOR_WHITE)
        pyxel.text(game["width"] / 2 - len("Press Space to start") * 2, game["height"] / 1.5,
                   "Press Space to start", pyxel.COLOR_YELLOW)
        pyxel.text(1, game["height"] - 10, "[R]Records", pyxel.COLOR_RED)
        pyxel.text(game["width"] - 4 * len("[Esc]Exit"), game["height"] - 10, "[Esc]Exit", pyxel.COLOR_WHITE)

    def drawrecords(self):
        pyxel.text(game["width"] / 2 - len("Records") * 2, 10, "Records",
                   pyxel.COLOR_RED)
        pyxel.text(1, game["height"] - 10, "[B] Back", pyxel.COLOR_WHITE)

        with open("records.csv") as data:
            records = [line.split(",") for line in data]
        for i in range(len(records)):
            pyxel.text(10, 20 + 10 * i, "%s- " % records[i][0], pyxel.COLOR_YELLOW)
            pyxel.text(16, 20 + 10 * i, " " + records[i][1], pyxel.COLOR_WHITE)
            pyxel.text(game["width"] - 30, 20 + 10 * i, records[i][2], pyxel.COLOR_YELLOW)

    def drawgameover(self):
        pyxel.text(game["width"] / 2 - len("GAME OVER") * 2, 10, "GAME OVER",
                   pyxel.COLOR_RED)

        pyxel.text(1, game["height"] / 3, "Points: %s" % self.player.points, pyxel.COLOR_WHITE)
        pyxel.text(1, game["height"] / 2, "Nickname (max. 15): ", pyxel.COLOR_YELLOW)
        pyxel.text(1, game["height"] / 1.5, self.player.nickname, pyxel.COLOR_WHITE)
        pyxel.text(game["width"] / 2 + 10, game["height"] - 10, "[Enter] End", pyxel.COLOR_DARKBLUE)

    def drawplaying(self):
        self.player.draw()
        for b in bullet["bullets"]: b.draw()
        for a in asteroid["asteroids"]: a.draw()
        for e in enemy["enemies"]: e.draw()

    def setpage(self, page, key=""):
        if key == "": game["page"] = page
        elif pyxel.btn(key): game["page"] = page

    def update(self):
        self.count_execution_time()
        if game["page"] == "home":
            pyxel.cls(pyxel.COLOR_BLACK)
            self.setpage("playing", pyxel.KEY_SPACE)
            self.setpage("records", pyxel.KEY_R)
        elif game["page"] == "playing":
            pyxel.cls(pyxel.COLOR_BLACK)
            if not self.player.controls_active and (game["elapsed_time"] - self.player.last_death) > self.player.respawn_time:
                self.player.controls_active = True
            self.player.shot(), self.player.move(), self.player.teleport(), self.player.verify_collision()
            if self.player.lives == 0: self.setpage("gameover")
            for b in bullet["bullets"]:
                b.move(), b.check_limit()
                self.player.points += b.verify_collision()
            Asteroid(), Enemy()
            for a in asteroid["asteroids"]: a.move(), a.check_limit()
            for e in enemy["enemies"]: e.move(), e.shot()
        elif game["page"] == "records":
            pyxel.cls(pyxel.COLOR_BLACK)
            self.setpage("home", pyxel.KEY_B)
        elif game["page"] == "gameover":
            pyxel.cls(pyxel.COLOR_BLACK)
            self.player.setnickname()
            if pyxel.btn(pyxel.KEY_ENTER):
                self.addnewrecord(self.player.nickname, self.player.points)
                self.player.reset(hard_reset=True)
                self.setpage("home")

    def draw(self):
        if game["page"] == "home": self.drawhome()
        elif game["page"] == "playing": self.drawplaying()
        elif game["page"] == "records": self.drawrecords()
        elif game["page"] == "gameover": self.drawgameover()

