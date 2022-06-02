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
                self.hit_box = pygame.Rect((self.x + 4, self.y), (self.width - 24, self.height - 10))
            elif self.running:
                if self.runCount > 42:
                    self.runCount = 0
                screen.blit(self.run[self.runCount // 6], (self.x, self.y))
                self.runCount += 1
                self.hit_box = pygame.Rect((self.x + 4, self.y), (self.width - 24, self.height - 13))
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
                self.hit_box = pygame.Rect((self.x + 4, self.y), (self.width - 24, self.height - 10))
            elif self.walking:
                if self.walkCount > 42:
                    self.walkCount = 0
                screen.blit(self.walk[self.walkCount // 6], (self.x, self.y))
                self.hit_box = pygame.Rect((self.x + 4, self.y), (self.width - 24, self.height - 10))
                self.walkCount += 1





    def get_hits(self, tiles):
        def check_collision(player_rect, target_rect):

            #< rect(129, 547, 76, 90) > < rect(192, 160, 32, 32) >
            pass

        hits = []
        for i in tiles:
            print(i.rect)
        new_tiles = filter(lambda tile:self.hit_box[0]+self.hit_box.width >= tile.rect.x >= self.hit_box[0] and tile.rect.y < 159, tiles)
        for new_tile in list(new_tiles):
            #print(self.hit_box, new_tile.rect)
            new_tile.rect[1] += 558
            '''if self.hit_box.colliderect(new_tile.rect):
                hits.append(new_tile.rect)
                print(True)'''

            new_tile.rect[1] -= 558

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
            if self.jumpList[self.jumpCount] * 1.2 < 0:  # Hit tile from the top
                self.jumping = False
                #self.velocity.y = 0
                self.y = tile.y - self.height + 558
                '''self.rect.bottom = self.position.y'''
            #elif self.y > tile.y:  # Hit tile from the bottom

                #while self.y != 0:
                    #self.y -= 20
                #self.jumping = False
                '''self.position.y = tile.rect.bottom + self.rect.h
                self.rect.bottom = self.position.y'''

    def update(self, tiles, screen):
        self.draw(screen)
        if self.jumping:
            self.checkCollisionsy(tiles)