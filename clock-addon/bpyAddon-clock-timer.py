

import bpy


# add text object
bpy.ops.object.text_add()
bpy.data.objects['Text'].name = 'timer'
obj = bpy.data.objects['timer']


# clears text
def clean_text():    
    obj.data.body = '00:00'


# set time accoring to user input  
def set_time(time_value):
    obj.data.body = time_value        


# returns current playback time
def get_playback_time():

    scene = bpy.context.scene

    fps = scene.render.fps / scene.render.fps_base
    frame = scene.frame_current

    return frame / fps


# convert seconds to timecode
def seconds_to_timecode(sec):

    minutes = "%02d" % int(sec / 60)
    seconds = "%02d" % int(sec % 60)

    return ''.join([minutes, ':', seconds])


# updates clock with playback time
def set_clock(scene):

    global START_TIME
    
    current_time = get_playback_time()

    secs = START_TIME + current_time

    if secs > 0:
        timecode = seconds_to_timecode(secs)
    else:
        timecode = '00:00'

    obj = scene.objects['timer']
    obj.data.body = timecode
    

if __name__ == "__main__":
     
    clean_text()
    
    START_TIME = 60 * 5 + 34
    bpy.app.handlers.frame_change_pre.append(set_clock)
