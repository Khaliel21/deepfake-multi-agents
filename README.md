# 🧠 Deep Fake Agent - Multi-Agent GenAI System

> Un projet GenAI modulaire et multimodal basé sur **LangChain**, **LangGraph** et des modèles HuggingFace pour générer, manipuler et détecter des vidéos deepfake.

---

## 🚀 Description

**Deep Fake Agent** est un pipeline intelligent qui simule la création d'une vidéo synthétique à partir d'un script généré automatiquement, en passant par la voix, la vidéo, puis la détection de deepfake.  
L’ensemble du système est orchestré via **LangGraph** en utilisant une architecture **multi-agent**, chaque agent ayant une tâche dédiée.

---

## 🧩 Fonctionnalités

- ✅ Génération de script vidéo à partir de prompts
- ✅ Résumé automatisé du script
- ✅ Synthèse vocale avec gTTS
- ✅ Génération vidéo (texte + voix)
- ✅ Détection de deepfake via modèles HuggingFace
- ✅ Orchestration avec LangGraph (START → END)
- ✅ Agents typés, testables et réutilisables
- ✅ Journalisation détaillée à chaque étape

---

## 🛠️ Architecture

```mermaid
flowchart TD
    Start([Start])
    ScriptAgent[[Script Agent]]
    SummaryAgent[[Summary Agent]]
    VoiceAgent[[Voice Agent]]
    VideoAgent[[Video Agent]]
    DeepFakeAgent[[DeepFake Detector]]
    CheckerAgent[[Checker Agent]]
    End([End])

    Start --> ScriptAgent
    ScriptAgent --> SummaryAgent
    SummaryAgent --> VoiceAgent
    VoiceAgent --> VideoAgent
    VideoAgent --> DeepFakeAgent
    DeepFakeAgent --> CheckerAgent
    CheckerAgent --> End
🧠 Technologies & Modèles
LangChain / LangGraph : orchestration & LCEL

Pydantic : schémas typés pour les entrées/sorties

gTTS : synthèse vocale

MoviePy / PIL : génération vidéo

HuggingFace (via InferenceClient) :

dima806/deepfake_vs_real_image_detection

prithivMLmods/Deep-Fake-Detector-v2-Model

prithivMLmods/Deepfake-Real-Class-Siglip2

🧱 Structure du projet
bash
Copier
Modifier
deepfake-multi-agents/
│
├── agents/                  # Tous les agents LCEL (script, summary, voice, etc.)
│   ├── script_agent.py
│   ├── summary_agent.py
│   ├── voice_agent.py
│   ├── video_agent.py
│   ├── deepfake_agent.py
│   ├── checker_agent.py
│   └── graph.py            # Construction du graphe LangGraph
│
├── utils_graph/            # Fonctions utilitaires
│   ├── media_tools.py
│   └── langchain_utils.py
│
├── config/                 # Configuration
│   └── settings.py
│
├── assets/                 # Fichiers statiques (images, etc.)
│
├── data/                   # Prompts ou exemples
│   └── prompt.txt
│
├── main.py                 # Entrée principale du programme
├── uni_test_main.py        # Test unitaire du graphe
├── template.py             # Gabarit vidéo
├── load_env.py             # Chargement des variables .env
├── requirements.txt
└── README.md               # Ce fichier
⚙️ Installation
bash
Copier
Modifier
git clone https://github.com/Khaliel21/deepfake-multi-agents.git
cd deepfake-multi-agents
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
▶️ Lancer la démo
bash
Copier
Modifier
python main.py
Le pipeline s'exécute automatiquement de START à END, avec logs détaillés à chaque étape.

✅ Test rapide
Tu peux exécuter un test global du pipeline avec :

bash
Copier
Modifier
python uni_test_main.py
📌 À venir
🎤 Intégration de Bark ou ElevenLabs pour des voix plus réalistes

🎬 Génération vidéo via AI (Stable Video Diffusion)

🖼️ Interface Web avec Streamlit ou Gradio

📊 Tableau de bord avec LangSmith

🧑‍💻 Auteur
Dan Cohen
📍 Passionné par le Generative AI, la R&D et les architectures multi-agents intelligentes.

📝 Licence
Ce projet est sous licence MIT.
Feel free to use, fork, contribute & star ⭐