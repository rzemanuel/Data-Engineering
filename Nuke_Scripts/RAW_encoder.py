#import nuke
import glob

video_file_paths = sorted(glob.glob("/Volumes/A001/*.braw"))
kelvins = [2500,3200,4200,4700,5000,5600,6000,6500,7000]

for x in kelvins:
    
    
    for i in video_file_paths:
    
        temp = nuke.createNode('Read')
        temp['file'].setValue( i)
        temp['decode_using'].setValue('Clip Custom')
        temp['viewing_bmdgen'].setValue(5)
        temp['raw'].setValue(True)
        temp["white_balance_kelvin"].setValue(x)
        temp1 = nuke.createNode('Reformat')
        temp1['format'].setValue('HD_1080')
        temp2= nuke.createNode('Write')
        temp2['file'].setValue('/Volumes/Macintosh HD/Users/ryan/pipeline/EXR_Data' +str(x)+"_daylightSP_" + i.split('/')[-1].split('.')[0] + '.exr')
        temp2['raw'].setValue(True)
        temp2['file_type'].setValue('exr')
        nuke.execute(temp2,1,1)
        nuke.delete(temp)
        nuke.delete(temp2)
        nuke.delete(temp1)
