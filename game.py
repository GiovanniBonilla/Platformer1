# Giovanni Bonilla, gqk5bm, and Noura Alghamdi, nwm3fj
# Final Submission
# You are a radical skateboarder that knows a door that leads to free zaza, but the puppet monsters are\
# Scouring the world looking for you, so you must avoid them to get to the door
# User input implemented through vertical movement using left and right arrow keys, as well as\
# Horizontal movement using the up arrow
# Game Over is implemented because when you touch the enemies too much and your health reaches 0,\
# Well, you die, and also hitting the floor is an automatic death, and death results in\
# Game Over screen and it gives you the option to restart by pressing the space bar
# Local images include a sprite sheet of a skateboarder, a puppet monster sprite sheet, a health bar\
# sprite sheet, and a bamboo door sprite sheet
# Additional feature 1 - Restart from Game Over: when you die or reach the door, you are given the option\
# to restart by pressing the space key, and it brings you back to the start and resets everything
# Additional feature 2 - Sprite Animation: the skateboarder animates when it jumps up, as well as when it\
# crouches by hitting the down arrow key, and it also animates when you reach the end
# Additional feature 3 - Enemies: If you touch any of the enemies, they will knock you upwards and reduce you health,\
# causing you to die, and they also move left and right, as well as flip directions they face
# Additional feature 4 - Scrolling level: level consists of platforms spread out to make it much larger than the camera\
# makes it appear to be
# Additional feature 5 - Health Bar: health bar goes down gradually when you touch an enemy, and when it runs out,\
# the player dies, and falling off the screen results in the health bar completely emptying and an automatic death
# Changes since CP2: Addition of door for when player reaches the end, player no longer bounces off bottom of screen,\
# addition of health bar, camera movement centered on player's position, ditched idea of player attack, addition\
# of restart from game over

import uvage

camera = uvage.Camera(800, 600)
skateboarder_sheet = uvage.load_sprite_sheet("https://opengameart.org/sites/default/files/spritesheet_48.png", 5, 9)
b3 = uvage.from_image(camera.x, camera.y, skateboarder_sheet[20])
b3.image = skateboarder_sheet[10]
# b3.flip()
game_over = False

player_facing_right = False
enemy_facing_right = False

b3_speed = 15

count = 0
floor = uvage.from_color(400, 400, "#964B00", 400, 50)
platform = uvage.from_color(1000, 300, "#964B00", 100, 25)

enemy_sheet = uvage.load_sprite_sheet("https://www.hiddenone-sprites.com/uploads/7/1/8/7/71878507/248379810.png", 6, 9)
e3 = uvage.from_image(800, camera.y, enemy_sheet[20])
e3.image = enemy_sheet[1]
enemy2 = uvage.from_image(1675, 250, enemy_sheet[20])
enemy3 = uvage.from_image(3000, 250, enemy_sheet[20])# platform4
enemy4 = uvage.from_image(4100, 250, enemy_sheet[20])# platform6
enemy5 = uvage.from_image(5500, 250, enemy_sheet[20])# platform9

heart_sprite_sheet = uvage.load_sprite_sheet("Health_Bar.png", 3, 2)
h3 = uvage.from_image(b3.x - 350, 550, enemy_sheet[1])
h3.image = heart_sprite_sheet[0]

heart_list = [heart_sprite_sheet[0], heart_sprite_sheet[2], heart_sprite_sheet[4], heart_sprite_sheet[1], heart_sprite_sheet[3], heart_sprite_sheet[5]]
# health_bar_sheet = uvage.load_sprite_sheet("https://art.pixilart.com/04dbaae0250b710.png", 6, 1)
# hb3 = uvage.from_image(camera.x, camera.y, health_bar_sheet[6])
# hb3.image = health_bar_sheet[5]

door_sheet = uvage.load_sprite_sheet("bamboo-doorv2.png", 2, 7)
d3 = uvage.from_image(6150, 400, enemy_sheet[20])
d3.image = door_sheet[0]
camera.center = [b3.x, b3.y]


def knock_back():
    global count
    global game_over
    b3.speedy = -30
    # if b3.x >= e3.x:
    #     b3.move(20, 0)
    # if b3.x < e3.x:
    #     b3.move(-20, 0)
    if b3.touches(e3) or b3.touches(enemy2) or b3.touches(enemy3) or b3.touches(enemy4) or b3.touches(enemy5):
        h3.image = heart_list[count]
        count += 1
        if count >= 6:
            game_over = True
            game_end()
    elif b3.y >= 600:
        h3.image = heart_list[5]
        game_over = True
        game_end()
    # b3.speedx = -5


