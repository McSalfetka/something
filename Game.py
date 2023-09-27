import pygame as pg
import random as ra

pg.init()

screen_width, screen_height = 800, 600

FPS = 24    # frame per second
clock = pg.time.Clock()

# изображения
bg_img = pg.image.load('background.png')
icon_img = pg.image.load('enemy.png')

display = pg.display.set_mode((screen_width, screen_height))
pg.display.set_icon(icon_img)
pg.display.set_caption('Космическое вторжение')

sys_font = pg.font.SysFont('arial', 34)
font = pg.font.Font('../04B_19.TTF', 48)

# display.fill('blue', (0, 0, screen_width, screen_height))
display.blit(bg_img, (0, 0))        # image.tr

text_img = sys_font.render('Score 123', True, 'white')
# display.blit(text_img, (100, 50))

game_over_text = font.render('Game Over', True, 'red')
wgo, hgo = game_over_text.get_size()
# display.blit(game_over_text, (screen_width/2 - w/2, screen_height / 2 - h/2))

n = ['3', '/3']
ammos = int(n[0])
print(ammos)
ammorelised = ''.join(n)
ammoleft = font.render(ammorelised, True, 'white')

score_text = font.render("score:", True, 'white')
ws, hs = score_text.get_size()

score = '0'
score_num_text = font.render(score, True, 'white')
# игрок
player_img = pg.image.load('../player.png')
player_width, player_height = player_img.get_size()
player_gap = 10
player_velocity = 10
player_dx = 0
player_x = screen_width/2 - player_width/2
player_y = screen_height - player_height - player_gap

bullet_img = pg.image.load('bullet.png')
bullet_width, bullet_height = bullet_img.get_size()
bullet_dy = -8
bullet_x = player_x + player_width/4
bullet_y = player_y - player_height/2
bullet_live = False

enemy_img = pg.image.load('enemy.png')
enemy_width, enemy_height = enemy_img.get_size()
enemy_dx = 0
enemy_dy = 5
enemy_x = 0
enemy_y = 0
enemy_alive = False
gameOn = True
print(wgo, ws)
def gameover():
    global score
    display.fill('blue', (0, 0, screen_width, screen_height))
    display.blit(game_over_text, (screen_width/2 - wgo/2, 0.45 * screen_height - hgo/2))
    score = str(score)
    display.blit(score_text, (screen_width/2 - ws/2, 0.55 * screen_height - hs/2))
    pg.display.update()
def enemy_create():
    global enemy_y, enemy_x
    enemy_x = ra.randint(0, screen_width)
    enemy_y = 0

def enemy_model():
    global enemy_y, enemy_x, bullet_live, gameOn, score
    enemy_x += enemy_dx
    enemy_y += enemy_dy
    if enemy_y > screen_height:
        enemy_create()
    if bullet_live:
        re = pg.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
        rb = pg.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
        is_crossed = re.colliderect(rb)
        if is_crossed:
            score = str(int(score)+1)
            enemy_create()
            bullet_live = False
    if gameOn:
        rp = pg.Rect(player_x, player_y, player_width, player_height)
        re = pg.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
        is_collapse = rp.colliderect(re)
        if is_collapse:
            gameOn = False
            enemy_create()


def model_update():
    palayer_model()
    bullet_model()
    enemy_model()

def palayer_model():
    global player_x
    player_x += player_dx
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width

def bullet_model():
    global bullet_y, bullet_dlive, bullet_live
    bullet_y += bullet_dy
    # пуля улетела за верх экрана
    if bullet_y < 0:
        bullet_live = False

def bullet_create():
    global bullet_y, bullet_x, bullet_live
    bullet_live = True
    bullet_x = player_x + player_width/4
    bullet_y = player_y - player_height/3


def display_redraw():
    display.blit(bg_img, (0, 0))
    display.blit(player_img, (player_x, player_y))
    display.blit(enemy_img, (enemy_x, enemy_y))
    display.blit(ammoleft, (screen_width-100, screen_height-100))
    if bullet_live:
        display.blit(bullet_img, (bullet_x, bullet_y))
    pg.display.update()

def event_processing():
    global player_dx, gameOn
    running = True
    for event in pg.event.get():
        # нажали крестик на окне
        if event.type == pg.QUIT:
            running = False
        # тут нажимаем на клавиши
        if event.type == pg.KEYDOWN:
            # нажали на q - quit
            if event.key == pg.K_q:
                running = False
        # движение игрока
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a or event.key == pg.K_LEFT:
                player_dx = -player_velocity
            if event.key == pg.K_d or event.key == pg.K_RIGHT:
                player_dx = player_velocity
            if event.key == pg.K_r:
                if not gameOn:
                    gameOn = True
        if event.type == pg.KEYUP:
            player_dx = 0

        if event.type == pg.MOUSEBUTTONDOWN:
            key = pg.mouse.get_pressed()
            if not bullet_live:
                bullet_create()


    clock.tick(FPS)
    return running

# ra.seed(77)
running = True
while running:
    if gameOn:
        #enemy_create()
        model_update()
        display_redraw()
    else:
        gameover()
    running = event_processing()
pg.quit()
