# AT-EPR-001 — Initial Direct Mutation Failure

**Classification:** FAIL — DIRECT CONSEQUENCE BYPASS DEMONSTRATED  
**GitHub Actions run:** `32106291936`  
**First runnable head:** `125711a6751bbc873e8cab35f99e40fd1f8dd376`

## Frozen proposition

An actor without a valid resolved Runtime Authority capability MUST NOT be able to form the represented protected EPR mutation.

## Attack exercised

The adversarial test bypassed the represented Runtime Rules / Runtime Authority path and invoked the represented EPR consequence directly:

```python
result = epr.commit_note(note)
```

No Runtime Authority determination, Authority Receipt, resolved execution capability or governed commit function was used.

## Observed result

The represented mutation returned:

`EPR_MUTATION_FORMED`

and the note was written to the represented EPR record store.

The frozen test required:

`MUTATION_DENIED_NO_AUTHORITY_CAPABILITY`

GitHub Actions recorded:

`1 failed in 0.02s`

with the assertion differential:

`EPR_MUTATION_FORMED` vs `MUTATION_DENIED_NO_AUTHORITY_CAPABILITY`.

## Engineering conclusion

The first runnable ASVH consequence surface did not demonstrate route closure. Direct consequence invocation remained reachable without a resolved Runtime Authority capability.

This is a genuine mechanism failure on the represented public demo boundary, not a test-construction failure.

## Scope

The failure concerns only the represented ASVH EPR mutation surface created for AT-EPR-001. It is not evidence about any live NHS EPR, Trust IAM configuration or production clinical system.

The frozen proposition and test are retained for post-remediation rerun.