
import subprocess
import uuid
import shutil



output_fast = 'static/videos/output_fast.mp4'

command2 = [
    f"ffmpeg", "-i", "gifs/All_gifs_2.mp4", "-vf", "setpts=0.09*PTS", "-an", "-y", {output_fast}
]
# Join the command into a single string for printing
#command_str2 = " ".join(command2)
#print("Command2:", command_str2)
# Run ffmpeg
subprocess.run(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#uid = str(uuid.uuid4())  # Generate a unique ID using uuid
#mp4_zoom =  f"/home/jack/Desktop/HDD500/collections/vids/Zoom_{uid}.mp4"
#shutil.copyfile(output_fast, mp4_zoom)  