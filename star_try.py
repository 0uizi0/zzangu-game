from pickle import FALSE
from socket import getnameinfo
from pkg_resources import to_filename
import random
import pygame

######################################################################
# 기본 초기화 (반드시 해야 하는 것들)

pygame.init()

#화면크기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("ZZangGu Game") #게임이름

#FPS
clock = pygame.time.Clock()
######################################################################

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
#배경 만들기
background = pygame.image.load("C:\\Users\\0uizi\\OneDrive\\문서\\3학년\\PythonWorkspace\\pygame_basic\\background.png")

#캐릭터 만들기
character = pygame.image.load("C:\\Users\\0uizi\\OneDrive\\문서\\3학년\\PythonWorkspace\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

# 이동 위치
to_x = 0
character_speed = 20

# 초코비 만들기
enemy = pygame.image.load("C:\\Users\\0uizi\\OneDrive\\문서\\3학년\\PythonWorkspace\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randrange(0,screen_width-enemy_width)
enemy_y_pos = 0
enemy_speed = 30

#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성(폰트, 크기)

#총 시간
total_time = 20

#시작 시간
start_ticks = pygame.time.get_ticks() #현재 tick을 받아옴

running = True
while running:
    dt = clock.tick(30) 

    # 2. 이벤트 처리 (키보드, 마우스 등)
    print("fps:"+str(clock.get_fps()))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randrange(0,screen_width-enemy_width)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False
   
    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))

    #타이머 집어 넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    #경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)),True,(255,255,255))
    #출력할 글자, True, 글자 색상
    screen.blit(timer,(10,10))

    #만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False
    
    pygame.display.update() 

#잠시 대기
pygame.time.delay(500) #0.5초 정도 대기(ms)

pygame.quit()