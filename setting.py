# Game Setup
WIDTH = 1280
HEIGTH = 720
FPS = 60

# Map Data
horizon_y = 500

# Character Data
chara_img = {
    'Slime' : {'image_player' : 'Python/BattleSlime/Character/Slime.PNG',
               'image_enemy' : 'Python/BattleSlime/Character/Slime_e.PNG'},
    'Block' : {'image_player' : 'Python/BattleSlime/Character/Block.PNG',
               'image_enemy' : 'Python/BattleSlime/Character/Block_e.PNG'},
    'Maru' :  {'image_player' : 'Python/BattleSlime/Character/Maru.PNG',
               'image_enemy' : 'Python/BattleSlime/Character/Maru_e.PNG'},
    'Takai' : {'image_player' : 'Python/BattleSlime/Character/Takai.PNG',
               'image_enemy' : 'Python/BattleSlime/Character/Takai_e.PNG'},
    'Tobu' : {'image_player' : 'Python/BattleSlime/Character/Tobu.PNG',
               'image_enemy' : 'Python/BattleSlime/Character/Tobu_e.PNG'},
    'Metal' : {'image_player' : 'Python/BattleSlime/Character/Metal.PNG',
               'image_enemy' : 'Python/BattleSlime/Character/Metal_e.PNG'},
    'Bomb' : {'image_player' : 'Python/BattleSlime/Character/Bomb.PNG',
               'image_enemy' : 'Python/BattleSlime/Character/Bomb_e.PNG'},
    'Twin' : {'image_player' : 'Python/BattleSlime/Character/Twin.PNG',
               'image_enemy' : 'Python/BattleSlime/Character/Twin_e.PNG'},
    'Unicorn' : {'image_player' : 'Python/BattleSlime/Character/Unicorn.PNG',
               'image_enemy' : 'Python/BattleSlime/Character/Unicorn_e.PNG'},
}

chara_data = {
    'Slime' :   {'health' : 100,    'atk': 1,   'atk_range' : 100,     'speed' : 2,    'flyable' : False,  'AOE' : False},
    'Block' :   {'health' : 1000,   'atk': 0.5, 'atk_range' : 100,     'speed' : 1,    'flyable' : False,  'AOE' : False},
    'Maru' :    {'health' : 100,    'atk': 1,   'atk_range' : 100,     'speed' : 5,    'flyable' : False,  'AOE' : False},
    'Takai' :   {'health' : 200,    'atk': 2,   'atk_range' : 100,     'speed' : 2,    'flyable' : False,  'AOE' : False},
    'Tobu' :    {'health' : 100,    'atk': 1,   'atk_range' : 200,     'speed' : 3,    'flyable' : True,   'AOE' : False},
    'Metal' :   {'health' : 100,    'atk': 1,   'atk_range' : 100,     'speed' : 1,    'flyable' : False,  'AOE' : False},
    'Bomb' :    {'health' : 50,     'atk': 50,  'atk_range' : 150,     'speed' : 2,    'flyable' : False,  'AOE' : True},
    'Twin' :    {'health' : 300,    'atk': 3,   'atk_range' : 100,     'speed' : 2,    'flyable' : False,  'AOE' : False},
    'Unicorn' : {'health' : 200,    'atk': 10,  'atk_range' : 100,     'speed' : 1,    'flyable' : False,  'AOE' : True}
}

enemy_list = ['Slime', 'Block', 'Maru', 'Takai', 'Tobu', 'Metal', 'Bomb', 'Twin', 'Unicorn']


# Button Setting
button_data = {
    'Slime' : 'Python/BattleSlime/Button/Slime_bt.PNG',
    'Block' : 'Python/BattleSlime/Button/Block_bt.PNG',
    'Maru' : 'Python/BattleSlime/Button/Maru_bt.PNG',
    'Takai' : 'Python/BattleSlime/Button/Takai_bt.PNG',
    'Tobu' : 'Python/BattleSlime/Button/Tobu_bt.PNG',
    'Metal' : 'Python/BattleSlime/Button/Metal_bt.PNG',
    'Bomb' : 'Python/BattleSlime/Button/Bomb_bt.PNG',
    'Twin' : 'Python/BattleSlime/Button/Twin_bt.PNG',
    'Unicorn' : 'Python/BattleSlime/Button/Unicorn_bt.PNG'
}
button_x_pos = [340, 490, 640, 790, 940]
