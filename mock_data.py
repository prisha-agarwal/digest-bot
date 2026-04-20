MOCK_MESSAGES = [
    # mech-eng — design change nobody else knows about yet
    {"channel": "mech-eng", "user": "Alice (Mechanical)", "is_manager": False, "reactions": 2, "replied": False,
     "text": "Redesigned the motor mount bracket — shifted it 4mm left to improve clearance. Updated CAD is in the shared drive. Electrical team should check if this affects their wiring routes."},

    {"channel": "mech-eng", "user": "Alice (Mechanical)", "is_manager": False, "reactions": 3, "replied": False,
     "text": "Tolerance on part #A12 is off by 0.3mm. If we ship this it will cause assembly failures at the joint. Need sign-off on a fix before we cut any more parts."},

    # electrical — sensor issue that firmware and mech teams don't know about
    {"channel": "electrical", "user": "David (Electrical)", "is_manager": False, "reactions": 4, "replied": False,
     "text": "Voltage readings from the proximity sensor are inconsistent above 3.3V. This will cause false triggers during operation. Root cause is unclear — could be a wiring issue or a PCB trace problem."},

    {"channel": "electrical", "user": "David (Electrical)", "is_manager": False, "reactions": 1, "replied": True,
     "text": "Pushed a calibration fix for the motor controller circuit. Needs physical testing on the actual hardware before we can sign off."},

    # supply-chain — delay that nobody on engineering knows about yet
    {"channel": "supply-chain", "user": "Sarah (Supply Chain)", "is_manager": False, "reactions": 5, "replied": False,
     "text": "URGENT: Primary aluminum supplier flagged a 3 week delay on the chassis and bracket order. This directly affects mechanical assembly. No backup supplier is currently qualified."},

    {"channel": "supply-chain", "user": "Sarah (Supply Chain)", "is_manager": False, "reactions": 1, "replied": False,
     "text": "PCB components are stocked for first 30 units but the proximity sensor is on backorder — lead time is now 6 weeks. This affects electrical team's testing timeline."},

    # product — customer requirements engineering hasn't heard yet
    {"channel": "product", "user": "James (Product)", "is_manager": False, "reactions": 3, "replied": False,
     "text": "Customer confirmed they need the robot to operate in temperatures down to -20C. This is a new hard requirement for the demo. Not sure if our current hardware is rated for this."},

    {"channel": "product", "user": "James (Product)", "is_manager": False, "reactions": 2, "replied": False,
     "text": "Customer also moved up the delivery deadline by 2 weeks. We are now 3 weeks from final handoff. Engineering hasn't been looped in yet."},

    # general — manager announcements everyone needs to see
    {"channel": "general", "user": "Tom (Manager)", "is_manager": True, "reactions": 6, "replied": True,
     "text": "3 weeks to customer handoff. All blockers need to be logged and resolved by end of this week. No exceptions."},

    {"channel": "general", "user": "Tom (Manager)", "is_manager": True, "reactions": 3, "replied": True,
     "text": "Launch readiness review is Friday 2pm. Every team lead needs a written status update covering open issues, dependencies, and risks."},
]
