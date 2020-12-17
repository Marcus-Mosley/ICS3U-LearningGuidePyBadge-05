#!/usr/bin/env python3
#
# Created by Marcus A. Mosley
# Created on December 2020
# This program is the "Space Aliens" program on the PyBadge

import ugame
import stage

import constants


def game_scene():
    # this function is the main game game_scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16(
        "space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16(
        "space_aliens.bmp")

    # set the background to image 0 in the image bank
    #     and the size (10x8 tiles of size 16X16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, constants.TOTAL_NUMBER_OF_ALIENS,
                        75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    # create a stage for the background to show up on
    #     and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites, items show up in order
    game.layers = [ship] + [background]
    # render all sprites
    #    most likely you will only render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # A button to fire
        if keys & ugame.K_X != 0:
            print("A")
        if keys & ugame.K_O != 0:
            print("B")
        if keys & ugame.K_START != 0:
            print("Start")
        if keys & ugame.K_SELECT != 0:
            print("Select")

        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        # update game logic

        # redraw Sprite
        game.render_sprites([ship])
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    game_scene()
