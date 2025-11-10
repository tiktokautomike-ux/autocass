from moviepy.editor import ImageClip, AudioFileClip, TextClip, CompositeVideoClip
from gtts import gTTS
import os
from config import CONFIG

def create_video(image_path, name, config=CONFIG):
    os.makedirs(os.path.join(config["output_dir"], "videos"), exist_ok=True)
    video_path = os.path.join(config["output_dir"], "videos", f"{name}.mp4")
    tts_text = f"What if {name} was real?"
    tts = gTTS(tts_text)
    audio_path = os.path.join(config["output_dir"], f"{name}_voice.mp3")
    tts.save(audio_path)
    image_clip = ImageClip(image_path).set_duration(7)
    audio_clip = AudioFileClip(audio_path)
    text_clip = TextClip(tts_text, fontsize=60, color='white', size=config["video_resolution"])
    text_clip = text_clip.set_duration(7).set_position(("center", "bottom"))
    final_clip = CompositeVideoClip([image_clip, text_clip])
    final_clip = final_clip.set_audio(audio_clip)
    final_clip.write_videofile(video_path, fps=config["video_fps"], codec='libx264')
    return video_path