

import bpy



# add text object
bpy.ops.object.text_add()
bpy.context.active_object

# clears text
def clean_text():
    bpy.ops.object.editmode_toggle()
    for i in range(0, 4):
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.move(type='NEXT_CHARACTER')
    bpy.ops.object.editmode_toggle()


# set time accoring to user input  
def set_initial_time(time_value):
    bpy.context.active_object    
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.text_insert(text=time_value, accent=False)
    bpy.ops.object.editmode_toggle()


clean_text()

t = '15:30'
set_initial_time(t)

# time updating logic
fps = bpy.data.scenes["Scene"].render.fps
frames = bpy.data.scenes["Scene"].frame_end
duration = frames / fps
sec = 0



# positions clock at the world origin
#bpy.context.active_object
#bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN')

