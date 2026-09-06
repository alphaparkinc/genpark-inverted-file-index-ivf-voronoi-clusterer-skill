"""
Inverted File Index (IVF) with Voronoi Cell Partitioning.
Zero external dependencies, standard library only.
"""

import math
from typing import Dict, List, Any, Optional, Tuple

class IVFVectorClustererClient:
    """
    Partitions vector space into Voronoi cells via coarse centroid clustering:
    - Assigns vector IDs to closest centroid posting list
    - Limits search scope to top-N closest Voronoi probe cells (nprobe)
    """

    def __init__(self, nlist: int = 3):
        self.nlist = nlist
        self.centroids = [] # List of centroid vectors
        self.posting_lists = {} # centroid_idx -> list of (doc_id, vector)

    def _euclidean_distance(self, v1: List[float], v2: List[float]) -> float:
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))

    def train_centroids(self, vectors: List[List[float]], max_iters: int = 5):
        """Initializes and refines coarse centroids via simple k-means."""
        if not vectors:
            return
        
        dim = len(vectors[0])
        # Simple deterministic initialization
        step = max(1, len(vectors) // self.nlist)
        self.centroids = [vectors[i * step] for i in range(min(self.nlist, len(vectors)))]
        for i in range(len(self.centroids)):
            self.posting_lists[i] = []

    def insert(self, doc_id: str, vector: List[float]):
        """Assigns vector to closest Voronoi centroid."""
        if not self.centroids:
            self.centroids = [vector]
            self.posting_lists[0] = [(doc_id, vector)]
            return

        best_c = 0
        min_dist = float("inf")
        for idx, c in enumerate(self.centroids):
            dist = self._euclidean_distance(vector, c)
            if dist < min_dist:
                min_dist = dist
                best_c = idx

        self.posting_lists[best_c].append((doc_id, vector))

    def search_ivf(self, query: List[float], nprobe: int = 1, top_k: int = 3) -> List[Dict[str, Any]]:
        """Searches only the top 'nprobe' closest Voronoi cells."""
        if not self.centroids:
            return []

        # Find closest centroids
        c_dists = [(idx, self._euclidean_distance(query, c)) for idx, c in enumerate(self.centroids)]
        c_dists.sort(key=lambda x: x[1])
        probed_centroids = [idx for idx, _ in c_dists[:nprobe]]

        candidates = []
        for c_idx in probed_centroids:
            for doc_id, vec in self.posting_lists.get(c_idx, []):
                dist = self._euclidean_distance(query, vec)
                candidates.append((doc_id, dist))

        candidates.sort(key=lambda x: x[1])
        return [{"id": d_id, "distance": round(dist, 4)} for d_id, dist in candidates[:top_k]]
