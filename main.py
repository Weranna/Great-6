import pygame
from characters.player import *
from characters.enemy import *
from sprites.sprites import *
from config.config import *
from config.tilemap import *
import sys
from sprites.terrain import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Great 6')
        self.font = pygame.font.Font('assets/fonts/Minecraft.ttf',100)
        self.running = True
        
        self.attack_spritesheet = Spritesheet('assets/images/attacks.png')
        self.character_spritesheet = Spritesheet('assets/images/characters.png')
        self.terrain_spritesheet = Spritesheet('assets/images/terrain.png')
        self.enemy_spritesheet =Spritesheet('assets/images/enemies.png')
        self.intro_background = pygame.image.load('assets/images/intro_screen.jpg')
        
        self.intro_background_width = WIN_WIDTH - 200
        self.intro_background = pygame.transform.scale(self.intro_background, (self.intro_background_width,WIN_HEIGHT))
        self.scroll = 0
        
        self.go_background = pygame.image.load('assets/images/gameover_screen.jpg')
        self.go_background = pygame.transform.scale(self.go_background, (WIN_WIDTH,WIN_HEIGHT))
        self.sign = pygame.image.load('assets/images/sign.png')
        self.sign = pygame.transform.scale(self.sign,(850,350))
        
    def create_tilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self,j,i)
                if column == "B":
                    Bush(self,j,i)
                if column == "P":
                    self.player = Player(self,j,i)
                    Grass(self,j,i)
                if column == "S":
                    Stone(self,j,i)
                if column == ".":
                    Grass(self,j,i)
                if column == "E":
                    Enemy(self,j,i)
                    Grass(self,j,i)
        
    def new(self):
        # A NEW GAME STARTS
        self.playing = True
        
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.terrain = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.npcs = pygame.sprite.LayeredUpdates()
        self.objects = pygame.sprite.LayeredUpdates()
        
        self.create_tilemap()
    
    def events(self):
        # GAME LOOP EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if self.player.facing == 'up':
                    Attack(self,self.player.rect.x,self.player.rect.y - TILESIZE/2)
                if self.player.facing == 'down':
                    Attack(self,self.player.rect.x,self.player.rect.y + TILESIZE)
                if self.player.facing == 'left':
                    Attack(self,self.player.rect.x - TILESIZE/2,self.player.rect.y)
                if self.player.facing == 'right':
                    Attack(self,self.player.rect.x + TILESIZE,self.player.rect.y)
    
    def update(self):
        # GAME LOOP UPDATES
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
    
    def main(self):
        # GAME LOPP
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    def game_over(self):
        
        text = self.font.render('GAME OVER',True,WHITE)
        text_rect = text.get_rect(center=(WIN_WIDTH/2,250))
        
        restart_button = Button(400,300,100,BLACK,'assets/images/button.png','Restart',50)
        
        for sprite in self.all_sprites:
            sprite.kill()
            
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False 
                    
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if restart_button.is_pressed(mouse_pos,mouse_pressed):
                self.new()
                self.main()
                
            self.screen.blit(self.go_background,(0,0))
            self.screen.blit(text,text_rect)
            self.screen.blit(restart_button.image,restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
        
    
    def intro_screen(self):
        intro = True
        
        title = self.font.render('GREAT 6',True,BLACK)
        title_rect = title.get_rect(center=(WIN_WIDTH/2,200))
       
        play_button = Button(400,300,100,BLACK,'assets/images/button.png','Play',50)
        
        
        
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if play_button.is_pressed(mouse_pos,mouse_pressed):
                intro = False
                
            tiles = math.ceil(WIN_WIDTH/self.intro_background_width) + 1
                
            for i in range (0,tiles):
                self.screen.blit(self.intro_background,(i*self.intro_background_width+self.scroll,0))
                
            self.scroll -= 5
            
            if abs(self.scroll) > self.intro_background_width:
                self.scroll = 0
            
            self.screen.blit(self.sign,(220,0))
            self.screen.blit(title,title_rect)
            self.screen.blit(play_button.image,play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
            

            
    
g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()
    
pygame.quit()
sys.exit()
