import pyxel
from Player import *
from Asteroid import *
from settings import *


class Game:
    def __init__(self):
        self.player = Player()
        self.elapsedtime = 0
        self.width = game["width"]
        self.height = game["height"]
        self.caption = game["caption"]
        self.fps = game["fps"]
        pyxel.init(self.width, self.height, caption=self.caption, fps=self.fps, quit_key=pyxel.KEY_Q)
        pyxel.run(self.update, self.draw)

    def count_execution_time(self):
        game["elapsed_time"] += game["frame"]

    def update(self):
        if game["page"] == "home":
            pyxel.cls(pyxel.COLOR_BLACK)
            if pyxel.btn(pyxel.KEY_ENTER):game["page"] = "playing"
            elif pyxel.btn(pyxel.KEY_R): game["page"] = "records"
        elif game["page"] == "playing":
            pyxel.cls(pyxel.COLOR_BLACK)
            self.count_execution_time()
            self.player.move(), self.player.teleport(), self.player.shot(), self.player.verify_collision()
            for b in bullet["bullets"]:
                b.move(), b.check_limit()
                self.player.points += b.verify_collision()
            Asteroid()
            for a in asteroid["asteroids"]: a.move(), a.check_limit()
        elif game["page"] == "records":
            pyxel.cls(pyxel.COLOR_BLACK)
            if pyxel.btn(pyxel.KEY_B): game["page"] = "home"

    def draw(self):
        if game["page"] == "home":
            pyxel.text(game["width"] / 2 - len("Welcome to the") * 2, game["height"] / 3, "Welcome to the",
                       pyxel.COLOR_WHITE)
            pyxel.text(game["width"] / 2 - len("Asteroids Game!") * 2, game["height"] / 2, "Asteroids Game!",
                       pyxel.COLOR_WHITE)
            pyxel.text(game["width"] / 2 - len("Press Enter to start") * 2, game["height"] / 1.5,
                       "Press Enter to start", pyxel.COLOR_YELLOW)
            pyxel.text(1, game["height"] - 10, "(R) Records", pyxel.COLOR_RED)
            pyxel.text(game["width"] / 2 + 3 * len("(Q) Quit"), game["height"] - 10, "(Q) Quit", pyxel.COLOR_WHITE)
        elif game["page"] == "playing":
            self.player.draw()
            for b in bullet["bullets"]: b.draw()
            for a in asteroid["asteroids"]: a.draw()
        elif game["page"] == "records":
            pyxel.text(1, game["height"] - 10, "(B) Back", pyxel.COLOR_WHITE)

