import redis
import os
import subprocess

r = redis.Redis(host=os.environ.get('REDIS_HOST', 'localhost'), port=6379, db=0)

while True:
    task = r.blpop("video_tasks", timeout=0)
    if task:
        chunk_name = task[1].decode('utf-8')
        print(f"Processing: {chunk_name}")
        # convert video to 720p
        subprocess.run(f"ffmpeg -i chunks/{chunk_name} -vf scale=-1:720 -c:v libx264 output/{chunk_name} -y", shell=True)
        
r.hset("progress", chunk_name, "completed") # update to redis
