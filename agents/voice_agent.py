from langchain_core.runnables import RunnableSerializable
from pydantic import BaseModel, Field
from typing import Any, Dict
from gtts import gTTS
import os
import logging
from pydub import AudioSegment

class VoiceAgent(RunnableSerializable, BaseModel):
    name: str = Field(default="voice_agent", description="Name of the agent")
    output_path: str = Field(default="data/narration.mp3", description="Path to save generated audio")


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__name__ = self.name

    def invoke(self, input: Dict[str, Any], config: Dict[str, Any] = None) -> Dict[str, Any]:
        logging.debug(f"[voice_agent] Received input: {input}")

        logging.debug(f"[voice_agent] Received summary: {input.get('summary')}")
        
        ##or input.get("script", "")
        script = input.get("summary") 
        logging.debug(f"VoiceAgent received script: {script}")
        
        if not script:
            logging.error("[voice_agent] Missing 'script' or 'summary' in input.")
            return {"success": False, "message": "Missing 'script' or 'summary' in input.", "audio_path": None}

        try:
            # Generate speech using gTTS
            tts = gTTS(text=script, lang='en')
            os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
            tts.save(self.output_path)
            
            logging.debug(f"[VoiceAgent] ✅ Audio file successfully saved at: {self.output_path}")
            
            return {
                "audio_path": self.output_path,
                "success": True,
                "message": "Audio generated successfully."
            }
        except Exception as e:
            return {
                "audio_path": None,
                "success": False,
                "message": f"Failed to generate audio: {str(e)}"
            }

    def invoke_batch(self, inputs: list[Dict[str, Any]], config: Dict[str, Any] = None) -> list[Dict[str, Any]]:
        
        results = []
        for idx, item in enumerate(inputs):
            script = item.get("script", "")
            if not script:
                results.append({"audio_path": None, "success": False, "message": "Missing script."})
                continue
            try:               
                path_mp3 = f"data/narration_{idx}.mp3"
                tts = gTTS(text=script, lang='en')
                tts.save(path_mp3)
                results.append({"audio_path": path_mp3, "success": True, "message": "OK"})
            except Exception as e:
                results.append({"audio_path": None, "success": False, "message": f"Error: {str(e)}"})
        return results