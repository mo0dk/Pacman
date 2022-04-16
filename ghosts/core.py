from abc import ABC, abstractmethod
from typing import List, Literal, SupportsAbs, Type, Tuple, Union

import pygame

import global_variables
import player
from perfomance import img_load
from player import Pacman

Direction = Literal["left", "right", "up", "back", ""]
AnimationList = List[pygame.Surface]


class AbstractGhostLogic(ABC):
    # Абстрактный класс логики призрака. У каждого призрака есть своя логика.

    # noinspection PyUnusedLocal
    @abstractmethod
    def __init__(self, main_ghost: "MainGhost"):
        self.eyes = "./textures/ghosts/eyes.png"

    # default_position: pygame.Vector2
    @property
    @abstractmethod
    def default_position(self) -> pygame.Vector2:
        """Позиция в которой появляется призрак"""
        ...

    # back_animations: AnimationList
    @property
    @abstractmethod
    def back_animations(self) -> AnimationList:
        """список картинок, отвечающих за анимацию вниз"""
        ...

    # left_animations: AnimationList
    @property
    @abstractmethod
    def left_animations(self) -> AnimationList:
        """список картинок, отвечающих за анимацию налево"""
        ...

    # right_animations: AnimationList
    @property
    @abstractmethod
    def right_animations(self) -> AnimationList:
        """список картинок, отвечающих за анимацию направо"""
        ...

    # up_animations: AnimationList
    @property
    @abstractmethod
    def up_animations(self) -> AnimationList:
        """список картинок, отвечающих за анимацию наверх"""
        ...

    # scared_animations: AnimationList
    @property
    @abstractmethod
    def scared_animations_blue(self) -> AnimationList:
        """список картинок, отвечающих за анимацию наверх"""
        ...

    # speed: SupportsAbs
    @property
    @abstractmethod
    def speed(self) -> SupportsAbs:
        """Скорость призрака."""
        ...

    @property
    @abstractmethod
    def default_direction(self) -> Direction:
        """Направление по умолчанию. Если направление == "", то призрак не отрисовывается и не двигается."""
        ...

    @abstractmethod
    def where_am_i_should_move(self, pacman: Pacman, all_ghosts: List["MainGhost"], stage, trigger) -> Direction:
        """Функция выполняющаяся каждый кадр. Должна возваращать направление в котором будет двигаться призрак."""
        ...

    @abstractmethod
    def go_home(self):
        """Функция которая возвращает призрака в калитку."""
        ...

    @property
    @abstractmethod
    def eaten(self) -> int:
        ...

    @eaten.setter
    @abstractmethod
    def eaten(self, value: int) -> int:
        ...


