import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Miata Mayhem")

WHITE = (255, 255, 255)
GOLD = (252, 186, 3)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
font = pygame.font.Font("font.ttf", 50)
font2 = pygame.font.Font("font.ttf", 100)
font3 = pygame.font.Font("font.ttf", 30)

doubloons= pygame.image.load("dabloon.png")
doubloon = pygame.transform.scale(doubloons,(50, 50))
doubloon_rect = doubloon.get_rect()

vitor = pygame.image.load("vi.png")
og_size3 = vitor.get_size()
scale3 = 0.7
new_size3 = (og_size3[0] * scale3), (og_size3[1] * scale3)
vg = pygame.transform.scale(vitor, new_size3)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
vitor_pos = pygame.Vector2(random.randint(0, 1280), random.randint(0, 360))

start = pygame.image.load("start.png")
start = pygame.transform.scale(start,(1280, 720))
running = False

def doubloons():
    x = random.randint(0, screen.get_width() - doubloon_rect.width)
    y = random.randint(0, screen.get_height() - doubloon_rect.height)
    return pygame.Rect(x,y,doubloon_rect.width, doubloon_rect.height)

def psp():
    lane = random.randint(200, 600) 
    psp_pos = pygame.Vector2(1280, lane) 
    return psp_pos

def start_screen():
    screen.blit(start, (0, 0))

    text = font2.render("Miata Mayhem", True, WHITE)
    text_rect = text.get_rect(center=(screen.get_width()//2, screen.get_height()//2 - 50))
    screen.blit(text, text_rect)

    instruction_text = font.render("Press S to start", True, WHITE)
    instruction_rect = instruction_text.get_rect(center=(screen.get_width()//2, screen.get_height()//2 + 50))
    screen.blit(instruction_text, instruction_rect)

    game = font3.render("Don't hit the police, plunder doubloons. But BE AWARE of Vitor Gonçalves.", True, WHITE)
    game_rect = game.get_rect(center=(screen.get_width()//2, screen.get_height()//2 + 110))
    screen.blit(game, game_rect)

    pygame.display.flip()

    waiting = True
    while waiting:
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if keys[pygame.K_s]:
            print("HELLO")
            waiting = False
            running = True

def ko_screen():
    screen.fill(BLACK)

    text = font2.render("Skill issue", True, RED)
    text_rect = text.get_rect(center=(screen.get_width()//2, screen.get_height()//2 - 50))
    screen.blit(text, text_rect)

    instruction_text = font.render("Press S to restart", True, WHITE)
    instruction_rect = instruction_text.get_rect(center=(screen.get_width()//2, screen.get_height()//2 + 50))

    instruction_text2 = font.render("Press ESC to quit", True, WHITE)
    instruction_rect2 = instruction_text2.get_rect(center=(screen.get_width()//2, screen.get_height()//2 + 120))

    instruction_text3 = font.render(f"Score: {score}", True, WHITE)
    instruction_rect3 = instruction_text3.get_rect(center=(screen.get_width()//2, screen.get_height()//2 + 190))

    screen.blit(instruction_text, instruction_rect)
    screen.blit(instruction_text2, instruction_rect2)
    screen.blit(instruction_text3, instruction_rect3)

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    waiting = False
                    reset()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return False
    return True

def reset():
    global player_pos, vitor_pos, doubloon_rect, score, times, psp_pos, psp_speed, vitor_speed, vg, scale3
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    vitor_pos = pygame.Vector2(random.randint(0, 1280), random.randint(0, 720))
    doubloon_rect = doubloons()
    score = 0
    times = 0
    psp_pos = psp()
    psp_speed = 2
    vitor_speed = 1
    scale3 = 0.7
    vg = pygame.transform.scale(vitor, new_size3)

def main_loop():
    global running , times, psp_speed, scale3, vitor_speed, score
    dt = 0
    times = 0

    vitor = pygame.image.load("vi.png")
    og_size3 = vitor.get_size()
    scale3 = 0.7
    
    collision_cooldown = 1000
    last_collision_time = 0

    miata = pygame.image.load("miata.png")
    og_size = miata.get_size()
    scale = 0.45
    new_size = (og_size[0] * scale), (og_size[1] * scale)
    smol_miata = pygame.transform.scale(miata , new_size)
    miata_flipped = pygame.transform.flip(smol_miata, True, False)
    show_miata = smol_miata

    background_image = pygame.image.load("road.png")
    background_image = pygame.transform.scale(background_image,(1280, 720))

    score = 0

    doubloon_rect = doubloons()

    bmw_psp = pygame.image.load("bmw.png")
    og_size2 = bmw_psp.get_size()
    scale2 = 0.65
    new_size2 = (og_size2[0] * scale2), (og_size2[1] * scale2)
    smol_bmw = pygame.transform.scale(bmw_psp, new_size2)

    psp_pos = psp()
    psp_speed = 3

    vitor_speed = 1 

    running = True
    while running:
        key_pressedA = False
        key_pressedD = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image, (0, 0))

        keys = pygame.key.get_pressed()
        speed = 300
        boost = 600

        s = boost if keys[pygame.K_SPACE] else speed

        if keys[pygame.K_w]:
            player_pos.y -= s * dt
            # Prevent from going off top edge
            if player_pos.y < 0:
                player_pos.y = 0
        if keys[pygame.K_s]:
            player_pos.y += s * dt
            # Prevent from going off bottom edge
            if player_pos.y > screen.get_height() - smol_miata.get_height():
                player_pos.y = screen.get_height() - smol_miata.get_height()

        if keys[pygame.K_a]:
            player_pos.x -= s * dt
            # Wrap around to right edge if off left edge
            if player_pos.x < -smol_miata.get_width():
                player_pos.x = screen.get_width()
            key_pressedA = True
        if keys[pygame.K_d]:
            player_pos.x += s * dt
            # Wrap around to left edge if off right edge
            if player_pos.x > screen.get_width():
                player_pos.x = -smol_miata.get_width()
            key_pressedD = True

        if key_pressedA: 
            show_miata = miata_flipped
        if key_pressedD: 
            show_miata = smol_miata 

        miata_rect = show_miata.get_rect(topleft=(player_pos.x, player_pos.y))

        screen.blit(show_miata, player_pos)

        if miata_rect.colliderect(doubloon_rect):
            doubloon_rect = doubloons() 
            score += 1

        score_text = font3.render(f'Score: {score}', True, GOLD)
        score_rect = score_text.get_rect(topright=(screen.get_width() - 10, 10))
        screen.blit(score_text, score_rect)

        screen.blit(doubloon, doubloon_rect.topleft)

        if psp_pos.x <= -smol_bmw.get_width():
            psp_pos = psp()

        bmw_rect = smol_bmw.get_rect(topleft=(psp_pos.x, psp_pos.y))

        if miata_rect.colliderect(bmw_rect): 
            scale3 += 0.005
            vitor_speed += 0.01

        new_size3 = (og_size3[0] * scale3), (og_size3[1] * scale3)
        vg = pygame.transform.scale(vitor, new_size3)

        psp_pos.x -= psp_speed
        screen.blit(smol_bmw, psp_pos)

        # Move Vitor towards the Miata
        if vitor_pos.x < player_pos.x:
            vitor_pos.x += vitor_speed
        elif vitor_pos.x > player_pos.x:
            vitor_pos.x -= vitor_speed

        if vitor_pos.y < player_pos.y:
            vitor_pos.y += vitor_speed
        elif vitor_pos.y > player_pos.y:
            vitor_pos.y -= vitor_speed

        vitor_rect = vg.get_rect(topleft=(vitor_pos.x, vitor_pos.y))

        current_time = pygame.time.get_ticks()

        if miata_rect.colliderect(vitor_rect) and current_time - last_collision_time > collision_cooldown:
            psp_speed += 3
            times += 1
            last_collision_time = current_time
            if times >= 3:
                if not ko_screen():
                    running = False
                    break
                

        lives = font3.render(f'Lives left: {3-times}', True, WHITE)
        lives_rect = lives.get_rect(topleft=(10, 10))
        screen.blit(lives, lives_rect)
        screen.blit(vg, vitor_pos)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    start_screen()
    while True:
        main_loop()
        if not running:
            break
    pygame.quit()
