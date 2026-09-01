import json
import sys
from pathlib import Path

p = Path(sys.argv[1])
d = json.loads(p.read_text(encoding="utf-8"))
print("keys:", list(d.keys()))
print("cluster_inventory:", len(d.get("cluster_inventory", [])))
for ci in d.get("cluster_inventory", []):
    print("  ", {k: ci.get(k) for k in ("level", "object", "clusters_reported", "annotation_labels")})
print("verifications:", len(d.get("verifications", [])), "new_findings:", len(d.get("new_findings", [])))
for v in d.get("verifications", []):
    print(f"  [{v.get('candidate_index')}] {str(v.get('cell_type'))[:40]} ; {v.get('original_symbol')} ; {v.get('evidence_type')} ; {v.get('decision')} ; pol={v.get('marker_polarity')} ; cit={v.get('citation_verified')} ; layer={v.get('four_layer_category')}")
    print("      reason:", str(v.get("reason"))[:140])
for nf in d.get("new_findings", []):
    print(f"  NEW {str(nf.get('cell_type'))[:40]} ; {nf.get('original_symbol')} ; {nf.get('evidence_type')} ; {nf.get('decision')} ; cit={nf.get('citation_verified')}")
    print("      reason:", str(nf.get("reason"))[:140])
print("issues:", len(d.get("issues", [])))
for i in d.get("issues", []):
    print("  ", i.get("severity"), i.get("issue_type"), str(i.get("description"))[:120])