class MainGhost:
    # Класс основного призрака. Он нужен для того что бы не дублировать код.

    # Если вы не понимаете что такое trigger_blocks, то прочитайте статью
    trigger_blocks = [
        [1, 1],
        [6, 1],
        [12, 1],
        [15, 1],
        [21, 1],
        [1, 5],
        [6, 5],
        [9, 5],
        [12, 5],
        [15, 5],
        [15, 8],
        [12, 8],
        [1, 8],
        [26, 8],
        [18, 5],
        [21, 5],
        [26, 5],
        [26, 1],
        [6, 8],
        [9, 8],
        [18, 8],
        [21, 8],
        [6, 14],
        [9, 14],
        [18, 14],
        [21, 14],
        [9, 17],
        [18, 17],
        [6, 20],
        [9, 20],
        [18, 20],
        [21, 20],
        [6, 23],
        [9, 23],
        [18, 23],
        [21, 23],
        [3, 26],
        [3, 23],
        [3, 20],
        [1, 20],
        [1, 23],
        [26, 23],
        [26, 20],
        [24, 26],
        [24, 23],
        [24, 20],
        [12, 29],
        [15, 29],
        [26, 29],
        [1, 29],

        # теперь нет
        [12, 11],
        [9, 11],
        [15, 11],
        [18, 11],
        [12, 23],
        [12, 26],
        [15, 26],
        [18, 26],
        [21, 26],
        [9, 26],
        [6, 26],
        [1, 26],
        [26, 26],
        [12, 20],
        [15, 20],
        [15, 23],
    ]

    @staticmethod
    def draw_trigger_blocks(screen: pygame.Surface):
        """Рисует trigger_blocks на экране"""
        for trigger_block in MainGhost.trigger_blocks:
            pygame.draw.rect(
                screen, (255, 0, 0),
                (int(global_variables.cell_size * trigger_block[0]),
                 50 + int(global_variables.cell_size * trigger_block[1]),
                 global_variables.cell_size, global_variables.cell_size
                 ),
                1
            )

    def __init__(self, ghost_logic: Type[AbstractGhostLogic], window=0):
        self.screen = window
        self._ghost_logic = ghost_logic(self)
        self._position = pygame.Vector2(self._ghost_logic.default_position.x, self._ghost_logic.default_position.y)
        self._direction: Direction = ""
        self._current_animation_frame = 0  # Текущий кадр
        self._current_animation_list: AnimationList = []  # Спосок текстур, отвечающих за анимацию в направлении где
        # направлен призрак
        self._current_speed = pygame.Vector2()  # Текущая скорость в x и y.
        self._timer = pygame.time.get_ticks()
        self._timer2 = pygame.time.get_ticks()
        self.direction = self._ghost_logic.default_direction
        self._scared = 0
        self.speed_mod = 1
        self.scare_timer = 0
        self.scare_mod = 1
        self.trigger = 0

    def _check_position(self):
        if player.game_map[self.position_in_blocks[1]][self.position_in_blocks[0]] == 0:
            print(f"[WARNING] Ghost {self} with {self.ghost_logic} in wall")

    def draw(self, screen: pygame.Surface):
        """Рисует призрака"""
        if not self._ghost_logic.eaten:
            self._check_position()
        # pygame.draw.rect(screen, (0, 0, 255), (self.ghost_logic.tar, int(self._position.y), 8, 8), 1)
        img = None
        position = None
        need_to_draw = True
        if self._scared and not self._ghost_logic.eaten:
            if pygame.time.get_ticks() - self._timer >= 200:  # Каждые 200 мс
                self._current_animation_frame += (1 + self.scare_mod)
                self._timer = pygame.time.get_ticks()
                if self._current_animation_frame >= (4 - self.scare_mod * 2):
                    self._current_animation_frame = 0
            img = img_load(self._ghost_logic.scared_animations_blue[self._current_animation_frame],
                           2 * global_variables.cell_size,
                           2 * global_variables.cell_size)
            position = (self._position.x - (global_variables.cell_size / 2),
                        self._position.y - (global_variables.cell_size / 2) + 50)
        elif self._ghost_logic.eaten:
            img = img_load(self._ghost_logic.eyes, 2 * global_variables.cell_size, 1.5 * global_variables.cell_size)
            position = (self._position.x - (global_variables.cell_size / 2),
                        self._position.y - (global_variables.cell_size / 2) + 50)
        elif self.direction != "":
            if pygame.time.get_ticks() - self._timer >= 200:  # Каждые 200 мс
                self._current_animation_frame += 1
                self._timer = pygame.time.get_ticks()
                if self._current_animation_frame >= len(self._current_animation_list):
                    self._current_animation_frame = 0
            img = img_load(self._current_animation_list[self._current_animation_frame],
                           2 * global_variables.cell_size, 2 * global_variables.cell_size)
            position = (self._position.x - (global_variables.cell_size / 2),
                        self._position.y - (global_variables.cell_size / 2) + 50)
        else:
            need_to_draw = False
        if need_to_draw:
            screen.blit(
                img,
                position
            )

    def update(self, pacman: Pacman, all_ghosts: List["MainGhost"], stage, trigger):
        """Двигает призрака и изменяет его направление"""

        if self._scared:
            if pygame.time.get_ticks() - self.scare_timer >= 7000:
                self.scared = 0
            if pygame.time.get_ticks() - self.scare_timer >= 4000:
                self.scare_mod = 0

        moved = False
        self.direction = self._ghost_logic.where_am_i_should_move(pacman, all_ghosts, stage,
                                                                  trigger)  # Направление куда должен
        # двигаться призрак
        if self._current_speed.x != 0:
            for _ in range(self._timer2, pygame.time.get_ticks(), abs(round(1000 // self._current_speed.x))):
                self._position.x += self._current_speed.x * self.speed_mod * \
                                    global_variables.difficulty * (global_variables.cell_size / 8)
                self.direction = self._ghost_logic.where_am_i_should_move(pacman, all_ghosts, stage,
                                                                          trigger)
                moved = True
        if self._current_speed.y != 0:
            for _ in range(self._timer2, pygame.time.get_ticks(), abs(round(1000 // self._current_speed.y))):
                self._position.y += self._current_speed.y * self.speed_mod * \
                                    global_variables.difficulty * (global_variables.cell_size / 8)
                self.direction = self._ghost_logic.where_am_i_should_move(pacman, all_ghosts, stage,
                                                                          trigger)
                moved = True
        if moved:
            self._timer2 = pygame.time.get_ticks()

    def reset_position(self):
        self._position.x = self.default_position.x
        self._position.y = self.default_position.y
        self._ghost_logic.stay = 1
        self._ghost_logic.stage = 1
        if self.default_position.y == 11 * global_variables.cell_size:
            self._direction = "right"
        self.scared = 0

    @property
    def direction(self) -> Direction:
        """Нарпавление в котором призрак смотрит"""
        return self._direction

    @direction.setter
    def direction(self, new_direction: Direction):
        if new_direction == "left":
            self._current_speed.x = -(abs(self._ghost_logic.speed))
            self._current_speed.y = 0
            self._current_animation_list = self._ghost_logic.left_animations
        elif new_direction == "right":
            self._current_speed.x = abs(self._ghost_logic.speed)
            self._current_speed.y = 0
            self._current_animation_list = self._ghost_logic.right_animations
        elif new_direction == "up":
            self._current_speed.x = 0
            self._current_speed.y = -(abs(self._ghost_logic.speed))
            self._current_animation_list = self._ghost_logic.up_animations
        elif new_direction == "back":
            self._current_speed.x = 0
            self._current_speed.y = abs(self._ghost_logic.speed)
            self._current_animation_list = self._ghost_logic.back_animations
        elif new_direction == "":
            self._current_speed.x = 0
            self._current_speed.y = 0
            self._current_animation_list = []
        else:
            raise ValueError("Parameter `new_direction` should be a 'left', 'right', 'up', 'back', or empty")
        self._direction = new_direction

    @property
    def turned_left(self) -> bool:
        """Возвращает True если призрак повёрнут налево, иначе False."""
        return self._direction == "left"

    @property
    def turned_right(self) -> bool:
        """Возвращает True если призрак повёрнут направо, иначе False."""
        return self._direction == "right"

    @property
    def turned_back(self) -> bool:
        """Возвращает True если призрак повёрнут вниз, иначе False."""
        return self._direction == "back"

    @property
    def turned_up(self) -> bool:
        """Возвращает True если призрак повёрнут навверх, иначе False."""
        return self._direction == "up"

    @property
    def position(self) -> pygame.rect.Rect:
        """Возвращает позицию призрака"""
        return pygame.rect.Rect(self._position.x, self._position.y, 2 * global_variables.cell_size,
                                2 * global_variables.cell_size)

    @position.setter
    def position(self, new_position: Union[pygame.rect.Rect, pygame.Vector2]):
        if isinstance(new_position, pygame.Vector2):
            self._position = pygame.rect.Rect(new_position.x, new_position.y,
                                              2 * global_variables.cell_size, 2 * global_variables.cell_size)
        self._position = new_position

    @property
    def position_in_blocks(self) -> Tuple[int, int]:
        """Возвращает позицию призрака в блоках."""
        return \
            round(self._position.x // global_variables.cell_size), round(self._position.y // global_variables.cell_size)

    @property
    def ghost_logic(self):
        return self._ghost_logic

    def force(self):
        self._position.x = int((self.position.x + global_variables.cell_size / 2) //
                               global_variables.cell_size) * global_variables.cell_size
        self._position.y = int((self.position.y + global_variables.cell_size / 2) //
                               global_variables.cell_size) * global_variables.cell_size

    def trigger_eaten(self):
        if not self.ghost_logic.eaten:
            self.ghost_logic.eaten = 1
            self.force()

    @property
    def default_position(self):
        return self._ghost_logic.default_position

    @property
    def scared(self):
        return self._scared

    @scared.setter
    def scared(self, val):
        if val:
            self._scared = 1
            self.speed_mod = 0.7
            self.scare_mod = 1
            self.scare_timer = pygame.time.get_ticks()
        else:
            self._scared = 0
            self.speed_mod = 1
            self._current_animation_frame = 0
