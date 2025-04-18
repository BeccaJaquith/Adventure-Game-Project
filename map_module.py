import pygame
import json
import os
import random

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

def get_default_state():
    rand_town = [random.randint(0, map_width), random.randint(0, map_height)]
    return {
        "player_position": rand_town,
        "town_position": rand_town,
        "monster_position": [5, 5],
        "monster_defeated": False
    }

def load_map_state():
    if not os.path.exists(map_state_file):
        return get_default_state()

    with open(map_state_file, "r") as file:
        try:
            state = json.load(file)
        except json.JSONDecodeError:
            return get_default_state()

    default = get_default_state()
    for key in default:
        if key not in state:
            state[key] = default[key]

    return state

def save_map_state(state):
    with open(map_state_file, "w") as file:
        json.dump(state, file, indent=4)

def generate_monster_position(town_pos):
    while True:
        pos = [random.randint(0, map_width - 1), random.randint(0, map_height - 1)]
        if pos != town_pos:
            return pos

def show_map(state):
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Explore Map")

    clock = pygame.time.Clock()
    running = True

    player_x, player_y = state["player_position"]
    monster_x, monster_y = state["monster_position"]
    town_x, town_y = state["town_position"]
    monster_defeated = state.get("monster_defeated", False)

    result = None

    while running:
        screen.fill(white)

        #Draw town.
        pygame.draw.circle(
            screen,
            green,
            (town_x * tile_size + tile_size // 2, town_y * tile_size + tile_size // 2),
            tile_size // 2 - 4,
        )

        #Draw monster if not defeated.
        if not monster_defeated:
            pygame.draw.circle(
                screen,
                red,
                (monster_x * tile_size + tile_size // 2, monster_y * tile_size + tile_size // 2),
                tile_size // 2 - 4,
            )

        #Draw player.
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
                save_map_state(state)

                if [player_x, player_y] == [town_x, town_y]:
                    pygame.quit()
                    return "town"

                if [player_x, player_y] == [monster_x, monster_y] and not monster_defeated:
                    pygame.quit()
                    return "battle"

        clock.tick(60)

    pygame.quit()
    return result

def mark_monster_defeated():
    state = load_map_state()
    state["monster_defeated"] = True
    save_map_state(state)

def respawn_monster():
    state = load_map_state()
    state["monster_defeated"] = False
    state["monster_position"] = generate_monster_position(state["town_position"])
    save_map_state(state)