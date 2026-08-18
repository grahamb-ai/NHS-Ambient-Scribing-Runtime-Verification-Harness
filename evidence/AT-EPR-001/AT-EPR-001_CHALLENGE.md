# AT-EPR-001 — Direct EPR Mutation Bypass Challenge

**Status:** FROZEN CHALLENGE — PRE-IMPLEMENTATION  
**Date:** 17 August 2026

## External proposition

The challenge is to attempt to bypass the Runtime Rules / Runtime Authority path and invoke the protected EPR mutation directly.

The decisive question is whether the same actor that proposes or handles the AI-generated clinical note can still cause the EPR mutation without first obtaining the resolved authority/capability required by the governed path.

## Required property

An actor without a valid resolved Runtime Authority capability MUST NOT be able to form the represented protected EPR mutation.

Equivalent failure condition:

> If direct invocation of the represented EPR mutation can succeed without the required resolved capability, route closure has not been demonstrated at that represented boundary.

## Current public proof surface

At the time this challenge is frozen, the public repository contains the ASVH documentation set and README but no executable EPR mutation surface, no represented EPR adapter, and no runnable bypass test.

Therefore the present classification is:

**ND — NOT DEMONSTRABLE ON THE CURRENT PUBLIC ASVH EXECUTION SURFACE**

This is not a PASS and not a FAIL. The required consequence surface does not yet exist in the public repository.

## Test construction rule

The implementation created for this challenge must make the proposition falsifiable rather than embedding the desired answer.

The first runnable version MUST preserve the ordinary architectural assumption being challenged. It MUST NOT pre-install a capability-isolation mechanism merely so the first test passes.

The sequence is:

1. create the minimum represented EPR mutation surface;
2. create the normal governed Runtime Authority path to that surface;
3. attempt to invoke the represented EPR mutation directly without resolved authority;
4. preserve the observed result before remediation;
5. if direct mutation succeeds, classify and preserve the failure;
6. strengthen the boundary only after the failure is recorded;
7. rerun the same bypass attempt;
8. classify only the surface actually demonstrated.

## Initial adversarial test

### Attack

Invoke the protected represented EPR mutation directly while bypassing:

- deterministic Runtime Rule evaluation;
- Runtime Authority determination;
- Authority Receipt / resolved capability acquisition; and
- the normal governed commit path.

### Expected secure outcome

`MUTATION_DENIED_NO_AUTHORITY_CAPABILITY`

### Failure outcome

`EPR_MUTATION_FORMED`

without a valid resolved authority capability.

If the failure outcome occurs, the classification is:

**FAIL — DIRECT CONSEQUENCE BYPASS DEMONSTRATED**

## Evidence to preserve

The evidence package for AT-EPR-001 will retain:

- this frozen proposition;
- the initial runnable mutation surface;
- the exact bypass test;
- first-run result;
- any failure trace;
- remediation diff;
- identical or semantically unchanged rerun;
- final bounded classification; and
- CI evidence where available.

## Claim boundary

Even if the represented mutation surface ultimately resists the bypass, AT-EPR-001 will not by itself establish:

- route closure inside Epic, Oracle Health/Cerner, EMIS, TPP or another live EPR;
- NHS Trust IAM or privileged-administrator route closure;
- production KMS/HSM/credential isolation;
- prevention of direct database mutation outside the represented adapter;
- distributed atomicity across independent clinical systems; or
- universal physical non-formation across systems not represented by this repository.

Any final PASS will therefore be explicitly bounded to the represented public harness mutation surface unless a real integration supplies a stronger proof surface.

## Engineering principle

`external proposition → frozen attack → observable failure/success → preserved evidence → remediation if required → rerun → bounded conclusion`
