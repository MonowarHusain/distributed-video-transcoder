# Distributed Video Transcoder

I built this to speed up video transcoding by splitting a big video into small chunks and processing them in parallel. It uses Redis as a task queue and multiple Docker workers to handle the heavy lifting.

### How it works
1. **Orchestrator**: Splits the `video.mp4` into 5-second segments using FFmpeg.
2. **Redis**: Stores the names of these segments in a list called `video_tasks`.
3. **Workers**: Three Docker containers (you can scale this) wait for tasks from Redis, transcode them to 720p, and save them to the `output` folder.
4. **Final Step**: Once the queue is empty, you just merge the chunks back together.



### Tech Stack
* **Python** (for the scripts)
* **Redis** (for the queue)
* **Docker** (to isolate and scale workers)
* **FFmpeg** (the actual engine)

### What you need
* Docker & Docker Compose
* FFmpeg installed on your main machine
* Python 3 + `redis-py` library

### Running it
1. Clone this repo:
   ```bash
   git clone[https://github.com/MonowarHusain/distributed-video-transcoder.git](https://github.com/MonowarHusain/distributed-video-transcoder.git)
   cd distributed-video-transcoder
