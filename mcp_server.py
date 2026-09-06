"""
MCP Server for genpark-inverted-file-index-ivf-voronoi-clusterer-skill
Standard JSON-RPC 2.0 protocol over stdio.
"""

import sys
import json
from client import IVFVectorClustererClient

client = IVFVectorClustererClient()

def handle_request(req):
    req_id = req.get("id")
    method = req.get("method")
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ivf_ready"}}

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
