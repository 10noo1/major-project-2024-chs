import math

music_list = []
lobbyMusic = 'Drops of H2O_FULL'
scoreboardMusic = 'Another way_FULL'

update_chart_flag = False


# player settings
stage_speed = 80
offset = 0
judgement_shown = False
guide_line_shown = False
music_pointer = 1 # 4
song_name = None # as a default
song_info_list = []

high_quality_verifying_graphics = False
sound_effect = [True]
particle_effect = [True]

creater_mode = False



# time settings
fps = 60 
main_loop_render_fps = 60

max_speed = 100 
min_speed = 15
max_offset = 1000
min_offset = -1000

# screen settings
line_number = 6
line_width = 80

width = line_number * line_width

line_axes = [(line_width//2) + line_width*(i+1) for i in range(line_number)]


option_key_x_level = width//2
option_key_y_level = 350

song_selection_key_x_level = width//2
song_selection_key_y_level = 550

button_y_offset = 25
button_x_size, button_y_size = 310,50



# node information
node_height = 20

line_length = 800
info_length = 200

height = line_length + info_length # this is equal to 'border line' position

node_spawning_y_pos = info_length + node_height//2

judgement_line_depth = node_height//2 + int(5 * (1000/60))  
judgement_line = height - judgement_line_depth  


# frame settings
guide_keys = ['F','G','H','J']
guide_key_size = len(guide_keys)
guide_y_loc = (judgement_line) + 50
guide_x_loc = line_width//2 + line_width


# some color settings
background_color = [(67, 18, 42),(242,193,217)]
line_color = (240,240,235)

node_color = [(187,167,247),(87, 67, 137)]

hold_color = [(190,190,190),(70,70,60)] # listify
holding_middle_color = (160,160,160)
not_holding_middle_color = (120,120,120)



bad_apple_color = (229,251,248)
bad_apple_toggled_color = (0,0,0)
red_color = (150,25,25)
debug_color = (67,209,189)

# GRADE SCORES BASED ON SCHOOL GRADES LMAO XD
score_grades = ['SUPER STAR','STAR','99.5 ATAR','EXTENSIVE','THROUGH','SOUND','BASIC','ELMENTARY','N AWARD']


score_colors = {'SUPER STAR':(0,221,192),'STAR':(25,224,198),'99.5 ATAR':(50,227,204),'EXTENSIVE':(76,231,210),'THROUGH':(102,234,217),'SOUND':(127,238,223),'BASIC':(153,241,229),'ELMENTARY':(178,244,236),'N AWARD':(204,248,242)}


def make_color_lighter(color):
    return min(color+100,255)

judgement_line_color = (make_color_lighter(background_color[0][0]),make_color_lighter(background_color[0][1]),make_color_lighter(background_color[0][2]))

# text settings
default_text_color = (0,220,220)
dark_text_color = (default_text_color[0]//2+10, default_text_color[1]//2+50, default_text_color[2]//2+50)
highlight_text_color = (200,230,255)
red_highlight_text_color = (240, 180, 180)
bar_color = (90,90,90)


frame_alpha_max = 100
frame_alpha = 0
frame_cycle = 2
frame_phase = 1/frame_cycle
frame_grad_color = 0

giant_text = 200
title_text = 50
sticker_text = title_text
big_text = 35  # 소제목 size
small_text = 20  # 설명용 text size
judgement_text = 20
tiny_text = 15
detail_text = 12

song_size_gradient = [22,18,15]
song_color_gradient = [(200,230,255),(180,220,235),(140,180,215)]


# song offsets
song_offsets = {'test': 0}

# jacket options
jacket_size = (300,300)
jacket_loc = (width//2 - jacket_size[0]//2, 180)
jacket_transition_size = (400,400)
jacket_transition_loc = (width//2 - jacket_size[0]//2, 300)


# back button
back_button_x_loc = width - big_text
back_button_y_loc = 0
