import sys

from pygame import QUIT, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP, KEYUP, K_ESCAPE, K_p

from class_dodge_cars import *

pygame.init()

width = 800  # WIDTH OF THE SCREEN
height = 600  # HEIGHT OF THE SCREEN
FPS = 40  # FRAME RATE
white = (255, 255, 255)
light_red = (255, 0, 0)
red = (150, 0, 0)
light_green = (0, 255, 0)
green = (0, 150, 0)
yellow = (255, 229, 10)
light_yellow = (212, 255, 10)
black = (0, 0, 0)
road_color = (47, 47, 47)

display = pygame.display.set_mode((width, height))  # DISPLAY SURFACE OBJECT
pygame.display.set_caption("Welcome to International Speedway!")  # CAPTION
clock = pygame.time.Clock()  # TIME OBJECT
CarImg = pygame.image.load("car.png")  # LOADING CAR IMAGE
RoadImg1 = pygame.image.load("road1.jpg")  # LOADING ROAD IMAGE
TreeImg1 = pygame.image.load("longtree1.jpg")  # LOADING TREE IMAGE
TreeImg2 = pygame.image.load("longtree2.jpg")
bugatti = pygame.image.load("Bugatti.png")
GameIcon = pygame.image.load("GameIcon.png")
pygame.display.set_icon(GameIcon)
life = 2  # LIFE OF THE GAMER
previous_score = DodgeCars(display=pygame.display.set_mode((width, height)), current_car=True, current_height=True,
                           current_width=True, dead_score_object=True,
                           dead_score_surface=True, score1=True, score2=True, opponent_cars=True,
                           opponent_car_height_width=True, random_number=True, opponent_car_start_x=True,
                           opponent_car_start_y_list=True, opponent_car_start_y=True, score_object=True,
                           score_surface=True, score=True, current_car2=True, opponent_car_start_y2=True)

previous_score.previous_score()
EndGame = False
GamePaused = False

just_in = DodgeCars(display=pygame.display.set_mode((width, height)), current_car=True, current_height=True,
                    current_width=True, dead_score_object=True,
                    dead_score_surface=True, score1=True, score2=True, opponent_cars=True,
                    opponent_car_height_width=True, random_number=True, opponent_car_start_x=True,
                    opponent_car_start_y_list=True, opponent_car_start_y=True, score_object=True,
                    score=True, score_surface=True, current_car2=True, opponent_car_start_y2=True)


def entry_screen():
    entry = True
    display.fill(white)

    while entry:

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        color_tuple = (red, yellow, green)
        color = color_tuple[random.randint(0, 2)]
        display_message("Dodge the Cars!", 70, 400, 100, color)
        display_message("Made By: Tim Tarver", 20, 650, 20, black)
        just_in.blit_image(bugatti, 175, 200)
        interactive(250, 450, 20, green, light_green, "Start!")
        interactive(400, 450, 20, yellow, light_yellow, "Ready!")
        interactive(550, 450, 20, red, light_red, "Quit!")

        pygame.display.update()
        clock.tick(30)


mouse_x, mouse_y = 0, 0
click_x, click_y = 0, 0
mouse_clicked = False


def interactive(center_x, center_y, radius, icolor, a_color, message):
    global mouse_x, mouse_y
    global click_x, click_y
    global mouse_clicked

    for event in pygame.event.get():

        if event.type == MOUSEMOTION:

            mouse_x, mouse_y = event.pos

        elif event.type == MOUSEBUTTONDOWN:

            click_x, click_y = event.pos
            mouse_clicked = True

        elif event.type == MOUSEBUTTONUP:

            click_x, click_y = event.pos
            mouse_clicked = True

    # print (mouse_x,mouse_y)
    left_x = center_x - radius
    left_y = center_y - radius
    width_c = height_c = 2 * radius  # Width And Height of rect bounding circle

    if left_x < mouse_x < (left_x + width_c) and left_y < mouse_y < (left_y + height_c):

        just_in.lights(center_x, center_y, radius, a_color)
        display_message(message, 20, center_x, center_y + 50, black)

        if 230 < click_x < (230 + 40) and 430 < click_y < (430 + 40) and mouse_clicked is True:

            mouse_clicked = False
            global life
            global GamePaused

            if life == -1:

                life = 2
                enter_game()
                main()

            elif GamePaused:

                GamePaused = False
                pygame.mixer.music.unpause()

            else:

                enter_game()
                main()
        elif 530 < click_x < (530 + 40) and 430 < click_y < (430 + 40) and mouse_clicked is True:

            pygame.quit()
            sys.exit()
    else:
        just_in.lights(center_x, center_y, radius, icolor)
        display_message(message, 20, center_x, center_y + 50, black)


