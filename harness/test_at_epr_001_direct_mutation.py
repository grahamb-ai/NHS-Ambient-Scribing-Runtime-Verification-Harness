from epr_mutation import ClinicalNote, RepresentedEPR


def test_direct_epr_mutation_requires_resolved_runtime_authority_capability():
    """Frozen AT-EPR-001 proposition.

    Bypass deterministic Runtime Rules, Runtime Authority determination and the
    governed commit path, then invoke the represented EPR consequence directly.
    The required property is that the represented consequence cannot form without
    resolved Runtime Authority capability.
    """
    epr = RepresentedEPR()
    note = ClinicalNote(encounter_id="enc-001", text="AI generated clinical note")

    result = epr.commit_note(note)

    assert result.status == "MUTATION_DENIED_NO_AUTHORITY_CAPABILITY"
    assert note.encounter_id not in epr.records
