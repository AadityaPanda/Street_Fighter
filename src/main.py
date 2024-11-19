import pygame
from pygame import mixer
import cv2
import numpy as np
from fighter import Fighter

mixer.init()
pygame.init()

# Constants
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h
FPS = 60
ROUND_OVER_COOLDOWN = 3000

# Colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Game Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Shadow Fight")
clock = pygame.time.Clock()

# Load Assets
bg_image = cv2.imread("assets/images/bg1.jpg")
victory_img = pygame.image.load("assets/images/victory.png").convert_alpha()
warrior_victory_img = pygame.image.load("assets/images/warrior.png").convert_alpha()
wizard_victory_img = pygame.image.load("assets/images/wizard.png").convert_alpha()

# Fonts
menu_font = pygame.font.Font("assets/fonts/turok.ttf", 50)
count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)

# Music and Sounds
pygame.mixer.music.load("assets/audio/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
sword_fx = pygame.mixer.Sound("assets/audio/sword.wav")
sword_fx.set_volume(0.5)
magic_fx = pygame.mixer.Sound("assets/audio/magic.wav")
magic_fx.set_volume(0.75)

# Load Fighter Spritesheets
warrior_sheet = pygame.image.load("assets/images/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/images/wizard.png").convert_alpha()

# Define Animation Steps
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

# Fighter Data
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 46]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 97]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

# Game Variables
score = [0, 0]  # Player Scores: [P1, P2]


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def blur_bg(image):
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    blurred_image = cv2.GaussianBlur(image_bgr, (15, 15), 0)
    return cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)


def draw_bg(image, is_game_started=False):
    if not is_game_started:
        blurred_bg = blur_bg(image)
        blurred_bg = pygame.surfarray.make_surface(np.transpose(blurred_bg, (1, 0, 2)))
        blurred_bg = pygame.transform.scale(blurred_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(blurred_bg, (0, 0))
    else:
        # Draw the unblurred background when the game starts
        image = pygame.surfarray.make_surface(np.transpose(image, (1, 0, 2)))
        image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(image, (0, 0))


def draw_button(text, font, text_col, button_col, x, y, width, height):
    pygame.draw.rect(screen, button_col, (x, y, width, height))
    pygame.draw.rect(screen, WHITE, (x, y, width, height), 2)
    text_img = font.render(text, True, text_col)
    text_rect = text_img.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_img, text_rect)
    return pygame.Rect(x, y, width, height)


def victory_screen(winner_img):
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < ROUND_OVER_COOLDOWN:
        draw_bg(bg_image)
        screen.blit(winner_img, (SCREEN_WIDTH // 2 - winner_img.get_width() // 2,
                                 SCREEN_HEIGHT // 2 - winner_img.get_height() // 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


def main_menu():
    while True:
        draw_bg(bg_image, is_game_started=False)

        title_text = "SHADOW FIGHT"
        draw_text(title_text, menu_font, RED, SCREEN_WIDTH // 2 - menu_font.size(title_text)[0] // 2, 50)

        button_width = 300
        button_height = 70
        button_spacing = 20

        start_button_y = SCREEN_HEIGHT // 2 - (button_height + button_spacing) * 1.5
        scores_button_y = SCREEN_HEIGHT // 2 - (button_height + button_spacing) * 0.5
        exit_button_y = SCREEN_HEIGHT // 2 + (button_height + button_spacing) * 0.5

        start_button = draw_button("START GAME", menu_font, BLACK, YELLOW, SCREEN_WIDTH // 2 - button_width // 2,
                                   start_button_y, button_width, button_height)
        scores_button = draw_button("SCORES", menu_font, BLACK, YELLOW, SCREEN_WIDTH // 2 - button_width // 2,
                                    scores_button_y, button_width, button_height)
        exit_button = draw_button("EXIT", menu_font, BLACK, YELLOW, SCREEN_WIDTH // 2 - button_width // 2,
                                  exit_button_y, button_width, button_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return "START"
                if scores_button.collidepoint(event.pos):
                    return "SCORES"
                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()

        pygame.display.update()
        clock.tick(FPS)


def scores_screen():
    while True:
        draw_bg(bg_image)

        scores_title = "SCORES"
        draw_text(scores_title, menu_font, RED, SCREEN_WIDTH // 2 - menu_font.size(scores_title)[0] // 2, 50)

        p1_text = f"P1: {score[0]}"
        p2_text = f"P2: {score[1]}"
        draw_text(p1_text, score_font, YELLOW, SCREEN_WIDTH // 2 - score_font.size(p1_text)[0] // 2, 250)
        draw_text(p2_text, score_font, YELLOW, SCREEN_WIDTH // 2 - score_font.size(p2_text)[0] // 2, 400)

        return_button = draw_button("RETURN TO MAIN MENU", menu_font, BLACK, YELLOW, SCREEN_WIDTH // 2 - 220, 700, 500, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.collidepoint(event.pos):
                    return

        pygame.display.update()
        clock.tick(FPS)


def reset_game():
    global fighter_1, fighter_2
    fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
    fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)


def draw_health_bar(health, x, y):
    pygame.draw.rect(screen, BLACK, (x, y, 200, 20))
    if health > 0:
        pygame.draw.rect(screen, RED, (x, y, health * 2, 20))
    pygame.draw.rect(screen, WHITE, (x, y, 200, 20), 2)


def countdown():
    countdown_font = pygame.font.Font("assets/fonts/turok.ttf", 100)
    countdown_texts = ["3", "2", "1", "FIGHT!"]

    for text in countdown_texts:
        draw_bg(bg_image, is_game_started=True)

        text_img = countdown_font.render(text, True, RED)
        text_width = text_img.get_width()
        x_pos = (SCREEN_WIDTH - text_width) // 2

        draw_text(text, countdown_font, RED, x_pos, SCREEN_HEIGHT // 2 - 50)

        pygame.display.update()
        pygame.time.delay(1000)


def game_loop():
    global score
    reset_game()
    round_over = False
    winner_img = None
    game_started = True

    countdown()

    while True:
        draw_bg(bg_image, is_game_started=game_started)

        draw_text(f"P1: {score[0]}", score_font, RED, 20, 20)
        draw_text(f"P2: {score[1]}", score_font, RED, SCREEN_WIDTH - 220, 20)
        draw_health_bar(fighter_1.health, 20, 50)
        draw_health_bar(fighter_2.health, SCREEN_WIDTH - 220, 50)

        exit_button = draw_button("MAIN MENU", menu_font, BLACK, YELLOW, SCREEN_WIDTH // 2 - 150, 20, 300, 50)

        if not round_over:
            fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_2, round_over)
            fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_1, round_over)

            fighter_1.update()
            fighter_2.update()

            if not fighter_1.alive:
                score[1] += 1
                round_over = True
                winner_img = wizard_victory_img
            elif not fighter_2.alive:
                score[0] += 1
                round_over = True
                winner_img = warrior_victory_img
        else:
            victory_screen(winner_img)
            return

        fighter_1.draw(screen)
        fighter_2.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    return

        pygame.display.update()
        clock.tick(FPS)


while True:
    menu_selection = main_menu()

    if menu_selection == "START":
        game_loop()
    elif menu_selection == "SCORES":
        scores_screen()
