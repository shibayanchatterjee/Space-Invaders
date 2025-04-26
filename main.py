import pygame as pyg

pyg.init()

def main():
    # Game loop
    running = True
    while running:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                running = False


if __name__ == "__main__":
    main()
