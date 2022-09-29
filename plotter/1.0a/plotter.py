

import bpy

scale_factor = 1
spacing = 1

coordinates = [
    (0,2),
    (1,6),
    (2,9),
    (3,3)
]

def add_bar(x, y):
    
    bpy.ops.mesh.primitive_plane_add(
        size = scale_factor * 1,
        enter_editmode = False,
        location = (x+0.5, 0, 0),
        scale = (0.8, 0.8, 1)
    )
    
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.mesh.extrude_region_move(
    
        #MESH_OT_extrude_region = {
         #   "use_normal_flip":False, 
          #  "use_dissolve_ortho_edges":False, 
           # "mirror":False
        #}, 
    
        TRANSFORM_OT_translate = {
            "value":(0, 0, y),  
            "constraint_axis":(False, False, True)
        }
    )

    bpy.ops.object.editmode_toggle()
    
    bpy.ops.transform.resize(value = (0.8, 0.8, 1))    
    
    
def plot():
    
    for coordinate in coordinates:
        add_bar(coordinate[0], coordinate[1])
        
        
if __name__ == "__main__":
    plot()