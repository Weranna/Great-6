import pygame
from config.config import *
import math

class Player(pygame.sprite.Sprite): 
    
    def __init__ (self,game,x,y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.x_change = 0
        self.y_change = 0
        
        self.facing = 'down'
        self.animation_loop = 1
        
        self.image = self.game.character_spritesheet.get_sprite(32,0,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.down_animations = [ self.game.character_spritesheet.get_sprite(32,0,self.width,self.height),
                           self.game.character_spritesheet.get_sprite(0,0,self.width,self.height),
                           self.game.character_spritesheet.get_sprite(64,0,self.width,self.height)
                           ]
        self.up_animations = [ self.game.character_spritesheet.get_sprite(32,96,self.width,self.height),
                           self.game.character_spritesheet.get_sprite(0,96,self.width,self.height),
                           self.game.character_spritesheet.get_sprite(64,96,self.width,self.height)
                           ]
        self.left_animations = [ self.game.character_spritesheet.get_sprite(32,32,self.width,self.height),
                           self.game.character_spritesheet.get_sprite(0,32,self.width,self.height),
                           self.game.character_spritesheet.get_sprite(64,32,self.width,self.height)
                           ]
        self.right_animations = [ self.game.character_spritesheet.get_sprite(32,64,self.width,self.height),
                           self.game.character_spritesheet.get_sprite(0,64,self.width,self.height),
                           self.game.character_spritesheet.get_sprite(64,64,self.width,self.height)
                           ]
    
    def update(self):
        self.movement()
        self.animate()
        self.collide_enemy()
        
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        
        self.x_change = 0
        self.y_change = 0
    
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_d]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_w]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_s]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'
            
    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self,self.game.enemies,False)
        if hits:
            self.kill()
            self.game.playing = False
            
    def collide_blocks(self,direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self,self.game.terrain,False)
            
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
                    
        if direction == "y":
            hits = pygame.sprite.spritecollide(self,self.game.terrain,False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED
            
    def animate(self):
        
        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(32,0,self.width,self.height)
            else:
                self.image = self.down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == 'up':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(32,96,self.width,self.height)
            else:
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(32,32,self.width,self.height)
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(32,64,self.width,self.height)
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1