def game_end():
    global game_over
    global count
    # timer = 0
    if game_over:
        if b3.touches(d3):
            camera.draw(uvage.from_text(camera.x, camera.y, "YOU WIN!", 60, "black", bold=False, italic=False))
            camera.draw(uvage.from_text(camera.x, camera.y + 50, "Press SPACE to Restart", 60, "black", bold=False,
                                        italic=False))
            if uvage.is_pressing("space"):
                game_over = False
                e3.image = enemy_sheet[1]
                camera.x = 400
                camera.y = 300
                b3.x = 400
                b3.y = camera.y
                e3.x = 800
                e3.y = camera.y
                enemy2.x = 1675
                enemy2.y = 250
                enemy3.x = 2900
                enemy3.y = 250
                enemy4.x = 4100
                enemy4.y = 250
                enemy5.x = 5500
                enemy5.y = 250
                # e3.x =
                count = 0
                h3.image = heart_list[0]
                h3.x = 50
        else:
            camera.draw(uvage.from_text(camera.x, camera.y, "GAME OVER", 60, "black", bold=False, italic=False))
            camera.draw(uvage.from_text(camera.x, camera.y + 50, "Press SPACE to Restart", 60, "black", bold=False, italic=False))
    if b3.touches(e3) or b3.touches(enemy2) or b3.touches(enemy3) or b3.touches(enemy4) or b3.touches(enemy5):
        if not game_over:
            knock_back()
        if game_over:
            if uvage.is_pressing("space"):
                game_over = False
                e3.image = enemy_sheet[1]
                camera.x = 400
                camera.y = 300
                b3.x = 400
                b3.y = camera.y
                e3.x = 800
                e3.y = camera.y
                enemy2.x = 1675
                enemy2.y = 250
                enemy3.x = 2900
                enemy3.y = 250
                enemy4.x = 4100
                enemy4.y = 250
                enemy5.x = 5500
                enemy5.y = 250
                # e3.x =
                count = 0
                h3.image = heart_list[0]
                h3.x = 50
    if b3.y >= 600:
        game_over = True
        camera.draw(uvage.from_text(camera.x, camera.y, "GAME OVER", 60, "black", bold=False, italic=False))
        camera.draw(
            uvage.from_text(camera.x, camera.y + 50, "Press SPACE to Restart", 60, "black", bold=False, italic=False))
        if uvage.is_pressing("space"):
            game_over = False
            e3.image = enemy_sheet[1]
            camera.x = 400
            camera.y = 300
            b3.x = 400
            b3.y = camera.y
            e3.x = 800
            e3.y = camera.y
            enemy2.x = 1675
            enemy2.y = 250
            enemy3.x = 2900
            enemy3.y = 250
            enemy4.x = 4100
            enemy4.y = 250
            enemy5.x = 5500
            enemy5.y = 250
            count = 0
            h3.image = heart_list[0]
            h3.x = 50


