# NHS Ambient Scribing Verification Harness (ASVH)

**An Open Engineering Reference Implementation for Runtime Verification of AI-Generated Clinical Documentation**

---

## Current Context – August 2026

On 6 August 2026, the **Health Services Safety Investigations Body (HSSIB)** announced a national patient safety investigation into the use of **Ambient Voice Technology (AVT)** within NHS hospitals.

The investigation highlights growing national interest in the safe operational use of AI-assisted clinical documentation, including how organisations assure patient safety when AI-generated records become part of the permanent **Electronic Patient Record (EPR)**.

The **Ambient Scribing Verification Harness (ASVH)** was developed prior to the HSSIB announcement and demonstrates one implementation-independent engineering approach to runtime verification immediately before AI-generated clinical documentation is committed to the EPR.

Rather than evaluating how an AI model generates clinical documentation, ASVH addresses a different engineering question:

> **Do the conditions and controls required for an AI-generated clinical record to be committed remain satisfied at the point of execution?**

An independent **Runtime Authority** evaluates those conditions immediately before commitment and determines whether execution remains admissible.

The project operationalises published NHS England guidance into deterministic **Runtime Rules**, evaluates those rules at runtime, and produces an evidential **Authority Receipt** recording the execution determination.

The HSSIB investigation is expected to report during 2027. ASVH does not anticipate its findings or propose regulatory recommendations. Instead, it provides an open engineering reference implementation intended to support discussion around runtime verification, evidential accountability and execution assurance for AI-enabled clinical documentation.

---

## Purpose

The NHS Ambient Scribing Verification Harness demonstrates how published operational guidance can be transformed into deterministic runtime controls and evaluated immediately before an AI-generated clinical record is committed.

ASVH provides an engineering reference for examining the boundary between:

**Governance → Runtime Authority → Execution**

The project is concerned specifically with the runtime determination that occurs immediately before consequence formation.

It does not attempt to determine whether an AI-generated clinical statement is medically correct. It determines whether the defined organisational conditions required for commitment remain satisfied.

---

## The Engineering Question

Traditional governance and clinical safety processes address important questions including:

- Was the system appropriately assessed?
- Was deployment authorised?
- Have hazards been identified?
- Are appropriate controls defined?
- Is human oversight required?

ASVH addresses an additional question that arises during operation:

> **Are those required conditions still satisfied for this execution, now?**

A control defined during deployment does not necessarily demonstrate that the conditions required for that control remain available or effective at a particular moment of execution.

Runtime verification therefore complements, rather than replaces, existing governance and clinical safety processes.

---

## What ASVH Demonstrates

ASVH demonstrates an end-to-end engineering lifecycle:

1. Published operational guidance is identified.
2. Narrative guidance is decomposed into engineering-relevant control statements.
3. Runtime conditions are separated from governance, evidence and out-of-scope requirements.
4. Runtime conditions are transformed into deterministic Runtime Rules.
5. Current operational evidence is assembled into a canonical runtime context.
6. An independent Runtime Authority evaluates the applicable Runtime Rules.
7. A deterministic runtime determination is produced.
8. An Authority Receipt records the determination and supporting evidence.
9. Only then may execution proceed to consequence formation.

The reference implementation therefore creates a traceable path from:

```text
Published Guidance
        │
        ▼
Guidance Decomposition
        │
        ▼
Runtime Conditions
        │
        ▼
Deterministic Runtime Rules
        │
        ▼
Canonical Runtime Context
        │
        ▼
Independent Runtime Authority
        │
        ▼
Execution Bind Point
        │
        ▼
ALLOW / ESCALATE / REFUSE
        │
        ▼
Authority Receipt
        │
        ▼
Clinical Record Commitment
```

---

## Runtime Authority

Within ASVH, **Runtime Authority** is architecturally separate from both the AI system generating the clinical documentation and the system responsible for executing the resulting action.

Its role is deliberately narrow.

It determines whether the organisational authority required for a proposed execution remains exercisable under the current runtime conditions.

The Runtime Authority does not:

- generate clinical documentation
- diagnose patients
- determine clinical truth
- replace clinician judgement
- establish organisational policy
- establish clinical safety requirements

It evaluates deterministic Runtime Rules derived from those requirements.

---

## Execution Bind Point

The **Execution Bind Point** is the point immediately before an execution would create institutional consequence.

For the ASVH reference workflow, that consequence is the commitment of AI-generated clinical documentation to the Electronic Patient Record.

The Runtime Authority is invoked at this boundary.

This is deliberately later than procurement, deployment approval or model generation.

The question being evaluated is not simply:

> **Was this system authorised?**

It is:

> **Is this specific execution still admissible under the current conditions?**

---

## Deterministic Outcomes

The Runtime Authority produces one of three deterministic outcomes:

### ALLOW

The required runtime conditions are satisfied and execution may proceed.

### ESCALATE

