import os
import logging
from pathlib import Path

# Logging configuration to display actions
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] :%(message)s:')

files_to_create = [
    "agents/script_agent.py",
    "agents/voice_agent.py",
    "agents/video_agent.py",
    "agents/summary_agent.py",
    "agents/checker_agent.py",
    "agents/graph.py",
    "config/settings.py",
    "data/prompt.txt",
    "data/narration.mp3",
    "data/output_video.mp4",
    "utils_graph/media_tools.py",
    "utils_graph/langchain_utils.py",
    "main.py",
    "requirements.txt"
]

# Create the directories and files according to the defined structure
for file_path in files_to_create:
    file_path = Path(file_path)
    filedir, file_name = os.path.split(file_path)

    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {file_name}")
    
    # Create empty files if they don't exist or if the file size is 0
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
        logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{file_name} is already ready")

print("? Project structure created successfully.")