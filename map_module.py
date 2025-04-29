import pygame
import json
import os
import random
import wanderingMonster

map_width = 10
map_height = 10
tile_size = 32
screen_width = map_width * tile_size
screen_height = map_height * tile_size
map_state_file = "map_state.json"

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)


'''Call the get_default_state function to set positions on the map.'''
def get_default_state():
    '''This function is used to set and call the positions of the town, player and monsters at the inital start.
    
    Arguments:
    None.

    Return:
    player_positon, town_position, monsters
    
    '''
    town_pos = [5, 5]
    monsters = [wanderingMonster.Monster(), wanderingMonster.Monster()]
    return {
        "player_position": town_pos,
        "town_position": town_pos,
        "monsters": monsters
    }


'''Call generate_monster_position to generate the monsters position on the map during play.'''
def generate_monster_position(town_pos):
    '''This function is used to generate the position of the monsters as they move around the map.
    Makes sure that the monster can't generate on the town position.
    
    Arguments:
    town_pos

    Return:
    pos

    '''
    while True:
        pos = [random.randint(0, map_width - 1), random.randint(0, map_height - 1)]
        if pos != town_pos:
            return pos


'''Call show_map to populate the game screen, set movements and graphics.'''
def show_map(state):
    '''This function is used to set the screen up, adjust movement speed, generate graphics, and monster interaction.
    
    Arguments:
    state

    Return:
    result
    
    '''
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Explore Map")

    clock = pygame.time.Clock()
    running = True

    player_x, player_y = state["player_position"]
    monsters = state["monsters"]
    town_x, town_y = state["town_position"]

    result = None

    monster_move = 0

    while running:
        # Respawn monsters when all are dead
        if len(monsters) <= 0:
            state = respawn_monsters(state)
            monsters = state["monsters"]

        screen.fill(white)

        #Draw town.
        pygame.draw.circle(
            screen,
            green,
            (town_x * tile_size + tile_size // 2, town_y * tile_size + tile_size // 2),
            tile_size // 2 - 4,
        )

        #Draw monster if not defeated.
        for monster in monsters:
            try:
                monster_image = pygame.image.load('images/' + monster.name.lower() + ".png")
                screen.blit(monster_image, (monster.position[1] * tile_size, monster.position[0] * tile_size))
            except FileNotFoundError:
                pygame.draw.circle(
                    screen,
                    monster.color,
                    (monster.position[1] * tile_size + tile_size // 2, monster.position[0] * tile_size + tile_size // 2),
                    tile_size // 2 - 4,
                )

        #Draw player.
        try:
            player_image = pygame.image.load('images/player.png')
            screen.blit(player_image, (player_x * tile_size, player_y * tile_size))
        except FileNotFoundError:
            pygame.draw.rect(
                screen,
                blue,
                pygame.Rect(player_x * tile_size, player_y * tile_size, tile_size, tile_size)
            )

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                dx, dy = 0, 0
                if event.key == pygame.K_UP:
                    dy = -1
                elif event.key == pygame.K_DOWN:
                    dy = 1
                elif event.key == pygame.K_LEFT:
                    dx = -1
                elif event.key == pygame.K_RIGHT:
                    dx = 1

                new_x = max(0, min(map_width - 1, player_x + dx))
                new_y = max(0, min(map_height - 1, player_y + dy))

                player_x, player_y = new_x, new_y
                state["player_position"] = [player_x, player_y]

                if monster_move >= 1:
                    for monster in monsters:
                        monster.move()
                    monster_move = -1

                if [player_x, player_y] == [town_x, town_y]:
                    pygame.quit()
                    return "town", None

                for monster in monsters:
                    if [player_x, player_y] == [monster.position[1], monster.position[0]]:
                        pygame.quit()
                        return "battle", monster
                    
                monster_move += 1

        clock.tick(60)

    pygame.quit()
    return result


'''Call respawn_monsters to respawn two monsters.'''
def respawn_monsters(state):
    '''This function is used to call two monsters from the wanderingMonster.py file.
    
    Arguments:
    state

    Return:
    state
    
    '''
    state["monsters"] = [wanderingMonster.Monster(), wanderingMonster.Monster()]
    return state