def car_crash(opponent_car_start_x, opponent_car_start_y, count):
    enter_current_score = DodgeCars(display=pygame.display.set_mode((width, height)),
                                    current_car=True, current_height=True, current_width=True, dead_score_object=True,
                                    dead_score_surface=True, score1=True, score2=True, opponent_cars=True,
                                    opponent_car_height_width=True, random_number=True, opponent_car_start_x=True,
                                    opponent_car_start_y_list=True, opponent_car_start_y=True, score_object=True,
                                    score_surface=True, score=True, current_car2=True, opponent_car_start_y2=True)

    sound_object = pygame.mixer.Sound('shot.wav')
    sound_object.play()
    explosion(opponent_car_start_x, opponent_car_start_y)
    enter_current_score.enter_current_score(count)
    # display_message("EXPLODED",100,width/2,height/2,black)
    life_count()
    time.sleep(2)
    main()


def explosion(opponent_car_start_x, opponent_car_start_y):
    explosion_image = pygame.image.load('explosion.gif')
    display.blit(explosion_image, (opponent_car_start_x, opponent_car_start_y))
    pygame.display.update()


def display_message(text, size, x, y, color):
    text_object = pygame.font.Font("Roboto-Regular.ttf", size)
    text_surface = text_object.render(text, True, color)
    rectangular_surface = text_surface.get_rect()
    rectangular_surface.center = (x, y)
    display.blit(text_surface, rectangular_surface)
    pygame.display.update()


def life_count():
    global life
    life -= 1

    if life == -1:

        game_over = DodgeCars(display=pygame.display.set_mode((width, height)), current_car=True, current_height=True,
                              current_width=True, dead_score_object=True,
                              dead_score_surface=True, score1=True, score2=True, opponent_cars=True,
                              opponent_car_height_width=True, random_number=True, opponent_car_start_x=True,
                              opponent_car_start_y_list=True, opponent_car_start_y=True, score_object=True,
                              score_surface=True, opponent_car_start_y2=True, current_car2=True, score=True)

        game_over.gameover()

        while True:
            restart_page()


def restart_page():
    interactive(250, 450, 20, green, light_green, "Restart!")
    interactive(550, 450, 20, red, light_red, "Quit!")
    pygame.display.update()
    clock.tick(15)


def pause_button():
    global GamePaused
    pygame.mixer.music.pause()
    GamePaused = True

    while GamePaused:
        display_message("PAUSED", 100, width / 2, height / 2, black)
        interactive(250, 450, 20, green, light_green, "Continue!")
        interactive(550, 450, 20, red, light_red, "Quit!")
        pygame.display.update()
        clock.tick(30)


def enter_game():
    display.fill(road_color)
    road_x = 200
    road_y = -580
    tree_x1 = 0
    tree_y1 = 0
    tree_x2 = 605
    tree_y2 = 0
    start_number = DodgeCars(display=pygame.display.set_mode((width, height)), current_car=True, current_height=True,
                             current_width=True, dead_score_object=True,
                             dead_score_surface=True, score1=True, score2=True, opponent_cars=True,
                             opponent_car_height_width=True, random_number=True, opponent_car_start_x=True,
                             opponent_car_start_y_list=True, opponent_car_start_y=True, score_object=True,
                             score_surface=True, opponent_car_start_y2=True, current_car2=True, score=True)

    at_start_time = 3

    while at_start_time >= 0:

        start_number.blit_image(RoadImg1, road_x, road_y)  # CALLING FUNCTION TO BLIT ROAD IMAGE
        start_number.blit_image(TreeImg1, tree_x1, tree_y1)  # CALLING FUNCTION TO BLIT TREE IMAGE
        start_number.blit_image(TreeImg2, tree_x2, tree_y2)  # CALLING FUNCTION TO BLIT TREE IMAGE

        if at_start_time == 0:

            display_message("GO!", 150, width / 2, height / 2, black)

        else:

            display_message(str(at_start_time), 150, width / 2, height / 2, black)
        at_start_time -= 1
        pygame.display.update()
        clock.tick(1)


