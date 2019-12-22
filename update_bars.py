
import bpy,csv      

def update_bars():
    with open(r'E:/aipapers.csv','r') as f:
        reader = list(csv.reader(f))
        reader=reader[1:]
        bpy.context.scene.frame_set(200)
        current_frame=200
        for j in dict:
            cube = bpy.data.objects[j]
            cube.location[1]=-5
            cube.keyframe_insert(data_path="location")
            
            cube.scale[0] = 1
            cube.keyframe_insert(data_path="scale")
        
        for i in range(2019-1996):
            current_frame += 50
            bpy.context.scene.frame_set(current_frame)
            rank=0
            period=21
            
                
            for row in reader[i*period:i*period+20]:
                rank += 1
            
            
            
                year=int(row[0])
                country=row[1]
                number=int(row[2])
            
                year_gap=year-1996
            
                cube = bpy.data.objects[country]
                flag= bpy.data.objects[dict[country][:-4]]
                text=bpy.data.objects[country+'-text']
                num=bpy.data.objects[country+'-number']
            
                cube.location[0]=number/400
                num.location[0]=number/200 +2
                
                if rank<16:
                    cube.location[1]=2.5*(15-rank)
                    flag.location[1]=2.5*(15-rank)
                    text.location[1]=2.5*(15-rank)-0.75
                    num.location[1]=2.5*(15-rank)-0.75
                else:
                    cube.location[1]=-10
                    flag.location[1]=-10
                    text.location[1]=-10-0.5
                    num.location[1]=-10-0.5
                    
                cube.location[2]=rank/1000
                cube.keyframe_insert(data_path="location")
                flag.keyframe_insert(data_path="location")
                text.keyframe_insert(data_path="location")
                num.keyframe_insert(data_path="location")
        
                cube.scale[0] = number/200
                
                cube.keyframe_insert(data_path="scale")
            

update_bars()
