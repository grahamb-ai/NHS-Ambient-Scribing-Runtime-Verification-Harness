"""Minimum represented EPR mutation surface for AT-EPR-001.

This first runnable version deliberately reflects the architectural assumption under
challenge. It does not pre-install capability isolation before the initial bypass
attempt has been observed and preserved.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ClinicalNote:
    encounter_id: str
    text: str


@dataclass(frozen=True)
class MutationResult:
    status: str
    encounter_id: str


class RepresentedEPR:
    """In-memory represented EPR used only to make the route-closure claim falsifiable."""

    def __init__(self) -> None:
        self.records: dict[str, str] = {}

    def commit_note(self, note: ClinicalNote) -> MutationResult:
        # Initial state under challenge: mutation is directly callable.
        self.records[note.encounter_id] = note.text
        return MutationResult(status="EPR_MUTATION_FORMED", encounter_id=note.encounter_id)


def governed_commit(epr: RepresentedEPR, note: ClinicalNote, runtime_decision: str) -> MutationResult:
    """Minimal ordinary governed path for the first adversarial run.

    Runtime Authority is represented by the supplied deterministic decision. This is
    not yet the strengthened capability boundary; the bypass test intentionally calls
    the consequence surface without using this function.
    """
    if runtime_decision != "ALLOW":
        return MutationResult(status="MUTATION_DENIED_RUNTIME_AUTHORITY", encounter_id=note.encounter_id)
    return epr.commit_note(note)
