# def get_recommendation():
#     pogoda=input("Введите текущую погоду (солнечно, дождь, снег, облачно): ")
#
#     try:
#         gradus=int(input("Введите температуру на улице"))
#     except ValueError:
#         print("неверный формат градусов")
#         return
#     else:
#         if gradus<0:
#             if pogoda.lower()=="снег":
#                 print("Сегодня сильный мороз и снег! Наденьте пуховик, теплую шапку, шарф, перчатки и теплые ботинки.")
#             else:
#                 print("Очень холодно! Наденьте теплую куртку, шапку, шарф и перчатки.")
#         elif gradus>=0 and gradus<=10:
#             if pogoda.lower()=="дождь":
#                 print("Прохладно и дождь. Возьмите зонт, наденьте непромокаемую куртку и свитер.")
#             else:
#                 print( "Прохладно. Наденьте куртку, свитер.")
#         elif gradus>=11 and gradus<=20:
#             if pogoda.lower()=="солнечно":
#                 print("Приятная погода. Можно надеть легкую куртку или кардиган. Не забудьте солнцезащитные очки!")
#             else:
#                  print( "Комфортная погода. Наденьте легкую куртку или толстовку.")
#         else:
#             if pogoda.lower()=="солнечно":
#                     print("Жарко! Наденьте легкую одежду, шорты, футболку. Не забудьте головной убор и солнцезащитный крем!")
#             else:
#                     print( "Тепло. Наденьте легкую одежду.")
#
# while True:
#     get_recommendation()
#
#     user_choice = input("\nХотите получить еще одну рекомендацию? (Введите любую цифру для выхода, или нажмите Enter для продолжения): ")
#
#     if user_choice.isdigit():
#         print("Завершение работы программы.")
#         break

# --- Обработка событий ---
# import pygame
# import sys
# import random
#
#
#
# # Инициализация Pygame
# pygame.init()
#
#
# # Настройки игрового поля
# WIDTH, HEIGHT = 800, 600  # Размеры экрана
# CELL_SIZE = 10 # Размер одной ячейки
# FPS = 10  # Частота обновления экрана
#
#
# # Настройка цветов
# FIELD_COLOR = (0, 0, 0)  # Цвет фона (черный)
# SNAKE_COLOR = (0, 255, 0)  # Цвет змейки (зеленый)
# FOOD_COLOR = (255, 0, 0)  # Цвет еды (красный)
# TEXT_COLOR = (255, 255, 255)  # Цвет текста (белый)
#
#
# # Создание окна
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Змейка на Python")
# clock = pygame.time.Clock()
#
#
# # Шрифт для отображения очков
# font = pygame.font.Font(None, 36)
#
#
# # Функция для отображения счета
# def draw_score(score):
#    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
#    screen.blit(score_text, (10, 10))
#
#
# # Функция для проверки столкновений
# def check_collision(position, snake_body):
#    return (
#        position in snake_body or
#        position[0] < 0 or
#        position[1] < 0 or
#        position[0] >= WIDTH or
#        position[1] >= HEIGHT
#    )
#
#
# # Основной игровой цикл
# def main():
#    snake = [(100, 100), (80, 100), (60, 100)]  # Начальная змейка
#    direction = "RIGHT"  # Начальное направление
#    food_position = (
#        random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
#        random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
#    )
#    score = 0
#    running = True
#
#
#    while running:
#        # Обработка событий
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#               pygame.quit()
#               sys.exit()
#            elif event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_w and direction != "DOWN":
#                    direction = "UP"
#                elif event.key == pygame.K_s and direction != "UP":
#                    direction = "DOWN"
#                elif event.key == pygame.K_a and direction != "RIGHT":
#                    direction = "LEFT"
#                elif event.key == pygame.K_d and direction != "LEFT":
#                    direction = "RIGHT"
#
#
#        # Обновление положения змейки
#        head_x, head_y = snake[0]
#        if direction == "UP":
#            head_y -= CELL_SIZE
#        elif direction == "DOWN":
#            head_y += CELL_SIZE
#        elif direction == "LEFT":
#            head_x -= CELL_SIZE
#        elif direction == "RIGHT":
#            head_x += CELL_SIZE
#        new_head = (head_x, head_y)
#
#
#        # Проверка столкновений
#        if check_collision(new_head, snake):
#            print(f"Игра окончена! Ваш счет: {score}")
#            running = False
#            break
#
#
#        # Добавление новой головы змейки
#        snake.insert(0, new_head)
#
#
#        # Проверка на съедение еды
#        if new_head == food_position:
#            score += 1
#            food_position = (
#                random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
#                random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
#            )
#        else:
#            snake.pop()  # Удаление последнего сегмента змейки
#       # Отрисовка элементов игры
#        screen.fill(FIELD_COLOR)  # Заливка фона
#        for segment in snake:
#            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))
#        pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(food_position[0], food_position[1], CELL_SIZE, CELL_SIZE))
#        draw_score(score)
#
#
#        pygame.display.flip()
#        clock.tick(FPS)  # Установка частоты обновления экрана
#
#
# # Запуск игры
# if __name__ == "__main__":
#    main()

