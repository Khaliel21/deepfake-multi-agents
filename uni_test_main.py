
###########################################################################################
######################### Script AGENTS TEST
###########################################################################################

# import logging
# from agents.script_agent import ScriptAgent

# # Setup des logs
# logging.basicConfig(level=logging.DEBUG)

# # Création de l'agent
# agent = ScriptAgent()

# # Input pour générer un script
# test_input = {
#     "topic": "L'impact des deepfakes sur la société"
# }

# # Appel de l'agent
# result = agent.invoke(test_input)

# # Affichage du résultat
# print("\n=== Résultat du ScriptAgent ===")
# print(result)


###########################################################################################
######################### Summary AGENTS TEST
###########################################################################################
import logging
from agents.summary_agent import SummaryAgent

# Setup des logs
logging.basicConfig(level=logging.DEBUG)

# Création de l'agent
agent = SummaryAgent()

# Exemple de script
test_input = {
    "script": """
    Les deepfakes sont des vidéos ou audios générés par intelligence artificielle, capables de reproduire des visages ou des voix de façon extrêmement réaliste. 
    Utilisés à la fois pour des contenus humoristiques et des manipulations d'information, ils posent un réel défi pour les médias et la véracité des contenus en ligne.
    """
}

# Appel de l'agent
result = agent.invoke(test_input)

# Affichage du résultat
print("\n=== Résultat du SummaryAgent ===")
print(result)

###########################################################################################
######################### AUDIO AGENTS TEST
###########################################################################################
# import logging
# from agents.voice_agent import VoiceAgent

# # Setup des logs
# logging.basicConfig(level=logging.DEBUG)

# # Création de l'agent
# agent = VoiceAgent()

# # Exemple de résumé à transformer en voix
# test_input = {
#     "summary": """
#     Les deepfakes sont des vidéos ou audios générés par intelligence artificielle qui reproduisent des visages ou des voix de manière réaliste. 
#     Ils posent un défi pour les médias et la véracité des contenus en ligne.
#     """
# }

# # Appel de l'agent
# result = agent.invoke(test_input)

# # Affichage du résultat
# print("\n=== Résultat du VoiceAgent ===")
# print(result)


###########################################################################################
######################### Video AGENTS TEST
###########################################################################################

# import logging
# from agents.video_agent import VideoAgent
# import os

# # Setup des logs
# logging.basicConfig(level=logging.DEBUG)

# # Création de l'agent
# agent = VideoAgent()

# # Chemin du fichier audio généré par VoiceAgent (doit exister avant de lancer)
# audio_path = "data/narration.mp3"  # ← vérifie qu'il est bien là
# image_path = "assets/default.png"  # ← vérifie aussi que cette image existe

# # Crée le dossier "assets" + une image de fond par défaut si elle n'existe pas
# if not os.path.exists(image_path):
#     from PIL import Image
#     os.makedirs("assets", exist_ok=True)
#     Image.new("RGB", (1280, 720), color=(30, 30, 30)).save(image_path)
#     print(f"[INFO] Image de fond générée automatiquement à {image_path}")

# # Input de test
# test_input = {
#     "audio_path": audio_path
# }

# # Appel de l'agent
# result = agent.invoke(test_input)

# # Affichage du résultat
# print("\n=== Résultat du VideoAgent ===")
# print(result)

###########################################################################################
######################### DeepFake AGENTS TEST
###########################################################################################

# import logging
# from agents.deepfake_agent import DeepFakeAgent, DeepFakeDetectionInput

# # Setup des logs
# logging.basicConfig(level=logging.DEBUG)

# # Création de l'agent
# agent = DeepFakeAgent()

# # Input test avec la vidéo générée précédemment
# test_input = DeepFakeDetectionInput(video_path="data/output_video.mp4")

# # Appel de l'agent
# try:
#     result = agent.invoke(test_input)
#     print("\n=== Résultat du DeepFakeAgent ===")
#     print(result)
# except Exception as e:
#     print(f"\n❌ Erreur pendant l'invocation : {e}")