def tick():
    global game_over
    global player_facing_right
    global enemy_facing_right
    camera.x = b3.x
    camera.clear('light blue')
    camera.draw(b3)
    camera.draw(e3)
    camera.draw(floor)
    camera.draw(platform)
    platform2 = platform.copy_at(1700, 300)
    camera.draw(platform2)
    platform3 = platform.copy_at(2300, 500)
    camera.draw(platform3)
    platform4 = platform.copy_at(2800, 300)
    camera.draw(platform4)
    platform5 = platform.copy_at(3300, 100)
    camera.draw(platform5)
    platform6 = platform.copy_at(3900, 300)
    camera.draw(platform6)
    platform7 = platform.copy_at(4400, 400)
    camera.draw(platform7)
    platform8 = platform.copy_at(4800, 200)
    camera.draw(platform8)
    platform9 = platform.copy_at(5300, 300)
    camera.draw(platform9)
    platform10 = platform.copy_at(6150, 450)
    camera.draw(platform10)

    camera.draw(d3)

    camera.draw(enemy2)
    camera.draw(enemy3)
    camera.draw(enemy4)
    camera.draw(enemy5)

    camera.draw(h3)

    # camera.draw(hb3)
    # camera.display()

    # hb3.x = 200
    # hb3.y = 500
    # b3.speedy = 10
    # b3.move_speed()
    b3.move_to_stop_overlapping(floor)
    b3.move_to_stop_overlapping(platform)
    b3.move_to_stop_overlapping(platform2)
    b3.move_to_stop_overlapping(platform3)
    b3.move_to_stop_overlapping(platform4)
    b3.move_to_stop_overlapping(platform5)
    b3.move_to_stop_overlapping(platform6)
    b3.move_to_stop_overlapping(platform7)
    b3.move_to_stop_overlapping(platform8)
    b3.move_to_stop_overlapping(platform9)
    b3.move_to_stop_overlapping(platform10)
    e3.move_to_stop_overlapping(floor)

    e3.y = 350

    if b3.touches(floor) or b3.touches(platform) or b3.touches(platform2) or b3.touches(platform3) \
            or b3.touches(platform4) or b3.touches(platform5) or b3.touches(platform6) or b3.touches(platform7)\
            or b3.touches(platform8) or b3.touches(platform9) or b3.touches(platform10):
        b3.image = skateboarder_sheet[10]

    if b3.touches(d3):
        b3.image = skateboarder_sheet[0]
        game_over = True
        game_end()
    b3.speedy += 0.9
    b3.move_speed()

    if not game_over:
        if enemy_facing_right:
            e3.speedx = 10
            e3.move_speed()
            enemy2.speedx = 20
            enemy2.move_speed()
            enemy3.speedx = 10
            enemy3.move_speed()
            enemy4.speedx = 10
            enemy4.move_speed()
            enemy5.speedx = 10
            enemy5.move_speed()
        if not enemy_facing_right:
            e3.speedx = -10
            e3.move_speed()
            enemy2.speedx = -20
            enemy2.move_speed()
            enemy3.speedx = -10
            enemy3.move_speed()
            enemy4.speedx = -10
            enemy4.move_speed()
            enemy5.speedx = -10
            enemy5.move_speed()
        if e3.x <= 30:
            enemy_facing_right = True
            e3.speedx = 0
            e3.flip()
        if e3.x >= 770:
            enemy_facing_right = False
            e3.speedx = 0
            e3.flip()
            e3.flip()
        if enemy2.x <= 730:
            enemy_facing_right = True
            enemy2.speedx = 0
            enemy2.flip()
        if enemy2.x >= 1675:
            enemy_facing_right = False
            enemy2.speedx = 0
            enemy2.flip()
            enemy2.flip()
        if enemy3.x <= 1900:
            enemy_facing_right = True
            enemy3.speedx = 0
            enemy3.flip()
        if enemy3.x >= 3000:
            enemy_facing_right = False
            enemy3.speedx = 0
            enemy3.flip()
            enemy3.flip()
        if enemy4.x <= 3400:
            enemy_facing_right = True
            enemy4.speedx = 0
            enemy4.flip()
        if enemy4.x >= 4600:
            enemy_facing_right = False
            enemy4.speedx = 0
            enemy4.flip()
            enemy4.flip()
        if enemy5.x <= 4800:
            enemy_facing_right = True
            enemy5.speedx = 0
            enemy5.flip()
        if enemy5.x >= 6200:
            enemy_facing_right = False
            enemy5.speedx = 0
            enemy5.flip()
            enemy5.flip()
        if uvage.is_pressing("up arrow"):
            b3.image = skateboarder_sheet[9]
            if b3.bottom_touches(floor) or b3.bottom_touches(platform) or b3.bottom_touches(platform2) \
                    or b3.bottom_touches(platform3) or b3.bottom_touches(platform4) or b3.bottom_touches(platform5) \
                    or b3.bottom_touches(platform6) or b3.bottom_touches(platform7) or b3.bottom_touches(platform8)\
                    or b3.bottom_touches(platform9) or b3.bottom_touches(platform10):
                b3.speedy = -20
        if uvage.is_pressing("left arrow"):
            if player_facing_right:
                player_facing_right = False
                b3.flip()
            b3.x -= b3_speed
            # camera.move(-15, 0)
            h3.move(-15, 0)
        if uvage.is_pressing("right arrow"):
            if not player_facing_right:
                player_facing_right = True
                b3.flip()
            b3.x += b3_speed
            # camera.move(15, 0)
            h3.move(15, 0)
        if uvage.is_pressing("down arrow"):
            b3.image = skateboarder_sheet[18]
        game_end()
    else:
        game_end()

    camera.display()


uvage.timer_loop(30, tick)