'''-----------------------------------------------------------------------------------------------------------'''

pygame.mixer.music.load('gamemusic.mp3')
pygame.mixer.music.play(-1,0.0)

def main():
    object_1 = DodgeCars(display=pygame.display.set_mode((width, height)), current_car=True, current_height=True,
                         current_width=True, dead_score_object=True,
                         dead_score_surface=True, score1=True, score2=True, opponent_cars=True,
                         opponent_car_height_width=True, random_number=True, opponent_car_start_x=True,
                         opponent_car_start_y_list=True, opponent_car_start_y=True, score_object=True,
                         score_surface=True, opponent_car_start_y2=True, current_car2=True, score=True)

    object_2 = DodgeCars(display=pygame.display.set_mode((width, height)), current_car=True, current_height=True,
                         current_width=True, dead_score_object=True,
                         dead_score_surface=True, score1=True, score2=True, opponent_cars=True,
                         opponent_car_height_width=True, random_number=True, opponent_car_start_x=True,
                         opponent_car_start_y_list=True, opponent_car_start_y=True, score_object=True,
                         score_surface=True, opponent_car_start_y2=True, current_car2=True, score=True)

    objects = (object_1, object_2)  # LIST OF OBJECTS

    life_2 = DodgeCars(display=pygame.display.set_mode((width, height)), current_car=True, current_height=True,
                       current_width=True, dead_score_object=True,
                       dead_score_surface=True, score1=True, score2=True, opponent_cars=True,
                       opponent_car_height_width=True, random_number=True, opponent_car_start_x=True,
                       opponent_car_start_y_list=True, opponent_car_start_y=True, score_object=True,
                       score_surface=True, opponent_car_start_y2=True, current_car2=True, score=True)
    # OBJECT TO DISPLAY LIFE

    car_x = width * 0.4  # X-COORDINATE OF CAR
    car_y = height * 0.8  # Y-COORDINATE OF CAR
    car_width = 64  # WIDTH OF CAR
    car_height = 104  # Height Of The Car
    previous_score = DodgeCars(display=pygame.display.set_mode((width, height)), current_car=True, current_height=True,
                               current_width=True, dead_score_object=True,
                               dead_score_surface=True, score1=True, score2=True, opponent_cars=True,
                               opponent_car_height_width=True, random_number=True, opponent_car_start_x=True,
                               opponent_car_start_y_list=True, opponent_car_start_y=True, score_object=True,
                               score_surface=True, opponent_car_start_y2=True, current_car2=True, score=True)
    road_count = 1

    delta_x = 0  # CHANGE IN POSITION OF CAR MOVING RIGHT OR LEFT
    delta_y = 0

    '''thing_w = 50
    thing_h = 50
    thing_start_x =  random.randrange(200,Road_r-thing_w)
    thing_start_y = -500
    color = black
    thing_speed=7'''

    right_end_of_road = 600  # RightEnd
    current_car1, opponent_car_width1, opponent_car_height1 = objects[0].opponent_cars1()
    opponent_car_start_x1, opponent_car_start_y1 = objects[0].opponent_car_coordinates(right_end_of_road)
    opponent_car_speed1 = 7
    opponent_car_speed2 = 7
    opponent_car_speed3 = 9
    opponent_car_list_of_speeds = [opponent_car_speed1, opponent_car_speed2, opponent_car_speed3]  # SPEED OF THE CARS
    add_speed1 = opponent_car_list_of_speeds[0]
    add_speed2 = opponent_car_list_of_speeds[1]
    add_speed3 = opponent_car_list_of_speeds[2]

    opponent_car_speed_up = 15  # SPEED WHEN UPPER ARROW KEY IS PRESSED
    second_car_first_time = 1
    '''COORDINATES FOR SETTING THE IMAGE OF ROAD AND SIDE TREES'''

    road_x = 200
    road_y = -580
    tree_x1 = 0
    tree_y1 = -580
    tree_x2 = 605
    tree_y2 = -580
    move_road = 5
    move_tree1 = 5
    move_tree2 = 5
    temporary_road_speed = 0
    temporary_tree_speed1 = 5
    temporary_tree_speed2 = 5
    temporary_road_speed3 = 5
    count = 0  # SCORE
    up_press_count = 1

    global GamePaused
    global opponent_car_start_y2
    global current_car2
    global opponent_car_start_x2
    global opponent_car_width2
    global opponent_car_height2

    if not GamePaused:

        while not EndGame:

            display.fill(road_color)
            road_y += move_road
            tree_y1 += move_tree1
            tree_y2 += move_tree2

            if road_y > 10:
                road_y = -580

            if tree_y1 > 10:
                tree_y1 = -580
                tree_y2 = -580
            objects[0].blit_image(RoadImg1, road_x, road_y)  # CALLING FUNCTION TO BLIT ROAD IMAGE
            objects[0].blit_image(TreeImg1, tree_x1, tree_y1)  # CALLING FUNCTION TO BLIT TREE IMAGE
            objects[0].blit_image(TreeImg2, tree_x2, tree_y2)  # CALLING FUNCTION TO BLIT TREE IMAGE

            for event in pygame.event.get():  # RETURNING THE LIST OF THE OCCURRED EVENTS

                if event.type == pygame.QUIT:  # CHECKING FOR QUIT
                    pygame.quit()
                    sys.exit()
                if event.type == KEYUP:  # WHAT TO DO WHEN KEY IS RELEASED
                    if event.key == K_ESCAPE:  # IF KEY RELEASED WAS ESCAPE KEY
                        pygame.quit()
                        sys.exit()
                    elif event.key == K_p:
                        pause_button()

                if event.type == pygame.KEYDOWN:  # WHAT TO DO IF KEY WAS PRESSED DOWN

                    if event.key == pygame.K_LEFT:  # IF KEY WAS LEFT ARROW KEY
                        delta_x = -6

                    elif event.key == pygame.K_RIGHT:  # IF KEY WAS RIGHT ARROW KEY
                        delta_x = 6

                    elif event.key == pygame.K_UP:

                        if up_press_count == 1:
                            car_y += -15
                        up_press_count += 1
                        move_road = 10
                        move_tree1 = 10
                        move_tree2 = 10
                        add_speed1 = 14

                        if count >= 10:
                            add_speed2 = 17
                        if count >= 20:
                            add_speed3 += 3

                    elif event.key == pygame.K_DOWN:
                        delta_y = 5

                elif event.type == pygame.KEYUP:  # WHEN KEY IS RELEASED

                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:

                        delta_x = 0
                        delta_y = 0
                    elif event.key == pygame.K_UP:

                        if up_press_count > 1:
                            car_y += 15
                            up_press_count = 1
                        add_speed1 = opponent_car_list_of_speeds[0]
                        move_road = temporary_road_speed
                        move_tree1 = temporary_tree_speed1
                        move_tree2 = temporary_tree_speed2

                        if count >= 10:
                            add_speed2 = opponent_car_list_of_speeds[1]
                        if count >= 20:
                            add_speed3 = opponent_car_list_of_speeds[2]
            car_x += delta_x  # CHANGING COORDINATE OF THE CAR
            car_y += delta_y
            opponent_car_start_y1 += add_speed1  # MOVING THE OPPONENT CAR ALONG Y-AXIS
            objects[0].blit_image(CarImg, car_x, car_y)  # BLITING IMAGE OF CAR TO CHANGED COORDINATE
            objects[0].blit_image(current_car1, opponent_car_start_x1,
                                  opponent_car_start_y1)  # BLITING THE IMAGE OF OPPONENT CAR TO NEW COORDINATE

            if count >= 10:
                opponent_car_start_y2 += add_speed2
                objects[0].blit_image(current_car2, opponent_car_start_x2, opponent_car_start_y2)
            elif count > 20:
               opponent_car_start_y3 += add_speed3
               objects[0].Blit_Image(current_car3,opponent_car_start_x3,opponent_car_start_y3)

            objects[0].current_game_score(count)  # Displaying Current Score
            previous_score.previous_score()  # DISPLAYING PREVIOUS SCORE
            life_2.display_life(life)  # DISPLAYING LIFE OF THE PLAYER

            if car_x < 200 or car_x > (width - car_width - 200) or (
                    car_y + car_height) > height or car_y < 0:
                # TESTING: IF CAR TOUCHED THE SIDES OF THE ROAD
                car_crash(car_x, car_y, count)  # CALLING CRASH()

            if opponent_car_start_y1 > height:  # IF OPPONENT CAR CROSSES THE BOTTOM SCREEN

                if count > 10:
                    current_car1, opponent_car_width1, opponent_car_height1 = objects[0].opponent_cars1()
                    opponent_car_start_x1, opponent_car_start_y1 = objects[0].opponent_car_coordinates(
                        right_end_of_road)

                    while opponent_car_start_x2 < opponent_car_start_x1 < opponent_car_start_x2 + opponent_car_width2:
                        current_car1, opponent_car_width1, opponent_car_height1 = objects[0].opponent_cars1()
                        opponent_car_start_x1, opponent_car_start_y1 = objects[0].opponent_car_coordinates(
                            right_end_of_road)

                else:

                    current_car1, opponent_car_width1, opponent_car_height1 = objects[0].opponent_cars1()
                    opponent_car_start_x1, opponent_car_start_y1 = objects[0].opponent_car_coordinates(
                        right_end_of_road)
                count += 1
                add_speed1 += 0.5

                opponent_car_list_of_speeds[0] += 0.005
                temporary_road_speed += 0.004
                move_road += 0.004
                move_tree1 += 0.004
                move_tree2 += 0.004
                temporary_tree_speed1 += 0.004
                temporary_tree_speed2 += 0.004

                if count == 10:
                    current_car2, opponent_car_width2, opponent_car_height2 = objects[0].opponent_cars1()
                    opponent_car_start_x2, opponent_car_start_y2 = objects[0].opponent_car_coordinates(
                        right_end_of_road)

            if count > 10:

                if opponent_car_start_y2 > height:

                    current_car2, opponent_car_width2, opponent_car_height2 = objects[0].opponent_cars1()
                    opponent_car_start_x2, opponent_car_start_y2 = objects[0].opponent_car_coordinates(
                        right_end_of_road)

                    while opponent_car_start_x1 < opponent_car_start_x2 < opponent_car_start_x1 + opponent_car_width1:
                        opponent_car_start_x2, \
                            opponent_car_start_y2 = objects[0].opponent_car_coordinates(right_end_of_road)
                    add_speed2 += 0.5    

                    if second_car_first_time == 1:
                        opponent_car_list_of_speeds[1] += 0.015
                        second_car_first_time += 1
                    opponent_car_list_of_speeds[1] += 0.006
                    count += 1

                    if count == 20:
                        current_car3, opponent_car_width3, opponent_car_height3 = objects[0].opponent_cars()
                        opponent_car_start_x3, opponent_car_start_y3 = objects[0].opponent_car_coordinates(right_side_of_road)

            if count > 20:

                if opponent_car_start_y3 > height:

                    current_car3, opponent_car_width3, opponent_car_height3 = objects[0].opponent_cars()
                    opponent_car_start_x3, opponent_car_start_y3 = objects[0].opponent_car_coordinates(right_side_of_road)
                    add_speed3 += 0.5
                    opponent_car_list_of_speeds[2] += 0.5
                    count += 1
                     
            # IF Y-COORDINATES CROSS OVER

            if car_y < opponent_car_start_y1 + opponent_car_height1 and (car_y + car_height) > opponent_car_start_y1:

                if (opponent_car_start_x1 < car_x < opponent_car_start_x1 + opponent_car_width1) or (
                        opponent_car_start_x1 < car_x + car_width < opponent_car_start_x1 + opponent_car_width1):
                    car_crash(car_x, car_y - 20, count)

            if 10 < count <= 20:

                if car_y < opponent_car_start_y2 + opponent_car_height2 and \
                        (car_y + car_height) > opponent_car_start_y2:  # IF Y-COORDINATES CROSS OVER

                    if (opponent_car_start_x2 < car_x < opponent_car_start_x2 + opponent_car_width2) or (
                            opponent_car_start_x2 < car_x + car_width < opponent_car_start_x2 + opponent_car_width2):
                        car_crash(car_x, car_y - 20, count)

            if count > 20:

                if car_y < opponent_car_start_y3 + opponent_car_height3 and (car_y + car_height) > opponent_car_start_y3: #IF Y-COORDINATES CROSS OVER

                    if (car_x > opponent_car_start_x3 and car_x < opponent_car_start_x3 + opponent_car_width3) or (car_x + car_width > opponent_car_start_x3 and car_x + car_width < opponent_car_start_x3 + opponent_car_width3):

                        car_crash(car_x, car_y-20, count)

            pygame.display.update()
            clock.tick(FPS)


entry_screen()
pygame.quit()
sys.exit()
