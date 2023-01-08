# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:11:16 2022

@author: Hp
"""

import pygame
import sys
pygame.init()
 
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
FPS = 20
# define the RGB value 
# for white colour 
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
ADD_NEW_FLAME_RATE = 25
devils_img = pygame.image.load('img/devils.png')
devils_img_rect = devils_img.get_rect()
devils_img_rect.left = 0
bullet_img = pygame.image.load('img/devils.png')
bullet_img_rect = bullet_img.get_rect()
bullet_img_rect.left = 0
CLOCK = pygame.time.Clock()
font = pygame.font.SysFont('Britannic Bold', 20)
 
# set the pygame window name and logo
canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('TOKKI DAMON')
icon = pygame.image.load('img/logos.png')
pygame.display.set_icon(icon)  
class Topscore:
    def __init__(self):
        self.high_score = 0
    def top_score(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score
 
topscore = Topscore() 
class Damon:
    damon_velocity = 10 
    def __init__(self):
        self.damon_img = pygame.image.load('img/ghost.png')
        self.damon_img_rect = self.damon_img.get_rect()
        self.damon_img_rect.width -= 10
        self.damon_img_rect.height -= 10
        self.damon_img_rect.top = WINDOW_HEIGHT/2
        self.damon_img_rect.right = WINDOW_WIDTH
        self.up = True
        self.down = False
 
    def update(self):
        canvas.blit(self.damon_img, self.damon_img_rect)
       if self.damon_img_rect.top <= devils_img_rect.bottom:
            self.up = False
            self.down = True
        elif self.damon_img_rect.bottom >= bullet_img_rect.top:
            self.up = True
            self.down = Fals
      if self.up:
            self.damon_img_rect.top -= self.damon_velocity
        elif self.down:
            self.damon_img_rect.top += self.damon_velocity 
class Flames:
    flames_velocity = 20
 
    def __init__(self):
        self.flames = pygame.image.load('img/bullet.png')
        self.flames_img = pygame.transform.scale(self.flames, (20, 20))
        selfflames_img_rect = self.flames_img.get_rect()
        self.flames_img_rect.right = damon.damon_img_rect.left
        self.flames_img_rect.top = damon.damon_img_rect.top + 30
    def update(self):
        canvas.blit(self.flames_img, self.flames_img_rect)
 
        if self.flames_img_rect.left > 0:
            self.flames_img_rect.left -= self.flames_velocity 
class Tokki:
    velocity = 10
 
    def __init__(self):
        self.tokki_img = pygame.image.load('img/tokki.png')
        self.tokki_img_rect = self.tokki_img.get_rect()
        self.tokki_img_rect.left = 20
        self.tokki_img_rect.top = WINDOW_HEIGHT/2 - 100
        self.down = True
        self.up = False
 
    def update(self):
        canvas.blit(self.tokki_img, self.tokki_img_rect)
        if self.tokki_img_rect.top <= devils_img_rect.bottom:
            game_over()
            if SCORE > self.tokki_score:
                self.tokki_score = SCORE
        if self.tokki_img_rect.bottom >= bullet_img_rect.top:
            game_over()
            if SCORE > self.tokki_score:
                self.tokki_score = SCORE
        if self.up:
            self.tokki_img_rect.top -= 10
        if self.down:
            self.tokki_img_rect.bottom += 10
 
 
def game_over():
    
    topscore.top_score(SCORE)
    game_over_img = pygame.image.load('img/end.png')
    game_over_img_rect = game_over_img.get_rect()
    game_over_img_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    canvas.blit(game_over_img, game_over_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
               
                game_loop()
        pygame.display.update()
 
 
def start_game():
    canvas.fill(BLACK)
    start_img = pygame.image.load('img/start.png')
    start_img_rect = start_img.get_rect()
    start_img_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    canvas.blit(start_img, start_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.update()
 
 
def check_level(SCORE):
    global LEVEL
    if SCORE in range(0, 10):
        devils_img_rect.bottom = 50
        bullet_img_rect.top = WINDOW_HEIGHT - 50
        LEVEL = 1
    elif SCORE in range(10, 20):
        devils_img_rect.bottom = 100
        bullet_img_rect.top = WINDOW_HEIGHT - 100
        LEVEL = 2
    elif SCORE in range(20, 30):
        devils_img_rect.bottom = 150
        bullet_img_rect.top = WINDOW_HEIGHT - 150
        LEVEL = 3
    elif SCORE > 30:
        devils_img_rect.bottom = 200
        bullet_img_rect.top = WINDOW_HEIGHT - 200
        LEVEL = 4
 
 
def game_loop():
    while True:
        global damon
        damon= Damon()
        flames = Flames()
        tokki = Tokki()
        add_new_flame_counter = 0
        global SCORE
        SCORE = 0
        global  HIGH_SCORE
        flames_list = []
        
        while True:
            canvas.fill(BLACK)
            check_level(SCORE)
            damon.update()
            add_new_flame_counter += 1
 
            if add_new_flame_counter == ADD_NEW_FLAME_RATE:
                add_new_flame_counter = 0
                new_flame = Flames()
                flames_list.append(new_flame)
            for f in flames_list:
                if f.flames_img_rect.left <= 0:
                    flames_listremove(f)
                    SCORE += 1
                f.update()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        tokki.up = True
                        tokki.down = False
                    elif event.key == pygame.K_DOWN:
                        tokki.down = True
                        tokki.up = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        tokki.up = False
                        tokki.down = True
                    elif event.key == pygame.K_DOWN:
                        tokki.down = True
                        tokki.up = False
 
            score_font = font.render('Score:'+str(SCORE), True, GREEN)
            score_font_rect = score_font.get_rect()
            score_font_rect.center = (200, devils_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(score_font, score_font_rect)
 
            level_font = font.render('Level:'+str(LEVEL), True, GREEN)
            level_font_rect = level_font.get_rect()
            level_font_rect.center = (500, devils_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(level_font, level_font_rect)
 
            top_score_font = font.render('Top Score:'+str(topscore.high_score),True,GREEN)
            top_score_font_rect = top_score_font.get_rect()
            top_score_font_rect.center = (800, devils_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(top_score_font, top_score_font_rect)
 
            canvas.blit(devils_img, devils_img_rect)
            canvas.blit(bullet_img, bullet_img_rect)
            tokki.update()
            for f in flames_list:
                if f.flames_img_rectcolliderect(tokki.tokki_img_rect):
                    game_over()
                    if SCORE > tokki.tokki_score:
                        tokki.tokki_score = SCORE
            pygame.display.update()
            CLOCK.tick(FPS)
 
 
start_game()
