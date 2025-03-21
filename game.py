import pygame
from scripts import player
from scripts import asteroid

# helpful const definitions for later
TITLE = "py-asteroids"
WINDOW = (800, 600)
REFRESH = 60

def main() -> None:
    pygame.init()
    display = pygame.display.set_mode(WINDOW)
    pygame.display.set_caption('pysteroids')
    clock = pygame.time.Clock()
    active = True

    # Player init
    plr = player.Player()

    # asteroids init
    asteroids = [asteroid.Asteroid(WINDOW[0], WINDOW[1]) for _ in range(10)]

    dt = 1 / REFRESH

    # Logic / Rendering loop
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

        pkey = pygame.key.get_pressed() 
        
        # Update game objects
        for rock in asteroids:
            rock.update(dt)

        plr.update(dt, pkey, asteroids)

        # Blanking fill before drawing
        display.fill("black")

        # Draw game objects
        for rock in asteroids:
            rock.draw(display)

        plr.draw(display)

        pygame.display.flip()

        # in case we run out of asteroids
        if len(asteroids) <= 1:
            asteroids = [asteroid.Asteroid(WINDOW[0], WINDOW[1]) for _ in range(10)]

        dt = clock.tick(REFRESH) / 1000 

    pygame.quit()

if __name__ == "__main__":
    main()