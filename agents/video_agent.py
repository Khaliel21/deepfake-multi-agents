from langchain_core.runnables import RunnableSerializable
from pydantic import BaseModel, Field
from typing import Any, Dict
import os
import logging

from moviepy import AudioFileClip, ImageClip, CompositeVideoClip

class VideoAgent(RunnableSerializable, BaseModel):
    name: str = Field(default="video_agent", description="Name of the agent")
    output_path: str = Field(default="data/output_video.mp4", description="Path to save the generated video")
    background_image: str = Field(default="assets/default.png", description="Path to background image")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__name__ = self.name

    def invoke(self, input: Dict[str, Any], config: Dict[str, Any] = None) -> Dict[str, Any]:
        logging.debug(f"VideoAgent input: {input}")
        
        audio_path = input.get("audio_path", "")
        logging.error(f"[video_agent] Invalid or missing audio_path: {audio_path}")
        if not audio_path or not os.path.exists(audio_path):
            return {"video_path": None, "success": False, "message": "Missing or invalid 'audio_path'."}

        try:
            os.makedirs(os.path.dirname(self.output_path), exist_ok=True)

            # Load audio and image
            audio = AudioFileClip(audio_path)
            image = ImageClip(self.background_image).with_duration(audio.duration)

            # Combine image + audio into a video clip
            video = image.with_audio(audio).with_fps(24)

            # Export video
            video.write_videofile(self.output_path, codec="libx264", audio_codec="aac", logger=None)
            logging.debug(f"Video path generated: {self.output_path}")

            return {
                "video_path": self.output_path,
                "success": True,
                "message": "Video generated successfully."
            }

        except Exception as e:
            return {
                "video_path": None,
                "success": False,
                "message": f"Failed to generate video: {str(e)}"
            }