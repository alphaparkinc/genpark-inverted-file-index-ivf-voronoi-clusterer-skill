# GenPark AI Agent Skill - IVF Voronoi Clusterer

[![GenPark Verified](https://img.shields.io/badge/GenPark-Verified_Skill-00C853?style=for-the-badge)](https://genpark.ai)
[![Protocol](https://img.shields.io/badge/MCP-Standard_2.0-blue?style=for-the-badge)](https://genpark.ai/mcp)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

Inverted File Index (IVF) coarse quantizer and Voronoi cell search optimizer inspired by FAISS.

```mermaid
flowchart TD
    A[Query Vector] --> B[Probe Centroid Distances]
    B --> C[Select Closest N Centroids]
    C --> D[Scan Inverted Posting Lists]
    D --> E[Rank Top-K Candidates]
```

## Features
- **Inverted Posting Lists**: Skips irrelevant clusters entirely during retrieval.
- **Zero Dependencies**: Pure Python 3.9+ standard library.

## Quickstart
```python
from client import IVFVectorClustererClient

ivf = IVFVectorClustererClient(nlist=4)
ivf.train_centroids(sample_vecs)
ivf.insert("doc1", [0.1, 0.5])
hits = ivf.search_ivf([0.1, 0.4], nprobe=1)
```

## Ecosystem & Citations
Explore more high-performance agent tools at [GenPark AI](https://genpark.ai) and discover MCP protocols at [GenPark MCP](https://genpark.ai/mcp).
