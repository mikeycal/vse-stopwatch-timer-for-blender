# Video Sequence Editor Stopwatch & Timer for Blender

- Quickly add a stopwatch or timer to your blender video
- Count Up [Stopwatch] or Count Down [Timer]
- Places a sequential timestamp inside of each video frame using "Text Effect" strips.
- Encapsulates all the frames into a metastrip making it easy to select, move, and group property settings.
- Resize it, move it, change its color, add a shadow, use it with effect strips or even animate the property settings with keyframes. 
- This script works best when using integer frame rates such as 24, 25, 30, 50, 60 fps. [See Why](https://github.com/mikeycal/vse-stopwatch-timer-for-blender/issues/2)

## Demo (Timer followed by Stopwatch)

![Timer](https://github.com/mikeycal/vse-stopwatch-timer-for-blender/blob/master/imgs/example.gif)
 
 _(Background video: (CC) Blender Foundation - http://www.tearsofsteel.org)_
 
## Setup

1) Right Click on "Raw" -> "Save Link as..." on the following page:

https://github.com/mikeycal/vse-stopwatch-timer-for-blender/blob/master/vse_stopwatch_and_timer_for_blender.py

2) Open your Blender project

3) Set Project FPS, Start and End Frame (Script will create a timer between start and end frame)

4) Switch an "Editor Window" to "Text Editor" by the editor type from the Editor Menu

Here is what an Editor Menu is: https://docs.blender.org/manual/en/dev/editors/

5) Press "Open" and select "blender_vse_timer.py" in "Text Editor" window

6) Press "Run Script"

## Download a Source Code Editor that supports Python

At times you will need to edit this Python Script. So I would advise that you download a free Source Code editor for your platform of choice. Here are my recommendations (I use Gedit):
  - Windows: https://atom.io/, https://notepad-plus-plus.org/, https://wiki.gnome.org/Apps/Gedit
  - OSX: https://atom.io/, https://wiki.gnome.org/Apps/Gedit
  - GNU/Linux: https://atom.io/, https://wiki.gnome.org/Apps/Gedit, kate

## Settings
- Simply change the values listed below to alter the size and look
- Note:  A Stopwatch counts forward [default setting]. A Timer counts in reverse - aka a countdown

![Settings](https://github.com/mikeycal/vse-stopwatch-timer-for-blender/blob/master/imgs/settings.JPG)

- Change timer position:
  - Right click on the Meta Strip
  - Select "Image Offset"
  - Change X or Y values

## Get Font Color Values
-  Blender use RGBA floating point values. This means if you try to put in RGBA values that you got from a Color Picker online, the values won't give you the correct color. The easiest way to get the Text Color values, is to use Blender's color picker for the Text Effect Strip.

Here is how you get the color values that can be used in place of the 1's in the following script variables:
- time_color = (1,1,1,1)   [value is White]
- shadow_color = (0,0,0,1) [value is black]
  - an example of a blender RGBA value setting would be (0,**0.001**,1,1) which is blue
  
![color-picker](https://github.com/mikeycal/vse-stopwatch-timer-for-blender/blob/master/imgs/color-pick.gif)

## How long should the script take to create Timestamps
**(These are the results when using my INTEL i5 3570K 3.4Ghz processor)**

![times](https://github.com/mikeycal/vse-stopwatch-timer-for-blender/blob/master/imgs/times.JPG)

- That's right... It takes 10 1/2 hours to create 300,000 timestamps. 
- Setting _put_in_meta_strip = False_ may improve render time, but the Metastrip is easier to manipulate in the VSE. 
- It is also important to note that Render Resolution doesn't seem to have any affect on script run time.

## Special thanks:
- This script wouldn't be possible without the function provided at the following link:
http://stackoverflow.com/questions/1384406/python-convert-seconds-to-hhmmss/1384710#1384710
- Thanks to Paul McGuire: http://stackoverflow.com/users/165216/paul-mcguire
- Note: Stackoverflow code is provided under a cc by-sa 3.0 license. In section 4, part b, the cc by-sa 3.0 license, it states that users may choose to use "(ii) a later version of this License with the same License Elements as this License;" This allows me to switch to a cc by-sa 4.0 license, which is one-way compatible with the GPL 3. 

 ## Support Me
 
I consider this script a work in progress. If you have any suggestions on features, find bugs, or if you have added some feature that you think I should include, send me an email at mikeycaldotcom@yahoo.com . If you want to help me out, you can [send me a Paypal donation](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2EU5ANN3XVLH4) at my Yahoo address or help me make the code better by giving me your Python tips for better code. In addition, visit my website at http://Mikeycal.com and see what I'm up to lately. I am dedicated to providing cross platform resources and instructional videos free of charge. Checkout my Blender Video Editing Series at the following link:
 https://www.youtube.com/playlist?list=PLjyuVPBuorqIhlqZtoIvnAVQ3x18sNev4

[![Send a Donation to Mikeycal](https://github.com/mikeycal/the-video-editors-render-script-for-blender/blob/master/imgs/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2EU5ANN3XVLH4)
