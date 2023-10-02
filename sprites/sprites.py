import random
import pygame
from config.config import *
import math

class Spritesheet:
    def __init__ (self,file):
        self.sheet = pygame.image.load(file).convert()
    
    def get_sprite(self,x,y,width,height):
        sprite = pygame.Surface([width,height])
        sprite.blit(self.sheet,(0,0),(x,y,width,height))
        sprite.set_colorkey(BLACK)
        return sprite                  
        
        
class Button:
    
    def __init__(self,y,width,height,fg,bg,content,fontsize):
        
        self.font = pygame.font.Font('assets/fonts/Minecraft.ttf',fontsize)
        self.content = content
        
        self.width = width
        self.height = height
        
        self.fg = fg
        self.bg = bg
        
        self.image = pygame.image.load(bg)
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect(center=(WIN_WIDTH/2,y))
        
        self.text = self.font.render(self.content,True,self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2,self.height/2))
        self.image.blit(self.text,self.text_rect)
        
    def is_pressed(self,pos,pressed):
        
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False
        
class Attack(pygame.sprite.Sprite):
    
    def __init__(self,game,x,y):
        
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.attacks # type: ignore
        pygame.sprite.Sprite.__init__(self,self.groups) # type: ignore
        
        self.x = x
        self.y = y
        self.width = TILESIZE/2
        self.height = TILESIZE/2
        
        self.animation_loop = 0
        self.image = self.game.attack_spritesheet.get_sprite(0,0,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.animations = [self.game.attack_spritesheet.get_sprite(0,0,self.width,self.height),
                      self.game.attack_spritesheet.get_sprite(16,0,self.width,self.height),
                      self.game.attack_spritesheet.get_sprite(32,0,self.width,self.height)
                      ]
    
    def update(self):
        self.animate()
        self.collide()
        
    def collide(self):
        hits = pygame.sprite.spritecollide(self,self.game.enemies,True)
        
    def animate(self):
        
        self.image = self.animations[math.floor(self.animation_loop)]
        self.animation_loop += 0.5
        if self.animation_loop >= 3:
            self.kill()
            
            