import runpod
from modules.image_gen import generate_realistic_image
from modules.video_gen import create_video
from modules.utils import log_message, load_config

def run(job):
    config = load_config()
    name = job["input"].get("name", "Homer Simpson")
    log_message(f"🎬 Starting job for: {name}")
    image_path = generate_realistic_image(name, config)
    video_path = create_video(image_path, name, config)
    log_message(f"✅ Video created: {video_path}")
    return {"status": "success", "video_path": video_path}

runpod.serverless.start({"handler": run})