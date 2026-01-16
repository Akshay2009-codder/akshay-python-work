import random
import sys
import pygame
from pygame.locals import *

pygame.init()

SCREENWIDTH = 400
SCREENHEIGHT = 600
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Flappy Bird by AK")

FPS = 32
FPSCLOCK = pygame.time.Clock()

WHITE = (255, 255, 255)

BACKGROUND = pygame.transform.scale(pygame.image.load("background.png").convert(), (SCREENWIDTH, SCREENHEIGHT))
PLAYER = pygame.image.load("bird.png").convert_alpha()
PIPE = pygame.image.load("pipe.png").convert_alpha()

PLAYER = pygame.transform.scale(PLAYER, (40, 30))
PIPE = pygame.transform.scale(PIPE, (70, 400))

GAME_SPRITES = {
    "PLAYER": PLAYER,
    "BACKGROUND": BACKGROUND,
    "PIPE": (
        pygame.transform.rotate(PIPE, 180),
        PIPE
    )
}

GAME_SOUNDS = {
    "wing": pygame.mixer.Sound("wing.mp3"),
    "point": pygame.mixer.Sound("point.mp3"),
    "hit": pygame.mixer.Sound("hit.mp3")
}

def welcomeScreen():
    playerx = int(SCREENWIDTH / 5)
    playery = int((SCREENHEIGHT - GAME_SPRITES["PLAYER"].get_height()) / 2)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES["BACKGROUND"], (0, 0))
                SCREEN.blit(GAME_SPRITES["PLAYER"], (playerx, playery))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    score = 0
    playerx = int(SCREENWIDTH / 5)
    playery = int(SCREENHEIGHT / 2)

    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    upperPipes = [
        {"x": SCREENWIDTH + 200, "y": newPipe1[0]["y"]},
        {"x": SCREENWIDTH + 200 + (SCREENWIDTH / 2), "y": newPipe2[0]["y"]},
    ]
    lowerPipes = [
        {"x": SCREENWIDTH + 200, "y": newPipe1[1]["y"]},
        {"x": SCREENWIDTH + 200 + (SCREENWIDTH / 2), "y": newPipe2[1]["y"]},
    ]

    pipeVelX = -4
    playerVelY = -9
    playerMaxVelY = 10
    playerAccY = 1

    playerFlapAccv = -8
    playerFlapped = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS["wing"].play()

        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)
        if crashTest:
            return

        playerMidPos = playerx + GAME_SPRITES["PLAYER"].get_width() / 2
        for pipe in upperPipes:
            pipeMidPos = pipe["x"] + GAME_SPRITES["PIPE"][0].get_width() / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
                GAME_SOUNDS["point"].play()

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY
        if playerFlapped:
            playerFlapped = False
        playerHeight = GAME_SPRITES["PLAYER"].get_height()
        playery = playery + min(playerVelY, SCREENHEIGHT - playery - playerHeight)

        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe["x"] += pipeVelX
            lowerPipe["x"] += pipeVelX

        if 0 < upperPipes[0]["x"] < 5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        if upperPipes[0]["x"] < -GAME_SPRITES["PIPE"][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        SCREEN.blit(GAME_SPRITES["BACKGROUND"], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES["PIPE"][0], (upperPipe["x"], upperPipe["y"]))
            SCREEN.blit(GAME_SPRITES["PIPE"][1], (lowerPipe["x"], lowerPipe["y"]))
        SCREEN.blit(GAME_SPRITES["PLAYER"], (playerx, playery))

        font = pygame.font.SysFont("Arial", 24, bold=True)
        score_surface = font.render(f"Score: {str(score)}", True, WHITE)
        SCREEN.blit(score_surface, (SCREENWIDTH/2 - score_surface.get_width()/2, 20))

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery < 0 or playery > SCREENHEIGHT - 30:
        GAME_SOUNDS["hit"].play()
        return True
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES["PIPE"][0].get_height()
        if playery < pipe["y"] + pipeHeight and abs(playerx - pipe["x"]) < GAME_SPRITES["PIPE"][0].get_width():
            GAME_SOUNDS["hit"].play()
            return True
    for pipe in lowerPipes:
        if playery + GAME_SPRITES["PLAYER"].get_height() > pipe["y"] and abs(playerx - pipe["x"]) < GAME_SPRITES["PIPE"][0].get_width():
            GAME_SOUNDS["hit"].play()
            return True
    return False

def getRandomPipe():
    pipeHeight = GAME_SPRITES["PIPE"][0].get_height()
    offset = SCREENHEIGHT / 3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - 1.2 * offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {"x": pipeX, "y": -y1},
        {"x": pipeX, "y": y2}
    ]
    return pipe

if __name__ == "__main__":
    while True:
        welcomeScreen()
        mainGame()
