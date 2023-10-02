import pygame
from config.config import *
import math
import random


class Enemy(pygame.sprite.Sprite):
    
    def __init__(self,game,x,y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies # type: ignore
        pygame.sprite.Sprite.__init__(self,self.groups) # type: ignore
        
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.x_change = 0
        self.y_change = 0
        
        self.facing = random.choice(['left','right'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(7,30)
        
        self.image = self.game.enemy_spritesheet.get_sprite(320,0,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.left_animations = [ self.game.enemy_spritesheet.get_sprite(320,32,self.width,self.height),
                           self.game.enemy_spritesheet.get_sprite(290,32,self.width,self.height),
                           self.game.enemy_spritesheet.get_sprite(351,32,self.width,self.height)
                           ]
        self.right_animations = [ self.game.enemy_spritesheet.get_sprite(320,64,self.width,self.height),
                           self.game.enemy_spritesheet.get_sprite(287,64,self.width,self.height),
                           self.game.enemy_spritesheet.get_sprite(351,64,self.width,self.height)
                           ]
        
    def update(self):
        self.movement()
        self.animate()
        
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        
        self.x_change = 0
        self.y_change = 0
        
    def movement(self):
        if self.facing == 'left':
            self.x_change -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = 'right'
        if self.facing == "right":
            self.x_change += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = 'left'
                
    def animate(self):

        if self.facing == 'left':
            self.image = self.left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 3:
                self.animation_loop = 1
        if self.facing == 'right':
            self.image = self.right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 3:
                self.animation_loop = 1