

import logging
from agents.graph import build_graph

graph = build_graph()


# Exécution du graph
input_data = {
    "topic": "Les deepfakes dans les médias"
}
logging.debug(f"Exécution du graph avec les données d'entrée : {input_data}")

try:
    result = graph.invoke(input_data)
    logging.debug("Exécution du graph terminée.")
except Exception as e:
    logging.error(f"Erreur lors de l'exécution du graph : {e}")

# Affichage des résultats
logging.debug("Affichage des résultats...")
print("?? Résultat de l'exécution LangGraph :")
print(f"Key Result: {result.keys()}")
print(f"Label : {result.get('label')}")
print(f"Confidence : {result.get('confidence')}")
print(f"Model Name : {result.get('model_used')}")
print(f"Comment : {result.get('comment')}")

#####################################################################################
