
def _load_knowledge_graph() -> dict:
    """加载知识图谱，缓存于模块级。"""
    global _KG_CACHE
    if _KG_CACHE is not None:
        return _KG_CACHE
    kg_path = os.environ.get(
        "KNOWLEDGE_GRAPH_PATH",
        str(Path(__file__).parent.parent.parent / "knowledge_base" / "math" / "knowledge_graph.json"),
    )
    with open(kg_path, "r", encoding="utf-8") as f:
        _KG_CACHE = json.load(f)
    return _KG_CACHE

def _get_prerequisites(kp_id: str) -> list[str]:
    """获取某知识点的先修列表。"""
    kg = _load_knowledge_graph()
    for kp in kg.get("knowledge_points", []):
        if kp["id"] == kp_id:
            return list(kp.get("prerequisites", []))
    return []