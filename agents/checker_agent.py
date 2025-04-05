from langchain_core.runnables import RunnableSerializable
from pydantic import BaseModel, Field
from typing import Dict, Any
import os
from moviepy import VideoFileClip, AudioFileClip
import logging
import time

class CheckerAgent(RunnableSerializable, BaseModel):
    name: str = Field(default="checker_agent", description="Name of the agent")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__name__ = self.name

    def check_script(self, script: str) -> bool:
        # V�rifie que le script n'est pas vide et fait un certain nombre de caract�res
        if not script or len(script) < 50:
            return False
        return True

    # def check_audio(self, audio_path: str) -> bool:
    #     # V�rifie si le fichier audio existe et s'il n'est pas vide
    #     if not os.path.exists(audio_path):
    #         return False
    #     try:
    #         # On peut charger l'audio avec MoviePy pour v�rifier la validit�
    #         audio = AudioFileClip(audio_path)
    #         if audio.duration < 1:  # Si l'audio est trop court
    #             return False
    #     except Exception as e:
    #         return False
    #     return True

    def check_audio(self, audio_path: str) -> bool:
        if not os.path.exists(audio_path):
            print(f"Audio path not found: {audio_path}")
            return False

        print(f"Audio file size: {os.path.getsize(audio_path)} bytes")  # ?? log ajout� ici

        try:
            audio = AudioFileClip(audio_path)
            if audio.duration < 1:
                print("Audio duration too short")
                return False
        except Exception as e:
            print(f"Audio load error: {e}")  # ?? log de l'erreur exacte
            return False

        return True

    def check_video(self, video_path: str) -> bool:
        # V�rifie si le fichier vid�o existe
        if not os.path.exists(video_path):
            return False
        try:
            video = VideoFileClip(video_path)
            if video.duration < 1:  # Si la vid�o est trop courte
                return False
        except Exception as e:
            return False
        return True

    # def invoke(self, input: Dict[str, Any], config: Dict[str, Any] = None) -> Dict[str, Any]:
    #     logging.debug(f"CheckerAgent input: {input}")
    #     # On commence par v�rifier le script
    #     script = input.get("script", "")
    #     if not self.check_script(script):
    #         return {"success": False, "message": "Invalid script."}

    #     # On v�rifie ensuite l'audio
    #     audio_path = input.get("audio_path", "")
    #     if not self.check_audio(audio_path):
    #         return {"success": False, "message": "Invalid or missing audio."}

    #     # Enfin, on v�rifie la vid�o
    #     video_path = input.get("video_path", "")
    #     if not self.check_video(video_path):
    #         return {"success": False, "message": "Invalid or missing video."}

    #     # Si tout est valide
    #     return {"success": True, "message": "All files are valid."}

    # def invoke(self, input: Dict[str, Any], config: Dict[str, Any] = None) -> Dict[str, Any]:
    #     # V�rifie l'audio
    #     time.sleep(2)
    #     audio_path = input.get("audio_path", "")
    #     if not self.check_audio(audio_path):
    #         return {"success": False, "message": "Invalid or missing audio."}

    #     # V�rifie la vid�o
    #     video_path = input.get("video_path", "")
    #     if not self.check_video(video_path):
    #         return {"success": False, "message": "Invalid or missing video."}

    #     # Si tout est ok
    #     return {
    #         "success": True,
    #         "message": "All files are valid.",
    #         "video_path": video_path,
    #         "audio_path": audio_path
    #     }

    def invoke(self, input: Dict[str, Any], config: Dict[str, Any] = None) -> Dict[str, Any]:
        import time
        import logging
        time.sleep(1)

        logging.debug(f"CheckerAgent input: {input}")

        audio_path = input.get("audio_path", "")
        video_path = input.get("video_path", "")
        
        if not self.check_audio(audio_path):
            return {"success": False, "message": f"Invalid or missing audio: {audio_path}"}

        if not self.check_video(video_path):
            return {"success": False, "message": f"Invalid or missing video: {video_path}"}
        
        logging.debug(f"Fichier audio existe ? {os.path.exists(audio_path)} | Chemin: {audio_path}")

        return {
            "video_path": video_path,
            "audio_path": audio_path,  # <== ceci manquait
            "success": True,
            "message": "Video generated successfully."
        }