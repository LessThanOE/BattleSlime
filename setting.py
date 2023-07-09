# Game Setup
WIDTH = 1280
HEIGTH = 720
FPS = 60

# Character Data
chara_data = {
    'Slime' : {'image' : 'Python/BattleSlime/Character/Slime.PNG', 'health' : 100, 'max_health': 100, 'atk' : 1, 'speed' : 2},
    'Block' : {'image' : 'Python/BattleSlime/Character/Block.PNG', 'health' : 500, 'max_health': 500, 'atk' : 0.5, 'speed' : 1},
    'Maru' : {'image' : 'Python/BattleSlime/Character/Maru.PNG', 'health' : 100, 'max_health': 100, 'atk' : 1, 'speed' : 5},
    'Takai' : {'image' : 'Python/BattleSlime/Character/Takai.PNG', 'health' : 200, 'max_health': 200, 'atk' : 2, 'speed' : 2},
    'Tobu' : {'image' : 'Python/BattleSlime/Character/Tobu.PNG', 'health' : 100, 'max_health': 100, 'atk' : 1, 'speed' : 3},
    'Metal' : {'image' : 'Python/BattleSlime/Character/Metal.PNG', 'health' : 100, 'max_health': 100, 'atk' : 1, 'speed' : 1},
    'Bomb' : {'image' : 'Python/BattleSlime/Character/Bomb.PNG', 'health' : 10, 'max_health': 10, 'atk' : 100, 'speed' : 2},
    'Twin' : {'image' : 'Python/BattleSlime/Character/Twin.PNG', 'health' : 300, 'max_health': 300, 'atk' : 3, 'speed' : 2},
    'Unicorn' : {'image' : 'Python/BattleSlime/Character/Unicorn.PNG', 'health' : 200, 'max_health': 200, 'atk' : 10, 'speed' : 1}
}

# Enemy Data
enemy_data = {
    'Slime' : {'image' : 'Python/BattleSlime/Character/Slime_wh.PNG', 'health' : 100, 'max_health': 100, 'atk' : 1, 'speed' : 2},
    'Block' : {'image' : 'Python/BattleSlime/Character/Block_wh.PNG', 'health' : 500, 'max_health': 500, 'atk' : 0.5, 'speed' : 1},
    'Maru' : {'image' : 'Python/BattleSlime/Character/Maru_wh.PNG', 'health' : 100, 'max_health': 100, 'atk' : 1, 'speed' : 5},
    'Takai' : {'image' : 'Python/BattleSlime/Character/Takai_wh.PNG', 'health' : 200, 'max_health': 200, 'atk' : 2, 'speed' : 2},
    'Tobu' : {'image' : 'Python/BattleSlime/Character/Tobu_wh.PNG', 'health' : 100, 'max_health': 100, 'atk' : 1, 'speed' : 3},
    'Metal' : {'image' : 'Python/BattleSlime/Character/Metal_wh.PNG', 'health' : 100, 'max_health': 100, 'atk' : 1, 'speed' : 1},
    'Bomb' : {'image' : 'Python/BattleSlime/Character/Bomb_wh.PNG', 'health' : 10, 'max_health': 10, 'atk' : 100, 'speed' : 2},
    'Twin' : {'image' : 'Python/BattleSlime/Character/Twin_wh.PNG', 'health' : 300, 'max_health': 300, 'atk' : 3, 'speed' : 2},
    'Unicorn' : {'image' : 'Python/BattleSlime/Character/Unicorn_wh.PNG', 'health' : 200, 'max_health': 200, 'atk' : 10, 'speed' : 1}
}
enemy_list = ['Slime', 'Block', 'Maru', 'Takai', 'Tobu', 'Metal', 'Bomb', 'Twin', 'Unicorn']


# Button Setting
button_data = {
    'Slime' : 'Python/BattleSlime/Button/Slime_bt.PNG',
    'Block' : 'Python/BattleSlime/Button/Block_bt.PNG',
    'Maru' : 'Python/BattleSlime/Button/Maru_bt.PNG',
    'Takai' : 'Python/BattleSlime/Button/Takai_bt.PNG',
    'Tobu' : 'Python/BattleSlime/Button/Tobu_bt.PNG',
    'Metal' : 'Python/BattleSlime/Button/Metal_bbt.PNG',
    'Bomb' : 'Python/BattleSlime/Button/Bomb_bt.PNG',
    'Twin' : 'Python/BattleSlime/Button/Twin_bt.PNG',
    'Unicorn' : 'Python/BattleSlime/Button/Unicorn_bt.PNG'
}
button_x_pos = [340, 490, 640, 790, 940]
