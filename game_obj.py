import pygame
import os
import csv

class saw():
    img = [pygame.transform.scale(pygame.image.load(os.path.join('png', 'SAW0.png')), (64, 64)), pygame.transform.scale(pygame.image.load(os.path.join('png', 'SAW1.png')), (64, 64)), pygame.transform.scale(pygame.image.load(os.path.join('png', 'SAW2.png')), (64, 64)), pygame.transform.scale(pygame.image.load(os.path.join('png', 'SAW3.png')), (64, 64))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x, y, width, height)
        self.count = 0
        self.safespot = x

    def draw (self, screen):
        if self.count >= 8:
            self.count = 0
        screen.blit(self.img[self.count // 2], (self.x, self.y))
        self.count += 1

    def update_position(self, change):
        if change == -45:
            self.x = self.safespot
        else:
            self.x += change

class Tile():
    def __init__(self, image, x, y):
        self.image = pygame.transform.scale(pygame.image.load(image), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


class TileMap():
    def __init__(self, filename):
        self.tile_size = 32
        self.start_x, self.start_y = 0, 558
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def draw_map(self, surface, bgX):
        surface.blit(self.map_surface, (bgX, 558))

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map

    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
        x, y = 0, 0

        for row in map:
            x = 0

            for tile in row:
                if tile == '-1':
                    self.start_x = x * self.tile_size
                    self.start_y += y * self.tile_size
                elif tile == '1' or tile == '2':
                    tiles.append(Tile(os.path.join('Tiles', 'Tile (2).png'), x * self.tile_size, (y * self.tile_size)))
                elif tile == '0':
                    tiles.append(Tile(os.path.join('Tiles', 'Tile (1).png'), x * self.tile_size, y * self.tile_size))
                elif tile == '3' or tile == '6':
                    tiles.append(Tile(os.path.join('Tiles', 'Tile (4).png'), x * self.tile_size, y * self.tile_size))
                elif tile == '4' or tile == '7' or tile == '8':
                    tiles.append(Tile(os.path.join('Tiles', 'Tile (5).png'), x * self.tile_size, y * self.tile_size))


                    # Move to next tile in current row
                x += 1

            # Move to next row
            y += 1
            # Store the size of the tile map
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size

        return tiles

