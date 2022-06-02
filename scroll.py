import pygame
import time
import sys
import player
import game_obj as object


bg_img = pygame.image.load('BG.png')
res = (750, 705)
screen = pygame.display.set_mode(res)
spaceChange = 0

speed = 5
knight = player.player(125, 648, 100, 100)
map = object.TileMap('game_map.csv')
saww = object.saw(225, 586, 64, 64)


def redrawWindow(screen, bgX):
    screen.blit(bg_img, (bgX, 0))
    map.draw_map(screen, bgX)
    saww.draw(screen)
    knight.update(map.tiles, screen)

    pygame.display.update()  # updates the screen


def game_screen(speed):

    bg_img = pygame.image.load('BG.png')
    bgX = 0
    start = time.time()
    while True:

        Font = pygame.font.SysFont('Calibre', 75)
        text = Font.render('Level 1', True, (255, 255, 255))
        screen.blit(text, (res[0]/5, res[1]/2))
        pygame.display.update()
        end = time.time()
        if end - start > 2:
            break

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and not (keys[pygame.K_d]) and not (bgX >= 125):
            bgX += speed
            map.start_x += speed
            saww.x += speed
            knight.runningBack = True
        if keys[pygame.K_d] and not (keys[pygame.K_a]):
            if not (keys[pygame.K_RSHIFT]) or knight.jumping:
                if not (bgX <= -1700):
                    bgX -= speed
                    saww.x -= speed
                    map.start_x -= speed
                knight.walking = True
            else:
                if not (bgX <= -1700):
                    bgX -= 3 * speed
                    saww.x -= 3 * speed
                    map.start_x -= 3 * speed


                knight.running = True

        if keys[pygame.K_w]:  # If user hits w
            if not (knight.jumping):  # If we are not already jumping
                knight.jumping = True


        redrawWindow(screen, bgX)
        knight.running = False
        knight.runningBack = False
        knight.walking = False



