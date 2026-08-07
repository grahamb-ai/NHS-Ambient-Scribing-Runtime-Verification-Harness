# NHS Ambient Scribing Verification Harness (ASVH)

**An Open Engineering Reference Implementation for Runtime Verification of AI-Generated Clinical Documentation**

---

## Current Context – August 2026

On **6 August 2026**, the **Health Services Safety Investigation Body (HSSIB)** announced a national patient safety investigation into the use of **Ambient Voice Technology (AVT)** within NHS hospitals.

The investigation highlights growing national interest in the safe operational use of AI-assisted clinical documentation, including how organisations assure patient safety when AI-generated records become part of the permanent Electronic Patient Record (EPR).

The Ambient Scribing Verification Harness (ASVH) was developed prior to the HSSIB announcement and demonstrates one implementation-independent engineering approach to runtime verification immediately before AI-generated clinical documentation is committed to the Electronic Patient Record (EPR).

Rather than evaluating how an AI model generates clinical documentation, ASVH demonstrates how an independent **Runtime Authority** can determine whether an AI-generated clinical record remains admissible for commitment immediately before execution.

The project operationalises published NHS England guidance into deterministic Runtime Rules, evaluates those rules at runtime, and produces an evidential **Authority Receipt** recording the execution decision.

The HSSIB investigation is expected to conclude during 2027. ASVH does not anticipate its findings or propose regulatory recommendations. Instead, it provides an open engineering reference implementation intended to support discussion around runtime verification, evidential accountability and execution assurance for AI-enabled clinical documentation.

---

# Purpose

ASVH demonstrates how published operational guidance can be transformed into deterministic runtime controls.

The project provides an implementation-independent engineering reference showing how runtime verification can complement existing governance, assurance and clinical safety processes.

It is intended to support discussion around:

- Runtime verification
- Execution assurance
- Evidential accountability
- AI-enabled clinical documentation
- Safe commitment of AI-generated records

---

# What ASVH Demonstrates

The project demonstrates:

- Decomposition of NHS England guidance into Runtime Rules
- Deterministic runtime policy evaluation
- Independent Runtime Authority
- Runtime admissibility assessment
- Execution Bind Point evaluation
- Authority Receipt generation
- Complete evidential traceability
- Deterministic execution outcomes

The implementation intentionally focuses on runtime behaviour rather than AI model performance.

---

# Engineering Philosophy

Traditional governance answers questions such as:

- Was the system approved?
- Was it clinically assessed?
- Was deployment authorised?

ASVH demonstrates an additional runtime question:

> **Should this AI-generated clinical record still be committed now?**

This determination occurs immediately before consequence formation.

The Runtime Authority evaluates current operational evidence and determines whether organisational authority remains sufficient for execution to proceed.

---

# Scope

ASVH does **not**:

- Perform clinical decision making
- Diagnose patients
- Assess AI model quality
- Replace clinical judgement
- Replace DCB0129 or DCB0160
- Replace NHS England guidance

Instead, it demonstrates how runtime verification may complement these existing governance processes.

---

# Architecture

The reference implementation demonstrates:

```
NHS Guidance
        │
        ▼
Guidance Decomposition
        │
        ▼
Runtime Rules
        │
        ▼
Runtime Authority
        │
        ▼
Execution Bind Point
        │
        ▼
Authority Receipt
        │
        ▼
Electronic Patient Record
```

---

# Repository Contents

| Document | Purpose |
|----------|---------|
| ASVH-METH-001 | Engineering methodology |
| ASVH-SPEC-001 | Runtime Rule specification |
| ASVH-TRACE-001 | Traceability matrix |
| ASVH-ARCH-001 | Reference architecture |
| ASVH-001 | Reference implementation |
| VERIFY-001 | Implementation verification report |

---

# Current Relevance

The HSSIB investigation reflects an important industry shift.

The conversation is moving beyond:

> **Can AI generate clinical documentation?**

towards:

> **How can organisations demonstrate that AI-generated documentation remained safe and admissible at the moment it became part of the clinical record?**

ASVH contributes to this discussion by demonstrating one possible runtime engineering approach.

---

# Relationship to NHS Guidance

ASVH is derived from published NHS England operational guidance.

The project:

- extracts runtime conditions
- converts narrative guidance into deterministic Runtime Rules
- evaluates those rules immediately before execution
- records evidential proof of the runtime decision

This work does not reinterpret NHS policy.

It demonstrates one possible engineering implementation.

---

# Open Engineering Reference

ASVH is published as an open engineering reference implementation.

Its purpose is to encourage discussion around:

- runtime verification
- evidential accountability
- implementation patterns
- interoperable runtime architectures
- patient safety

The project is implementation-independent and intended to complement existing NHS governance frameworks.

---

# Future Publications

Companion publications include:

- ASVH-METH-001
- ASVH-SPEC-001
- ASVH-TRACE-001
- ASVH-ARCH-001
- VERIFY-001

Planned publications:

- **ASVH Insight Note 001 – HSSIB's Investigation into Ambient Voice Technology: Why Runtime Verification Matters**

---

# Contributing

Technical discussion and constructive feedback are welcome.

The objective of ASVH is to encourage open engineering discussion around runtime assurance for AI-enabled clinical documentation.

---

# Licence

This repository is published for research, engineering discussion and interoperability.

It is not a clinical product and should not be interpreted as clinical or regulatory guidance.

---

**FlowSignal™**

*Independent Runtime Authority for AI Execution*

**Execute with Authority. Defend with Evidence.**
