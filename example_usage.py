"""
Demonstration of genpark-inverted-file-index-ivf-voronoi-clusterer-skill
"""

from client import IVFVectorClustererClient

def main():
    ivf = IVFVectorClustererClient(nlist=2)

    training_data = [
        [0.1, 0.2], [0.15, 0.25],
        [0.8, 0.9], [0.85, 0.95]
    ]
    ivf.train_centroids(training_data)

    ivf.insert("p1", [0.12, 0.22])
    ivf.insert("p2", [0.14, 0.26])
    ivf.insert("p3", [0.82, 0.91])

    # Search with nprobe=1 (only checks cell for cluster 1)
    results = ivf.search_ivf([0.11, 0.21], nprobe=1, top_k=2)
    print("=== IVF VORONOI SEARCH RESULTS ===")
    for r in results:
        print(f"[{r['id']}] Distance: {r['distance']}")

if __name__ == "__main__":
    main()
