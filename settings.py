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
    "max_lives": 3,
    "trisize": 6,
    "beginning_speed": 0,
    "beginning_points": 0,
    "nickname": "",
    "respawn_time": 3,
    "color": 9
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

