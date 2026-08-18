"""Represented EPR mutation boundary for AT-EPR-001.

After the preserved initial bypass failure, the consequence surface is strengthened so
that direct mutation requires a capability resolved by the governed Runtime Authority
path. This is an in-process reference-demonstrator mechanism, not a production IAM or
EPR security boundary.
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


class _ResolvedAuthorityCapability:
    """Opaque in-process capability used only by the represented governed path."""


_RESOLVED_AUTHORITY_CAPABILITY = _ResolvedAuthorityCapability()


class RepresentedEPR:
    """In-memory represented EPR used to exercise the consequence boundary."""

    def __init__(self) -> None:
        self.records: dict[str, str] = {}

    def commit_note(
        self,
        note: ClinicalNote,
        authority_capability: object | None = None,
    ) -> MutationResult:
        if authority_capability is not _RESOLVED_AUTHORITY_CAPABILITY:
            return MutationResult(
                status="MUTATION_DENIED_NO_AUTHORITY_CAPABILITY",
                encounter_id=note.encounter_id,
            )

        self.records[note.encounter_id] = note.text
        return MutationResult(status="EPR_MUTATION_FORMED", encounter_id=note.encounter_id)


def governed_commit(epr: RepresentedEPR, note: ClinicalNote, runtime_decision: str) -> MutationResult:
    """Represented governed commit path.

    Only an ALLOW determination resolves the in-process capability consumed at the
    represented EPR mutation boundary. ESCALATE/REFUSE do not receive that capability.
    """
    if runtime_decision != "ALLOW":
        return MutationResult(status="MUTATION_DENIED_RUNTIME_AUTHORITY", encounter_id=note.encounter_id)

    return epr.commit_note(note, authority_capability=_RESOLVED_AUTHORITY_CAPABILITY)
