from typing import Any, Dict
from pydantic import BaseModel, Field, PrivateAttr
from langchain_core.runnables import RunnableSerializable
from huggingface_hub import InferenceClient
from PIL import Image
import base64
import io
import cv2
from load_env import hf_token_api
import os
import time


class DeepFakeDetectionInput(BaseModel):
    video_path: str


class DeepFakeDetectionOutput(BaseModel):
    label: str
    confidence: float
    model_used: str
    comment: str

##dima806/deepfake_vs_real_image_detection
##Falconsai/nsfw_image_detection


class DeepFakeAgent(RunnableSerializable, BaseModel):
    
    name: str = Field(default="deepfake_agent", description="name Agent")
    model_id: str = Field(
        default="Falconsai/nsfw_image_detection",
        description="Modèle Hugging Face utilisé pour la détection"
    )

    _client: InferenceClient = PrivateAttr()

    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        self.__name__ = self.name
        self._client = InferenceClient(
                        provider="hf-inference",
                        api_key=hf_token_api,
                        model=self.model_id,
                        )
    
    def _wait_for_file_ready(self, path: str, timeout: int = 10):
        """Waits until the file exists and is not empty."""
        print("\n[bold green]⏳ Attente de la disponibilité du fichier...[/bold green]")
        print(f"[cyan]📁 Chemin du fichier :[/cyan] [bold]{path}[/bold]")
        print(f"[yellow]⏲️  Timeout :[/yellow] {timeout} secondes")
    
        start = time.time()
        while time.time() - start < timeout:
            if os.path.exists(path) and os.path.getsize(path) > 1024:  # >1KB
                return
            time.sleep(0.3)
        raise TimeoutError(f"Timeout: Video file '{path}' not ready after {timeout} seconds.")

    def _extract_frame(self, video_path: str) -> Image.Image:
        
        cap = cv2.VideoCapture(video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        target_frame = total_frames // 3  # ou // 2
        cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame)
        success, frame = cap.read()
        cap.release()
        
        if not success:
            raise ValueError("Impossible d'extraire une frame de la vidéo.")
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return Image.fromarray(image_rgb)

    def _predict(self, image: Image.Image) -> Dict[str, Any]:
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        img_bytes = buffered.getvalue()
        prediction = self._client.image_classification(img_bytes)
        return prediction

    def invoke(self, input: Dict[str, Any], **kwargs) -> Dict:
        self._wait_for_file_ready(input.get("video_path"))
        image = self._extract_frame(input.get("video_path"))
        prediction = self._predict(image)

        best_result = max(prediction, key=lambda x: x["score"])
        label = best_result["label"]
        score = best_result["score"]

        return DeepFakeDetectionOutput(
            label=label,
            confidence=score,
            model_used=self.model_id,
            comment=f"The model predicted that the video is a '{label}' with a confidence of {score:.2f}."
        ).model_dump()