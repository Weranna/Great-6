import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Great 6')
        self.font = pygame.font.Font('assets/fonts/Minecraft.ttf',80)
        self.running = True
        
        self.attack_spritesheet = Spritesheet('assets/images/attacks.png')
        self.character_spritesheet = Spritesheet('assets/images/characters.png')
        self.terrain_spritesheet = Spritesheet('assets/images/terrain.png')
        self.enemy_spritesheet =Spritesheet('assets/images/enemies.png')
        self.intro_background = pygame.image.load('assets/images/intro_screen.jpg')
        self.intro_background = pygame.transform.scale(self.intro_background, (WIN_WIDTH,WIN_HEIGHT))
        self.go_background = pygame.image.load('assets/images/gameover_screen.jpg')
        self.go_background = pygame.transform.scale(self.go_background, (WIN_WIDTH,WIN_HEIGHT))
        
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
        
        restart_button = Button(350,150,50,WHITE,BLACK,'Restart',32)
        
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
        title_rect = title.get_rect(center=(WIN_WIDTH/2,80))
        
        play_button = Button(180,100,50,WHITE,BLACK,'Play',32)
        
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if play_button.is_pressed(mouse_pos,mouse_pressed):
                intro = False
                
            self.screen.blit(self.intro_background,(0,0)) # type: ignore
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
