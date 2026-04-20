PROJECT_PHASE = "pre-launch"

ROLE_PRIORITY_MAP = {
    "mechanical_engineer": ["tolerance", "assembly", "CAD", "design", "fabrication", "part", "bracket", "mount", "clearance", "weld"],
    "electrical_engineer": ["firmware", "circuit", "PCB", "voltage", "sensor", "wiring", "calibration", "signal", "power", "current"],
    "supply_chain": ["supplier", "delay", "cost", "shipment", "order", "inventory", "stock", "lead time", "vendor", "procurement"],
    "engineering_manager": ["tolerance", "voltage", "sensor", "supplier", "delay", "blocked", "blocker", "milestone", "deadline", "risk", "demo", "assembly", "firmware", "shipment", "cost", "wiring", "dropping", "records", "training"],
    "product_manager": ["milestone", "deadline", "customer", "feature", "launch", "risk", "feedback", "roadmap", "demo", "requirement", "schedule"]
}

PHASE_CONTEXT = {
    "prototyping": "The team is in early prototyping. Design changes are expected and supplier delays are low priority.",
    "testing": "The team is in testing phase. Hardware failures, spec deviations, and integration bugs are highest priority.",
    "pre-launch": "The team is approaching launch. Any blockers, supplier delays, or unresolved hardware issues are critical and urgent."
}