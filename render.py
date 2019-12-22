
import bpy


bpy.context.scene.frame_set(300)
bpy.context.scene.render.filepath = 'E:/300.png'
bpy.ops.render.render(write_still = True)
