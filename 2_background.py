from pickle import FALSE
import pygame

pygame.init() #초기화. 반드시 필요

#화면크기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("ZZangGu Game") #게임이름

#배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\0uizi\\OneDrive\\문서\\3학년\\PythonWorkspace\\pygame_basic\\background.png")

#이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아님

    screen.blit(background,(0,0)) #배경 그리기

    pygame.display.update() #게임화면 다시 그리기

#pygame 종료
pygame.quit()

#main브랜치에서 내용 수정함.
#user1에서 수정한 내역을 main브랜치가 받아야함.
#이때 pull 사용함.