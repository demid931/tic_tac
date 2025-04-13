import pygame

pygame.init()  # обязательная каманда people
window_size = (600,600)

screen = pygame.display.set_mode(window_size)  # создание экрана(окна) с размера 300x300
screen.fill((255, 255, 255))

pygame.draw.line(screen,(0,0,0),[200,0],[200,600], 2)
pygame.draw.line(screen,(0,0,0),[400,0],[400,600],2)
pygame.draw.line(screen,(0,0,0),[0,200],[600,200],2)
pygame.draw.line(screen,(0,0,0),[0,400],[600,400],2)


pygame.display.set_caption("БАСУХА В ДЕЛЕ РОДНЫЕ")  # название окна
backgound_color = (255, 255, 255)  # цвет
clock = pygame.time.Clock()  # создание игровово таймера
a=1280/5

while True:  # игрововй таймер
    clock.tick(40)  # частота обновления таймераааааа
    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.QUIT:  # если нажали на крестик
            pygame.QUIT()  # выйти из ГОЙДА

    pygame.display.update()  # ОБНОВЛЕНИЕ ДИСПЛЕЯ
