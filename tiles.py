import pygame, csv, os

class Tile(pygame.sprite.Sprite):
    def __init__(self, tileid, image, x, y, spritesheet, flip, cancollide, hazard, finish):
        pygame.sprite.Sprite.__init__(self)
        self.tileid = tileid
        if flip:
            self.image = pygame.transform.flip(spritesheet.parse_sprite(image), True, False)
        else:
            self.image = spritesheet.parse_sprite(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.cancollide = cancollide
        self.hazard = hazard
        self.finish = finish

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class TileMap():
    def __init__(self, filename, spritesheet):
        self.tile_size = 75
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def draw_map(self, surface):
        surface.blit(self.map_surface, (0, 0))

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
                if self.spritesheet.filename == 'level1spritesheet.png':
                    # Finish Tile
                    if tile == '29':
                        tiles.append(Tile('29','sprite30', x * self.tile_size, y * self.tile_size, self.spritesheet, False, True, False, True))
                    # Spike(Let player fall through)
                    elif tile == '49':
                        tiles.append(Tile('49','sprite50', x * self.tile_size, y * self.tile_size, self.spritesheet, False, False, False, False))
                    # Dirt(Set as hazard, below spike)
                    elif tile == '100':
                        tiles.append(Tile('100','sprite101', x * self.tile_size, y * self.tile_size, self.spritesheet, False, True, True, False))
                    # Water(Hazard)
                    elif tile == '93':
                        tiles.append(Tile('93','sprite94', x * self.tile_size, y * self.tile_size, self.spritesheet, False, True, True, False))
                    # Sign(Not collidable)
                    elif tile == '141':
                        tiles.append(Tile('141','sprite142', x * self.tile_size, y * self.tile_size, self.spritesheet, False, False, False, False))
                    # Flipped Sign
                    elif tile == '160':
                        tiles.append(Tile('160','sprite142', x * self.tile_size, y * self.tile_size, self.spritesheet, True, False, False, False))
                    elif tile != '-1':
                        imagestr = 'sprite'
                        imagestr += str(int(tile)+1)
                        tiles.append(Tile(tile, imagestr, x * self.tile_size, y * self.tile_size, self.spritesheet, False, True, False, False))
                # Move to next tile in current row
                x += 1

            # Move to next row
            y += 1
            # Store the size of the tile map
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles