# AT-EPR-001 — Direct EPR Mutation Bypass Result

**Final classification:** PASS — represented in-process EPR mutation boundary  
**External/live EPR route closure:** NOT DEMONSTRATED  
**Post-remediation GitHub Actions run:** `32106441519`

## Proposition

An actor without a valid resolved Runtime Authority capability MUST NOT be able to form the represented protected EPR mutation.

## Initial result

The first runnable implementation exposed the represented mutation directly. The frozen adversarial test bypassed the governed Runtime Authority path and invoked `commit_note()` without resolved capability.

GitHub Actions run `32106291936` failed with:

`EPR_MUTATION_FORMED`

instead of:

`MUTATION_DENIED_NO_AUTHORITY_CAPABILITY`

Classification:

**FAIL — DIRECT CONSEQUENCE BYPASS DEMONSTRATED**

The failure is preserved separately in `AT-EPR-001_INITIAL_FAILURE.md`.

## Remediation

The represented EPR mutation boundary was strengthened so that consequence formation requires an opaque in-process capability resolved only by the represented governed ALLOW path.

Direct invocation without that capability returns:

`MUTATION_DENIED_NO_AUTHORITY_CAPABILITY`

and does not write the note into the represented record store.

The frozen adversarial test itself was not weakened or changed.

## Rerun

GitHub Actions run `32106441519` reran the frozen direct-mutation challenge after remediation.

Result:

**PASS**

The direct bypass path no longer formed the represented EPR consequence under the exercised condition.

## Demonstrated scope

AT-EPR-001 now demonstrates, on the public ASVH reference-demonstrator boundary exercised by this test, that direct represented EPR mutation without the resolved in-process Runtime Authority capability is denied.

This is evidence of route closure for the specific represented direct-invocation path tested.

## Residual limitations

AT-EPR-001 does NOT demonstrate:

- route closure inside Epic, Oracle Health/Cerner, EMIS, TPP or another live EPR;
- NHS Trust IAM, administrator or service-account isolation;
- production process/KMS/HSM capability isolation;
- prevention of direct database or vendor API mutation outside the represented adapter;
- distributed atomicity across clinical systems;
- universal physical non-formation in infrastructure not represented by this repository.

The in-process capability is a reference-demonstrator control, not a production security boundary.

## Evidence lineage

`frozen external proposition -> minimum falsifiable consequence surface -> genuine FAIL -> preserved failure -> boundary strengthening -> unchanged challenge rerun -> bounded PASS`
