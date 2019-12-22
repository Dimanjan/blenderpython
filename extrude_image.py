import bpy

dict={'Australia': 'australia.png', 'Belgium': 'belgium.png', 'Brazil': 'brazil.png', 'Canada': 'canada.png', 'China': 'china.png', 'Czech Republic': 'czech-republic.png', 'Finland': 'finland.png', 'France': 'france.png', 'Germany': 'germany.png', 'Greece': 'greece.png', 'Hong Kong': 'hong-kong.png', 'India': 'india.png', 'Indonesia': 'indonesia.png', 'Iran': 'iran.png', 'Israel': 'israel.png', 'Italy': 'italy.png', 'Japan': 'japan.png', 'Malaysia': 'malasya.png', 'Mexico': 'mexico.png', 'Netherlands': 'netherlands.png', 'Poland': 'poland.png', 'Portugal': 'portugal.png', 'Romania': 'romania.png', 'Russian Federation': 'russia.png', 'Singapore': 'singapore.png', 'South Korea': 'south-korea.png', 'Spain': 'spain.png', 'Sweden': 'sweden.png', 'Switzerland': 'switzerland.png', 'Taiwan': 'taiwan.png', 'Thailand': 'thailand.png', 'Turkey': 'turkey.png', 'United Kingdom': 'united-kingdom.png', 'United States': 'us.png'}

bpy.context.scene.frame_set(200)

for i in dict:
    name=dict[i]
    bpy.ops.import_image.to_plane(files=[{"name":name, "name":name}], directory="C:\\Users\\diman_jung\\Desktop\\flags\\", align_axis='Z+', relative=False)
    print(i)
    #Extrude
    bpy.ops.object.editmode_toggle()
    extrude_z=1
    bpy.ops.mesh.extrude_context_move(MESH_OT_extrude_context={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, extrude_z), "orient_type":'NORMAL', "orient_matrix":((0, -1, 0), (1, 0, -0), (0, 0, 1)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":True, "use_accurate":False})
    bpy.ops.object.editmode_toggle()
    bpy.context.object.location[0] = -1
    bpy.context.object.location[1] = -5
    bpy.context.object.location[2] = -0.5
    bpy.context.object.keyframe_insert(data_path="location")



 
