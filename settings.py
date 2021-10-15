game = {
    "width": 120,
    "height": 80,
    "caption": "Asteroids Game (Version II)",
    "fps": 60,
    "frame": 1/60,
    "elapsed_time": 0,
    "page": "home"
}

player = {
    "beginningx": game["width"],
    "beginningy": game["height"],
    "beginning_rotation": -90,
    "points": 0
}

bullet = {
    "speed": 100,
    "limit_time": 0.3,
    "last_shot": 0,
    "bullets": []
}

asteroid = {
    "asteroids": [],
    "speed": 4,
    "limit_time": 1,
    "last_spawn": 0,
    "radius": [2, 3, 4]
}

