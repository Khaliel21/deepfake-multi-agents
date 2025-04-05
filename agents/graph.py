
from langgraph.graph import StateGraph, START, END
from langchain_core.runnables import RunnablePassthrough,RunnableLambda
from agents.script_agent import ScriptAgent
from agents.summary_agent import SummaryAgent
from agents.voice_agent import VoiceAgent
from agents.video_agent import VideoAgent
from agents.checker_agent import CheckerAgent
from agents.deepfake_agent import DeepFakeAgent, DeepFakeDetectionInput
from pydantic import BaseModel, Field

import logging
from typing import Any, Dict, Optional


def build_graph():
    # Logging configuration
    logging.basicConfig(level=logging.DEBUG)

    # Agent initialization
    logging.debug("Initializing agents...")

    script_agent = ScriptAgent(name="script_agent")
    logging.debug(f"Agent {script_agent.name} initialized.")

    summary_agent = SummaryAgent(name="summary_agent")
    logging.debug(f"Agent {summary_agent.name} initialized.")

    voice_agent = VoiceAgent(name="voice_agent")
    logging.debug(f"Agent {voice_agent.name} initialized.")

    video_agent = VideoAgent(name="video_agent")
    logging.debug(f"Agent {video_agent.name} initialized.")

    deepfake_agent = DeepFakeAgent(name="deepfake_agent")
    logging.debug(f"Agent {deepfake_agent.name} initialized.")


    # Adding nodes to the graph
    logging.debug("Adding nodes to the graph...")
    
    graph_builder = StateGraph(dict)
    
    graph_builder.add_node("script", script_agent.invoke)
    logging.debug("Node 'script' added.")

    graph_builder.add_node("summary", summary_agent.invoke)
    logging.debug("Node 'summary' added.")

    graph_builder.add_node("voice", voice_agent.invoke)
    logging.debug("Node 'voice' added.")

    graph_builder.add_node("video", video_agent.invoke)
    logging.debug("Node 'video' added.")

    graph_builder.add_node("deepfake", deepfake_agent.invoke)
    logging.debug("Node 'deepfake' added.")



    # Defining edges (connections) between the nodes
    
    logging.debug("Defining connections between nodes...")
    graph_builder.add_edge(START, "script")
    logging.debug("Edge added: START -> script.")

    graph_builder.add_edge("script", "summary")
    logging.debug("Edge added: script -> summary.")

    graph_builder.add_edge("summary", "voice")
    logging.debug("Edge added: summary -> voice.")
    
    graph_builder.add_edge("voice", "video")
    logging.debug("Edge added: voice -> video.")


    graph_builder.add_edge("video", "deepfake")
    logging.debug("Edge added: voice -> video.")

    graph_builder.add_edge("deepfake", END)
    logging.debug("Edge added: video -> END.")

    # Compiling the graph
    logging.debug("Compiling the graph...")
    graph = graph_builder.compile()
    logging.debug("Graph successfully compiled.")

    return graph 