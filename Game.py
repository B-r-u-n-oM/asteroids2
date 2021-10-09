import pyxel
from Player import *
from settings import *


class Game:
    def __init__(self):
        self.player = Player()
        self.elapsedtime = 0
        self.width = game["width"]
        self.height = game["height"]
        self.caption = game["caption"]
        self.fps = game["fps"]
        self.ispaused = True
        pyxel.init(self.width, self.height, caption=self.caption, fps=self.fps)
        pyxel.run(self.update, self.draw)

    def count_execution_time(self):
        self.elapsedtime += game["frame"]

    def update(self):
        self.count_execution_time()
        pyxel.cls(pyxel.COLOR_BLACK)
        self.player.move(), self.player.teleport()
        self.player.shot() if (self.elapsedtime - bullet["last_shot"]) > bullet["limit_time"] else None
        for b in bullet["bullets"]: b.move(), b.check_limit()

    def draw(self):
        self.player.draw()
        for b in bullet["bullets"]: b.draw()

    def state(self):
        if pyxel.btnp(pyxel.KEY_ENTER): self.ispaused = not self.ispaused







