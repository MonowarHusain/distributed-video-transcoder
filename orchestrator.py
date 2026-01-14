import redis
import subprocess
import os

r = redis.Redis(host='localhost', port=6379, db=0)

def split_and_queue(video_name):
    # split in 5 sec
    if not os.path.exists('chunks'): os.makedirs('chunks')
    subprocess.run(f"ffmpeg -i input/{video_name} -f segment -segment_time 5 -c copy chunks/part%03d.mp4 -y", shell=True)
    
    # send to queue
    chunks = sorted([f for f in os.listdir('chunks') if f.startswith('part')])
    for chunk in chunks:
        r.rpush("video_tasks", chunk)
        print(f"Queued: {chunk}")

if __name__ == "__main__":
    split_and_queue("video.mp4") 
