import pygame
import os

class player(object):
    run = [pygame.transform.scale(pygame.image.load(os.path.join("png", 'Run (' + str(x) + ').png')), (75, 75)) for x in range(1, 10)]
    jump = [pygame.transform.scale(pygame.image.load(os.path.join("png", 'Jump (' + str(x) + ').png')), (75, 75)) for x in range(1, 10)]
    walk = [pygame.transform.scale(pygame.image.load(os.path.join("png", 'Walk (' + str(x) + ').png')), (75, 75)) for x in range(1, 10)]
    idle = [pygame.transform.scale(pygame.image.load(os.path.join("png", 'Idle (' + str(x) + ').png')), (75, 75)) for x in range(1, 9)]
    runBack = [pygame.transform.scale(pygame.image.load(os.path.join("png", 'RunBack (' + str(x) + ').png')), (75, 75)) for x in range(1, 10)]

    jumpList = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1,
                -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
                -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.jumpCount = 0
        self.jumpCount = 0
        self.running = False
        self.runningBack = False
        self.runCount = 0
        self.idleCount = 0
        self.walking = False
        self.walkCount = 0
        self.hit_box = pygame.Rect((self.x, self.y), (self.width, self.height))

    def draw(self, screen):
            if self.jumping:
                self.y -= self.jumpList[self.jumpCount] * 1.2
                screen.blit(self.jump[self.jumpCount // 18], (self.x, self.y))
                self.jumpCount += 1
                if self.jumpCount > 108:
                    self.jumpCount = 0
                    self.jumping = False
                    self.runCount = 0

            elif self.running:
                if self.runCount > 42:
                    self.runCount = 0
                screen.blit(self.run[self.runCount // 6], (self.x, self.y))
                self.runCount += 1
            elif not(self.running) and not(self.runningBack) and not(self.walking):
                if self.idleCount > 42:
                    self.idleCount = 0
                screen.blit(self.idle[self.idleCount // 6], (self.x, self.y))
                self.idleCount += 1
            elif self.runningBack:
                if self.runCount > 42:
                    self.runCount = 0
                screen.blit(self.runBack[self.runCount // 6], (self.x, self.y))
                self.runCount += 1
            elif self.walking:
                if self.walkCount > 42:
                    self.walkCount = 0
                screen.blit(self.walk[self.walkCount // 6], (self.x, self.y))
                self.walkCount += 1



    def update(self, pressed_keys):
        if pressed_keys[pygame.K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_s]:
            self.rect.move_ip(0, 5)

    def get_hits(self, tiles):
        hits = []
        for tile in tiles:
            if self.hit_box.colliderect(tile):
                hits.append(tile)
        return hits

    def checkCollisionsx(self, tiles):
        collisions = self.get_hits(tiles)
        for tile in collisions:
            if self.x < tile.x:  # Hit tile moving right
                self.position.x = tile.rect.left - self.rect.w
                self.rect.x = self.position.x
            elif self.velocity.x < 0:  # Hit tile moving left
                self.position.x = tile.rect.right
                self.rect.x = self.position.x

    def checkCollisionsy(self, tiles):
        collisions = self.get_hits(tiles)
        for tile in collisions:
            if self.y < tile.y:  # Hit tile from the top
                self.jumping = False
                #self.velocity.y = 0
                self.y = tile.y + self.height
                '''self.rect.bottom = self.position.y'''
            elif self.y > tile.y:  # Hit tile from the bottom
                while self.y != 0:
                    self.y -= 20
                self.jumping = False
                '''self.position.y = tile.rect.bottom + self.rect.h
                self.rect.bottom = self.position.y'''
