import pygame
from var import *
from music_ import *
from text_write import *
from image_processor import *
from chart import *
from song_selection import *


pygame.init()  #
clock = pygame.time.Clock()
# screen size: 1920 x 1080

screen = pygame.display.set_mode((width, height))  # window 
pygame.display.set_caption('RYTHME')  #  title
width, height = pygame.display.get_surface().get_size()  #  width, height

screen.fill(background_color[0])  # background coloUr

# main screen ---------------------------------------------------
run = True
meta_run = True

def exit():
    pygame.quit()
    return False, False

while meta_run:
    global stage_speed, offset, judgement_shown, guide_line_shown, high_quality_verifying_graphics, music_list, music_pointer, song_name
    # The Music in main
    music_Q(lobbyMusic,True)
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # QUIT
                run, meta_run = exit()
                break

            if event.type == pygame.MOUSEMOTION:
                # FOLLOWS THE PLAYERS MOUSE
                # point.pos = pygame.mouse.get_pos()
                pass

            if event.type == pygame.MOUSEBUTTONUP:
                (xp, yp) = pygame.mouse.get_pos()
                mouse_particle_list.append((pygame.time.get_ticks(),(xp, yp)))
                mouse_click_sound()


                if abs(xp - song_selection_key_x_level) < big_text*6:
                    if abs(yp - (song_selection_key_y_level)) < big_text:
                        print('SONG SELECTED')
                        run = False
                        music_list, music_pointer, song_name = song_selection_screen(screen,clock,stage_speed, offset, judgement_shown, guide_line_shown, high_quality_verifying_graphics)
                        #prints the music infos
                        break



            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # esc to exit
                    run, meta_run = exit()
                    break

                elif event.key == pygame.K_RETURN:
                    print('back to the past!')
                    run = False
                    music_list, music_pointer, song_name = song_selection_screen(screen, clock, stage_speed, offset,
                                                                                 judgement_shown, guide_line_shown,
                                                                                 high_quality_verifying_graphics)
                    break



        if not run:
            break

        screen.fill(background_color[0])

        write_text(screen, width//2, height//8 , 'made this game in 2 weeks help', big_text, background_color[0], highlight_text_color)

        write_text(screen, option_key_x_level, option_key_y_level,
                   'Options', big_text, background_color[0],
                   highlight_text_color)
        pygame.draw.rect(screen, highlight_text_color, [width//4 - big_text, option_key_y_level - button_y_offset, button_x_size, button_y_size], 4,8)

        write_text(screen, song_selection_key_x_level, song_selection_key_y_level,
                   'SHOW!!!', big_text, background_color[0],
                   highlight_text_color)
        pygame.draw.rect(screen, highlight_text_color, [width//4 - big_text,  song_selection_key_y_level - button_y_offset, button_x_size, button_y_size], 4,8)

        write_text(screen, width // 2, height-small_text*4, 'noobs guide! ', small_text, background_color[0],
                   highlight_text_color)
        write_text(screen, width // 2, height-small_text*2, 'press %s,%s,%s,%s to the beat'%(guide_keys[0],guide_keys[1],guide_keys[2],guide_keys[3]), small_text, background_color[0],
                   highlight_text_color)



        pygame.display.flip()
        clock.tick(main_loop_render_fps)