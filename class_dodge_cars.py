import random
import time

import pygame


class DodgeCars:

    def __init__(self, score, score1,
                 score2, display, dead_score_object,
                 opponent_cars, opponent_car_height_width, random_number,
                 current_car, current_width, current_height,
                 opponent_car_start_x, opponent_car_start_y_list, opponent_car_start_y,
                 score_object, score_surface, dead_score_surface,
                 opponent_car_start_y2, current_car2):
        
        self.display = display
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.width = 800
        self.height = 600
        self.GOImg = pygame.image.load('gameover.png')
        self.p_score = []
        self.score = score
        self.score1 = score1
        self.score2 = score2
        self.dead_score_object = dead_score_object
        self.dead_score_surface = dead_score_surface
        self.opponent_cars = opponent_cars
        self.opponent_car_height_width = opponent_car_height_width
        self.random_number = random_number
        self.current_car = current_car
        self.current_width = current_width
        self.current_height = current_height
        self.opponent_car_start_x = opponent_car_start_x
        self.opponent_car_start_y_list = opponent_car_start_y_list
        self.opponent_car_start_y = opponent_car_start_y
        self.score_object = score_object
        self.score_surface = score_surface
        self.opponent_car_start_y2 = opponent_car_start_y2
        self.current_car2 = current_car2

    def blit_image(self, image, x, y):

        self.display.blit(image, (x, y))

    def opponent_cars1(self):

        self.opp_cars = [pygame.image.load("caropp1.png"), pygame.image.load("BLUECAR.png"),
                         pygame.image.load("caropp3.png")]
        self.opponent_car_height_width = [(65, 104), (64, 106), (63, 104)]
        self.random_number = random.randrange(0, 3)
        self.current_car = self.opp_cars[self.random_number]
        self.current_width, self.current_height = self.opponent_car_height_width[self.random_number]
        return self.current_car, self.current_width, self.current_height

    def opponent_car_coordinates(self, right_end_of_road):

        self.opponent_car_start_x = random.randrange(200, right_end_of_road - 64)
        self.opponent_car_start_y_list = [-10, -20, -15, -12, -23]
        self.opponent_car_start_y = self.opponent_car_start_y_list[random.randrange(0, 4)]
        return self.opponent_car_start_x, self.opponent_car_start_y

    def current_game_score(self, count):

        self.score_object = pygame.font.Font("Roboto-Regular.ttf", 30)
        self.score_surface = self.score_object.render("Score: " + str(count), True, self.black)
        self.display.blit(self.score_surface, (0, 0))

    def gameover(self):

        self.display.blit(self.GOImg, (100, 200))
        pygame.display.update()
        time.sleep(2)

    @staticmethod
    def enter_current_score(c_score):

        write = open("highscore.txt", 'a')
        write.write('\n')
        write.write(str(c_score))
        write.close()

    def previous_score(self):

        read = open("highscore.txt", 'r')
        score = read.readlines()
        read.close()
        score1 = [x.rstrip() for x in score]
        score2 = [int(x) for x in score1]
        score2.sort()
        DodgeCars.show_previous_score(self, self.score)

    def show_previous_score(self, p_score):

        self.dead_score_object = pygame.font.Font("Roboto-Regular.ttf", 20)
        self.dead_score_surface = self.dead_score_object.render("Previous High Score: " + str(p_score),
                                                                True, self.black)
        self.display.blit(self.dead_score_surface, (0, 575))

    def display_life(self, life):

        self.score_object = pygame.font.Font("Roboto-Regular.ttf", 30)
        self.score_surface = self.score_object.render("Turns Left: " + str(life), True, self.black)
        self.display.blit(self.score_surface, (620, 0))

    def lights(self, center_x, center_y, radius, color):

        pygame.draw.circle(self.display, color, (center_x, center_y), radius)
