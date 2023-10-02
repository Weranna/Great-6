import pygame
from config.config import *

class Bush(pygame.sprite.Sprite):
    
    def __init__(self,game,x,y):
        
        self.game = game
        self._layer = TERRAIN_LAYER
        self.groups = self.game.all_sprites, self.game.terrain # type: ignore
        pygame.sprite.Sprite.__init__(self,self.groups) # type: ignore
        
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(352,352,self.width-1,self.height-1)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
class Stone(pygame.sprite.Sprite):
    
    def __init__(self,game,x,y):
        
        self.game = game
        self._layer = TERRAIN_LAYER
        self.groups = self.game.all_sprites, self.game.terrain # type: ignore
        pygame.sprite.Sprite.__init__(self,self.groups) # type: ignore
        
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(960,445,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
class Ground(pygame.sprite.Sprite):
    
    def __init__(self,game,x,y):
        
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(384,352,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
class Grass(pygame.sprite.Sprite):
    
    def __init__(self,game,x,y):
        
        self.game = game
        self._layer = GRASS_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(480,352,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y