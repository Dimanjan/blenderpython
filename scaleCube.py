import bpy 
from math import sin

bpy.context.scene.frame_set(1)
bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

cube = bpy.data.objects['Cube']

start_frame = 1
end_frame = start_frame + 100

while start_frame < end_frame:
    
    bpy.context.scene.frame_set(start_frame*3)
    
    x=sin(start_frame/10)*10
    
    bpy.context.object.scale[0] = x
    cube.keyframe_insert(data_path="scale")

    start_frame += 1
