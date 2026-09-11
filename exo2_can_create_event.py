from echo import echo

"""
Exercice 2 — Règle métier : peut-on créer un événement ?
Les consignes sont dans enonce.md (section EXO 2).
"""

active_user = {"name": "Fatima", "active": True}
inactive_user = {"name": "Igor", "active": False}

@echo
def can_create_event(title, capacity, organizer) -> list[str]:
    errs = []

    if 3 > len(title) < 100 : errs.append("err1")
    if capacity <= 0 : errs.append("err2")
    if not organizer["active"] : errs.append("err3")

    return errs


can_create_event("Concert Metal", 200, active_user)
can_create_event("AB", 200, active_user)
can_create_event("AB", -1, inactive_user)
can_create_event("Concert Metal", 0, active_user)
can_create_event("Concert Metal", 200, inactive_user)