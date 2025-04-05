# ?? Deep Fake Agent - Multi-Agent GenAI System

> Un projet GenAI modulaire et multimodal bas� sur **LangChain**, **LangGraph** et des mod�les HuggingFace pour g�n�rer, manipuler et d�tecter des vid�os deepfake.

---

## ?? Description

**Deep Fake Agent** est un pipeline intelligent qui simule la cr�ation d'une vid�o synth�tique � partir d'un script g�n�r� automatiquement, en passant par la voix, la vid�o, puis la d�tection de deepfake.  
L�ensemble du syst�me est orchestr� via **LangGraph** en utilisant une architecture **multi-agent**, chaque agent ayant une t�che d�di�e.

---

## ?? Fonctionnalit�s

- ? G�n�ration de script vid�o � partir de prompts
- ? R�sum� automatis� du script
- ? Synth�se vocale avec gTTS
- ? G�n�ration vid�o (texte + voix)
- ? D�tection de deepfake via mod�les HuggingFace
- ? Orchestration avec LangGraph (START ? END)
- ? Agents typ�s, testables et r�utilisables
- ? Journalisation d�taill�e � chaque �tape

---

## ??? Architecture

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
?? Technologies & Mod�les
LangChain / LangGraph : orchestration & LCEL

Pydantic : sch�mas typ�s pour les entr�es/sorties

gTTS : synth�se vocale

MoviePy / PIL : g�n�ration vid�o

HuggingFace (via InferenceClient) :

dima806/deepfake_vs_real_image_detection

prithivMLmods/Deep-Fake-Detector-v2-Model

prithivMLmods/Deepfake-Real-Class-Siglip2

?? Structure du projet
bash
Copier
Modifier
deepfake-multi-agents/
?
??? agents/                  # Tous les agents LCEL (script, summary, voice, etc.)
?   ??? script_agent.py
?   ??? summary_agent.py
?   ??? voice_agent.py
?   ??? video_agent.py
?   ??? deepfake_agent.py
?   ??? checker_agent.py
?   ??? graph.py            # Construction du graphe LangGraph
?
??? utils_graph/            # Fonctions utilitaires
?   ??? media_tools.py
?   ??? langchain_utils.py
?
??? config/                 # Configuration
?   ??? settings.py
?
??? assets/                 # Fichiers statiques (images, etc.)
?
??? data/                   # Prompts ou exemples
?   ??? prompt.txt
?
??? main.py                 # Entr�e principale du programme
??? uni_test_main.py        # Test unitaire du graphe
??? template.py             # Gabarit vid�o
??? load_env.py             # Chargement des variables .env
??? requirements.txt
??? README.md               # Ce fichier
?? Installation
bash
Copier
Modifier
git clone https://github.com/Khaliel21/deepfake-multi-agents.git
cd deepfake-multi-agents
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
?? Lancer la d�mo
bash
Copier
Modifier
python main.py
Le pipeline s'ex�cute automatiquement de START � END, avec logs d�taill�s � chaque �tape.

? Test rapide
Tu peux ex�cuter un test global du pipeline avec :

bash
Copier
Modifier
python uni_test_main.py
?? � venir
?? Int�gration de Bark ou ElevenLabs pour des voix plus r�alistes

?? G�n�ration vid�o via AI (Stable Video Diffusion)

??? Interface Web avec Streamlit ou Gradio

?? Tableau de bord avec LangSmith

????? Auteur
Dan Cohen
?? Passionn� par le Generative AI, la R&D et les architectures multi-agents intelligentes.

?? Licence
Ce projet est sous licence MIT.
Feel free to use, fork, contribute & star ?