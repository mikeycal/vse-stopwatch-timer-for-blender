########################### BEGIN GPL LICENSE BLOCK ############################
#
#     THE BLENDER VSE STOPWATCH AND TIMER
#     Copyright (C) 2017 Mike Meyers 
#
#     This program is free software; you can redistribute it and/or
#     modify it under the terms of the GNU General Public License as 
#     published by the Free Software Foundation; either version 3 
#     of the License, or (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#     
#     You should have received a copy of the GNU General Public License
#     along with this program; if not, write to the Free Software Foundation,
#     Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
############################ END GPL LICENSE BLOCK #############################

#________________________________<[ CREDITS ]>__________________________________
#
# "secondsToStr()" function was provided by Paul McGuire under the CC BY-SA 4.0 
# Currently, the "CC BY-SA 4.0" License is "one way" compatible with the GPL 3 
# Link to code:
# http://stackoverflow.com/questions/1384406/python-convert-seconds-to-hhmmss/1384710#1384710
# Link to Paul McGuire's Stack Exchange profile:
# http://stackoverflow.com/users/165216/paul-mcguire
#
# All other code written by Mike Meyers
#_______________________________________________________________________________

#____________________________<[ SUPPORT \ CONTACT ]>____________________________
#
#                  Programmed by Mike "Mikeycal" Meyers
#                   Website: http://www.mikeycal.com
#   Blender Video Editing Tutorials: https://www.youtube.com/user/MikeycalDOTcom
#   Support Email [Paypal Donations Email] : mikeycaldotcom@yahoo.com
#_______________________________________________________________________________

#______________________________<[ INSTRUCTIONS ]>_______________________________
#
# SOURCE LOCATION: https://github.com/mikeycal/blender-vse-stopwatch-and-timer
#
#   1) Set the [ User Preferences ] in this script
#   2) Open Blender -> Switch any Blender Window to "Text Editor"
#   3) Click "Open" (bottom of Text Editor) and select this Python File 
#   4) Set the FPS and FRAME RANGE in the Blender render properties window
#   5) Click "Run Script" (Bottom of Text Editor)
#   6) Blender will create timestamps for the length of the FRAME RANGE
#   7) If blender (Not Responding) the script is still running - wait for it. 
#   8) Known Issues: https://github.com/mikeycal/blender-vse-stopwatch-and-timer/issues  
#_______________________________________________________________________________

import bpy
from functools import reduce

#---------------------------- [ USER PREFERENCES ] ----------------------------
                                                                               # | A Stopwatch counts forward [default setting]. A Timer counts in reverse - aka a countdown
count_in_reverse = False        # (Default: False) [True, False]                 | False = Stopwatch. True = Timer 
show_starting_zero_frame = True # (Default: True) [True, False]                  | Creates a 00:00:00.000 start frame when counting up - placed outside frame range
show_ending_zero_frame = True   # (Default: True) [True, False]                  | Creates a 00:00:00.000 end frame when doing countdown - placed outside frame range 
                                                                               # | Frame 1 should be > 0 time. We place 0's outside of the Frame Range.
#time format
show_hours = True          # (Default: True) [True, False]
show_minutes = True        # (Default: True) [True, False]
show_seconds = True        # (Default: True) [True, False]
show_milliseconds = True   # (Default: True) [True, False] 

#time style
time_font_size = 200       # (Default: True) [int value] 
time_color = (1,1,1,1)     # Default: (1,1,1,1) (Red, Green, Blue, Alpha)        | eg: White is (1,1,1,1) | Black is (0,0,0,1)
shadow = True              # (Default: True) [True, False]
shadow_color = (0,0,0,1)   # Default: (0,0,0,1) (Red, Green, Blue, Alpha)   

put_in_meta_strip = True   # (Default: True) [True, False]                       | It's much easier to manipulate as a single Meta Strip

#-------------------------------------------------------------------------------

# function to convert floating point number of seconds to hh:mm:ss.sss
def secondsToStr(t):                                                           
    return "%02d:%02d:%02d.%03d" % \
        reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
            [(t*1000,),1000,60,60])

found_scene = False

