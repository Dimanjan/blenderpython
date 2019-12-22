import bpy

import time

def update_text(name):
    scene = bpy.context.scene
    
    scene = bpy.context.scene
    t=name+'-number'
    obj = scene.objects[t]
    cub = scene.objects[name]
        
        
    def recalculate_text(scene):
        l=cub.scale[0]  
        obj.data.body = '{0:.00f}'.format(l*200)

        
    bpy.app.handlers.frame_change_pre.append(recalculate_text)

update_text('Australia')
time.sleep(0.12)
update_text('Belgium')
time.sleep(0.12)
update_text('Brazil')
time.sleep(0.12)
update_text('Canada')
time.sleep(0.12)
update_text('China')
time.sleep(0.12)
update_text('Czech Republic')
time.sleep(0.12)
update_text('Finland')
time.sleep(0.12)
update_text('France')
time.sleep(0.12)
update_text('Germany')
time.sleep(0.12)
update_text('Greece')
time.sleep(0.12)
update_text('Hong Kong')
time.sleep(0.12)
update_text('India')
time.sleep(0.12)
update_text('Indonesia')
time.sleep(0.12)
update_text('Iran')
time.sleep(0.12)
update_text('Israel')
time.sleep(0.12)
update_text('Italy')
time.sleep(0.12)
update_text('Japan')
time.sleep(0.12)
update_text('Malaysia')
time.sleep(0.12)
update_text('Mexico')
time.sleep(0.12)
update_text('Netherlands')
time.sleep(0.12)
update_text('Poland')
time.sleep(0.12)
update_text('Portugal')
time.sleep(0.12)
update_text('Romania')
time.sleep(0.12)
update_text('Russian Federation')
time.sleep(0.12)
update_text('Singapore')
time.sleep(0.12)
update_text('South Korea')
time.sleep(0.12)
update_text('Spain')
time.sleep(0.12)
update_text('Sweden')
time.sleep(0.12)
update_text('Switzerland')
time.sleep(0.12)
update_text('Taiwan')
time.sleep(0.12)
update_text('Thailand')
time.sleep(0.12)
update_text('Turkey')
time.sleep(0.12)
update_text('United Kingdom')
time.sleep(0.12)
update_text('United States')