Execution cannot be independently authorised from the available runtime evidence and requires an authorised escalation path.

### REFUSE

The required conditions for execution are not satisfied and execution must not proceed.

Insufficient evidence is itself treated as an explicit runtime condition rather than silently interpreted as permission.

---

## Authority Receipts

Every runtime determination produces an **Authority Receipt**.

The Authority Receipt provides an evidential record of the determination immediately preceding consequence formation.

Depending on the implementation, the receipt may preserve information including:

- applicable Runtime Rules
- runtime context
- evidence references
- determination
- reason codes
- timestamps
- execution identifiers
- policy or rule versions

This allows the execution decision to be reconstructed and examined independently of the AI system that generated the original clinical documentation.

---

## Relationship to NHS England Guidance

ASVH was developed from published NHS England guidance concerning the use of AI-enabled ambient scribing products in health and care settings.

The methodology does not treat every statement in the guidance as a runtime control.

Guidance statements are decomposed into four categories:

| Classification | Meaning |
|---|---|
| **Governance** | Requirements applying primarily to organisational governance, deployment or oversight |
| **Runtime Condition** | Conditions capable of affecting whether execution should proceed at runtime |
| **Evidence** | Information that should be preserved to support accountability and reconstruction |
| **Out of Scope** | Requirements outside the Runtime Authority boundary |

Only appropriate **Runtime Conditions** become candidates for deterministic Runtime Rules.

This separation is fundamental to the ASVH methodology.

---

## Scope and Limitations

ASVH is an engineering reference implementation.

It is **not**:

- a medical device
- a clinical decision support system
- an ambient scribing product
- a diagnostic system
- a replacement for clinician review
- a replacement for DCB0129
- a replacement for DCB0160
- a replacement for NHS England guidance
- regulatory guidance
- a certification mechanism
- evidence that any particular AVT product is safe

The reference implementation demonstrates an architectural and engineering method.

Individual NHS organisations remain responsible for their own governance, clinical safety, deployment and operational decisions.

---

## Reference Publications

The ASVH project is supported by a set of companion engineering publications.

| Publication | Purpose |
|---|---|
| **ASVH-METH-001** | Engineering methodology for transforming operational guidance into deterministic runtime controls |
| **ASVH-SPEC-001** | Runtime Rule specification |
| **ASVH-TRACE-001** | Traceability between source guidance, runtime conditions, Runtime Rules and execution evidence |
| **ASVH-ARCH-001** | Reference architecture |
| **ASVH-001** | Reference implementation |
| **VERIFY-001** | Implementation and verification evidence |

Together, these artefacts separate methodology, specification, traceability, architecture and implementation evidence.

---

## Current Patient Safety Context

The HSSIB investigation into Ambient Voice Technology creates an important opportunity to examine not only how these systems are assessed before deployment, but how safety controls operate during real clinical workflows.

ASVH does not attempt to predict the investigation's findings.

It contributes a narrower engineering proposition:

> **Where execution depends upon defined organisational conditions and controls, those conditions can be evaluated deterministically immediately before execution and the resulting determination can be preserved as evidence.**

This allows runtime verification to complement existing clinical safety, governance and incident investigation mechanisms.

---

## Open Engineering Reference

ASVH is published as an open engineering reference implementation to encourage technical examination, challenge and interoperability.

The objective is not to prescribe a particular commercial implementation.

It is to make the engineering method inspectable.

Developers, NHS organisations, clinical safety professionals, researchers, AI suppliers and governance specialists are encouraged to examine the architecture, Runtime Rules, traceability model and implementation evidence.

Constructive technical challenge is welcome.

---

## Related Analysis

A companion insight note is being developed:

**ASVH-IN-001 — HSSIB's Investigation into Ambient Voice Technology: Why Runtime Verification Matters**

The note examines the emerging patient-safety discussion from a runtime engineering perspective and considers the distinction between deployment assurance and verification immediately before execution.

---

## Status

ASVH is an evolving engineering reference implementation.

The repository and associated publications should be interpreted as technical research and implementation evidence rather than clinical, legal or regulatory advice.

Changes to the reference implementation will be documented as the engineering model develops.

---

## About FlowSignal

ASVH is developed as part of the wider **FlowSignal™** work on independent Runtime Authority and runtime admissibility.

FlowSignal explores the architectural boundary between approved decision-making and institutional execution: the point at which an organisation must determine whether delegated authority remains exercisable immediately before consequence formation.

ASVH applies that engineering model to a representative NHS ambient scribing workflow.

---

## Disclaimer

This repository is provided for engineering research, technical discussion and interoperability purposes.

Nothing within ASVH constitutes medical, clinical, regulatory or legal advice.

References to NHS England guidance, HSSIB, DCB0129, DCB0160 or other external standards and organisations do not imply endorsement of ASVH or FlowSignal by those organisations.

---

**FlowSignal™**

**Independent Runtime Authority**

*Execute with Authority. Defend with Evidence.*
