# Game Setup
WIDTH = 1280
HEIGTH = 720
FPS = 60

# Map Data
horizon_y = 500
left_border = 100
right_border = 1100

# Character Data
chara_img = {
    "Slime": {
        "image_player": "Python/BattleSlime/Character/Slime.PNG",
        "image_enemy": "Python/BattleSlime/Character/Slime_e.PNG",
    },
    "Block": {
        "image_player": "Python/BattleSlime/Character/Block.PNG",
        "image_enemy": "Python/BattleSlime/Character/Block_e.PNG",
    },
    "Maru": {
        "image_player": "Python/BattleSlime/Character/Maru.PNG",
        "image_enemy": "Python/BattleSlime/Character/Maru_e.PNG",
    },
    "Takai": {
        "image_player": "Python/BattleSlime/Character/Takai.PNG",
        "image_enemy": "Python/BattleSlime/Character/Takai_e.PNG",
    },
    "Tobu": {
        "image_player": "Python/BattleSlime/Character/Tobu.PNG",
        "image_enemy": "Python/BattleSlime/Character/Tobu_e.PNG",
    },
    "Metal": {
        "image_player": "Python/BattleSlime/Character/Metal.PNG",
        "image_enemy": "Python/BattleSlime/Character/Metal_e.PNG",
    },
    "Bomb": {
        "image_player": "Python/BattleSlime/Character/Bomb.PNG",
        "image_enemy": "Python/BattleSlime/Character/Bomb_e.PNG",
    },
    "Twin": {
        "image_player": "Python/BattleSlime/Character/Twin.PNG",
        "image_enemy": "Python/BattleSlime/Character/Twin_e.PNG",
    },
    "Unicorn": {
        "image_player": "Python/BattleSlime/Character/Unicorn.PNG",
        "image_enemy": "Python/BattleSlime/Character/Unicorn_e.PNG",
    },
}

chara_data = {
    "Slime": {
        "cost": 10,
        "add_money": 10,
        "health": 100,
        "speed": 2,
        "atk": 10,
        "atk_range": 100,
        "speed": 2,
        "knock_distance": 30,
        "cooldown": 700,
        "flyable": False,
    },
    "Block": {
        "cost": 10,
        "add_money": 10,
        "health": 100,
        "speed": 2,
        "atk": 10,
        "atk_range": 100,
        "speed": 2,
        "knock_distance": 30,
        "cooldown": 700,
        "flyable": False,
    },
    "Maru": {
        "cost": 10,
        "add_money": 10,
        "health": 100,
        "speed": 2,
        "atk": 10,
        "atk_range": 100,
        "speed": 2,
        "knock_distance": 30,
        "cooldown": 700,
        "flyable": False,
    },
    "Takai": {
        "cost": 10,
        "add_money": 10,
        "health": 100,
        "speed": 2,
        "atk": 10,
        "atk_range": 100,
        "speed": 2,
        "knock_distance": 30,
        "cooldown": 700,
        "flyable": False,
    },
    "Tobu": {
        "cost": 10,
        "add_money": 10,
        "health": 100,
        "speed": 2,
        "atk": 10,
        "atk_range": 200,
        "speed": 2,
        "knock_distance": 100,
        "cooldown": 700,
        "flyable": True,
    },
    "Metal": {
        "cost": 10,
        "add_money": 10,
        "health": 100,
        "speed": 2,
        "atk": 10,
        "atk_range": 100,
        "speed": 2,
        "knock_distance": 30,
        "cooldown": 700,
        "flyable": False,
    },
    "Bomb": {
        "cost": 10,
        "add_money": 10,
        "health": 100,
        "speed": 2,
        "atk": 10,
        "atk_range": 100,
        "speed": 2,
        "knock_distance": 30,
        "cooldown": 700,
        "flyable": False,
    },
    "Twin": {
        "cost": 10,
        "add_money": 10,
        "health": 100,
        "speed": 2,
        "atk": 10,
        "atk_range": 100,
        "speed": 2,
        "knock_distance": 30,
        "cooldown": 700,
        "flyable": False,
    },
    "Unicorn": {
        "cost": 10,
        "add_money": 10,
        "health": 100,
        "speed": 2,
        "atk": 10,
        "atk_range": 100,
        "speed": 2,
        "knock_distance": 30,
        "cooldown": 700,
        "flyable": False,
    },
}

enemy_list = [
    "Slime",
    "Block",
    "Maru",
    "Takai",
    "Tobu",
    "Metal",
    "Bomb",
    "Twin",
    "Unicorn",
]


# Button Setting
button_data = {
    "Slime": "Python/BattleSlime/Button/Slime_bt.PNG",
    "Block": "Python/BattleSlime/Button/Block_bt.PNG",
    "Maru": "Python/BattleSlime/Button/Maru_bt.PNG",
    "Takai": "Python/BattleSlime/Button/Takai_bt.PNG",
    "Tobu": "Python/BattleSlime/Button/Tobu_bt.PNG",
    "Metal": "Python/BattleSlime/Button/Metal_bt.PNG",
    "Bomb": "Python/BattleSlime/Button/Bomb_bt.PNG",
    "Twin": "Python/BattleSlime/Button/Twin_bt.PNG",
    "Unicorn": "Python/BattleSlime/Button/Unicorn_bt.PNG",
}
button_x_pos = [340, 490, 640, 790, 940]
