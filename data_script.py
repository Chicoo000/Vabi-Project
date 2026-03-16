import json
import pandas as pd

# 1. Load the JSON file
with open('MC1_data/MC1_graph.json', 'r') as f:
    data = json.load(f)

# 2. Extract Nodes and save to CSV
nodes_df = pd.DataFrame(data['nodes'])
nodes_df.to_csv('MC1_nodes.csv', index=False)
print(f"Nodes saved! Total: {len(nodes_df)} rows")

# 3. Extract Links (Edges) and save to CSV
links_df = pd.DataFrame(data['links'])
links_df.to_csv('MC1_links.csv', index=False)
print(f"Links saved! Total: {len(links_df)} rows")