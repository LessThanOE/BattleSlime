# Game Setup
WIDTH = 1280
HEIGTH = 720
FPS = 60

BLUE = (61, 202, 245, 96)
RED = (217, 80, 102, 85)

# Map Data
horizon_y = 500
left_border = 100
right_border = 1100

# Character Data
chara_img = {
    "Slime": {
        "image_player": "Entity/Character/Slime.PNG",
        "image_enemy": "Entity/Character/Slime_enemy.PNG",
    },
    "Block": {
        "image_player": "Entity/Character/Block.PNG",
        "image_enemy": "Entity/Character/Block_enemy.PNG",
    },
    "Maru": {
        "image_player": "Entity/Character/Maru.PNG",
        "image_enemy": "Entity/Character/Maru_enemy.PNG",
    },
    "Takai": {
        "image_player": "Entity/Character/Takai.PNG",
        "image_enemy": "Entity/Character/Takai_enemy.PNG",
    },
    "Tobu": {
        "image_player": "Entity/Character/Tobu.PNG",
        "image_enemy": "Entity/Character/Tobu_enemy.PNG",
    },
    "Metal": {
        "image_player": "Entity/Character/Metal.PNG",
        "image_enemy": "Entity/Character/Metal_enemy.PNG",
    },
    "Bomb": {
        "image_player": "Entity/Character/Bomb.PNG",
        "image_enemy": "Entity/Character/Bomb_enemy.PNG",
    },
    "Twin": {
        "image_player": "Entity/Character/Twin.PNG",
        "image_enemy": "Entity/Character/Twin_enemy.PNG",
    },
    "Unicorn": {
        "image_player": "Entity/Character/Unicorn.PNG",
        "image_enemy": "Entity/Character/Unicorn_enemy.PNG",
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
    "Slime": "Button/Slime_button.PNG",
    "Block": "Button/Block_button.PNG",
    "Maru": "Button/Maru_button.PNG",
    "Takai": "Button/Takai_button.PNG",
    "Tobu": "Button/Tobu_button.PNG",
    "Metal": "Button/Metal_button.PNG",
    "Bomb": "Button/Bomb_button.PNG",
    "Twin": "Button/Twin_button.PNG",
    "Unicorn": "Button/Unicorn_button.PNG",
}
button_x_pos = [340, 490, 640, 790, 940]