for scene in bpy.data.scenes:
    if not found_scene:
        scene_name = scene.name 
        the_framerate = scene.render.fps / scene.render.fps_base
        start_at_frame = scene.frame_start
        end_frame_of_project = scene.frame_end 
        total_number_of_frames = end_frame_of_project - start_at_frame + 1  
        found_scene = True
        the_channel = 1
        try:
            for seq in scene.sequence_editor.sequences_all:                    #  | Place strips above highest strip
                if seq.channel > the_channel:
                    the_channel = seq.channel + 1
        except AttributeError:                                                 #  | When VSE is empty, there is no Attribute , so we catch the error.
            print("VSE EMPTY")

the_time_in_secs = total_number_of_frames / the_framerate
time_per_frame = the_time_in_secs / total_number_of_frames

if not count_in_reverse: 
    new_time_per_frame = 0.0
else:
    new_time_per_frame = the_time_in_secs + time_per_frame

first_time_in_loop = True

seq = bpy.context.scene.sequence_editor_create()
bpy.ops.sequencer.select_all(action='DESELECT')                                #  | This prevents other strips from being put in metastrip

while start_at_frame <= total_number_of_frames:   
    seq.sequences.new_effect(str(start_at_frame), type='TEXT', channel=1, \
    frame_start=start_at_frame, frame_end=(start_at_frame+1))

    if not count_in_reverse:
        if first_time_in_loop and show_starting_zero_frame: 

            seq.sequences.new_effect("pre_frame", type='TEXT', channel=1, \
            frame_start=start_at_frame - 1, frame_end=start_at_frame)

            full_time = secondsToStr(0)   

            h, m, s = full_time.split(':')
            s, ms = s.split('.')

            final_print_string = ""    

            if show_hours: 
                final_print_string += h + ":"  
            if show_minutes:
                final_print_string += m + ":" 
            if show_seconds:
                final_print_string += s
            if show_milliseconds:
                final_print_string += "." + ms 

            seq.sequences["pre_frame"].text = final_print_string
            seq.sequences["pre_frame"].font_size = time_font_size
            seq.sequences["pre_frame"].color = time_color
            seq.sequences["pre_frame"].use_shadow = shadow
            seq.sequences["pre_frame"].shadow_color = shadow_color

            first_time_in_loop = False

        new_time_per_frame += time_per_frame
    else:
        new_time_per_frame = new_time_per_frame - time_per_frame

    full_time = secondsToStr(new_time_per_frame)   

    h, m, s = full_time.split(':')
    s, ms = s.split('.')

    final_print_string = ""    

    if show_hours: 
        final_print_string += h + ":"  
    if show_minutes:
        final_print_string += m + ":" 
    if show_seconds:
        final_print_string += s
    if show_milliseconds:
        final_print_string += "." + ms 

    seq.sequences[str(start_at_frame)].text = final_print_string
    seq.sequences[str(start_at_frame)].font_size = time_font_size
    seq.sequences[str(start_at_frame)].color = time_color
    seq.sequences[str(start_at_frame)].use_shadow = shadow
    seq.sequences[str(start_at_frame)].shadow_color = shadow_color

    start_at_frame += 1
    
    if start_at_frame > total_number_of_frames and count_in_reverse \
    and show_ending_zero_frame:
        seq.sequences.new_effect("post_frame", type='TEXT', channel=1, \
        frame_start=start_at_frame, frame_end=start_at_frame + 1)

        full_time = secondsToStr(0)   

        h, m, s = full_time.split(':')
        s, ms = s.split('.')

        final_print_string = ""    

        if show_hours: 
            final_print_string += h + ":"  
        if show_minutes:
            final_print_string += m + ":" 
        if show_seconds:
            final_print_string += s
        if show_milliseconds:
            final_print_string += "." + ms 

        seq.sequences["post_frame"].text = final_print_string
        seq.sequences["post_frame"].font_size = time_font_size
        seq.sequences["post_frame"].color = time_color
        seq.sequences["post_frame"].use_shadow = shadow
        seq.sequences["post_frame"].shadow_color = shadow_color

if put_in_meta_strip:
    bpy.ops.sequencer.meta_make()
    my_metastrip = bpy.context.scene.sequence_editor.active_strip.name
    bpy.data.scenes[scene_name].sequence_editor.sequences_all[my_metastrip].blend_type = "ALPHA_OVER"
