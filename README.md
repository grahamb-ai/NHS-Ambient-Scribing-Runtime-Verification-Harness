# ASVH-001

# NHS Ambient Scribing Runtime Verification Harness

### Engineering deterministic runtime verification for AI-enabled ambient scribing

---

> **Engineering Reference Project**
>
> ASVH demonstrates one implementation-independent approach to deterministic runtime verification for AI-enabled ambient scribing. It is intended to stimulate architectural discussion and does not represent NHS England guidance or policy.

---

## Overview

The **NHS Ambient Scribing Runtime Verification Harness (ASVH)** is an implementation-independent engineering reference demonstrating how NHS England guidance for AI-enabled ambient scribing can be transformed into deterministic runtime verification immediately before clinical documentation is committed to the Electronic Patient Record (EPR).

The project does **not** implement an ambient scribing platform.

Instead, it demonstrates how an independent Runtime Authority can evaluate whether delegated authority remains legitimately exercisable immediately before institutional consequence formation.

ASVH has been developed as a reference implementation for healthcare architects, NHS organisations, clinical safety teams, digital transformation leaders and ambient scribing suppliers interested in execution-time assurance.

---

# Why ASVH?

NHS England's guidance clearly establishes governance expectations for the safe deployment of AI-enabled ambient scribing.

These include requirements relating to:

- Clinical Safety
- Governance
- Human Review
- Clinical Approval
- Organisational Responsibility
- Safe Deployment

ASVH explores a complementary engineering question:

> **How can an NHS organisation deterministically verify, immediately before AI-generated documentation is committed to the EPR, that execution should still proceed?**

The project demonstrates one implementation-independent engineering approach to answering that question.

---

# Architectural Position

ASVH is **not**:

- An ambient scribing product
- A governance framework
- A clinical decision support system
- An Electronic Patient Record
- A replacement for clinician judgement

Instead, ASVH demonstrates an independent **Runtime Authority** operating at the **Execution Bind Point** immediately before consequence formation.

```text
Ambient Scribing Platform
            │
            ▼
AI Generated Clinical Documentation
            │
            ▼
     Clinician Review
            │
            ▼
    Clinician Approval
            │
            ▼
══════════════════════════════════════
      Execution Bind Point
 Independent Runtime Authority
══════════════════════════════════════
            │
            ▼
     ALLOW
   ESCALATE
    REFUSE
            │
            ▼
 Commit Documentation to the EPR
```

---

# Repository Contents

This repository contains the engineering artefacts supporting the ASVH reference project.

| Document | Description |
|-----------|-------------|
| **ASVH-METH-001** | Runtime Requirements Engineering Methodology |
| **ASVH-SPEC-001** | Runtime Authority Specification |
| **ASVH-TRACE-001** | Guidance-to-Implementation Traceability |
| **ASVH-ARCH-001** | Reference Architecture |
| **Sample Authority Receipts** | Example runtime evidence outputs |
| **Example Runtime Decisions** | Sample deterministic evaluations |

---

# Engineering Principles

ASVH has been engineered around the following principles:

- Implementation Independence
- Deterministic Runtime Evaluation
- Independent Runtime Authority
- Guidance-Derived Engineering
- Complete Traceability
- Explainable Execution Decisions
- Evidential Accountability
- Separation of Governance from Runtime Execution

---

# Runtime Authority

Within ASVH, the Runtime Authority is responsible for determining whether delegated authority remains legitimately exercisable immediately before documentation is committed to the Electronic Patient Record.

Runtime Authority **does not replace**:

- Governance
- Clinical Judgement
- Organisational Approval
- Human Review
- Existing Ambient Scribing Platforms

Instead, it evaluates the current runtime context to determine whether execution remains admissible.

Possible outcomes are:

| Decision | Meaning |
|-----------|---------|
| **ALLOW** | Runtime conditions remain satisfied and execution may proceed. |
| **ESCALATE** | Runtime conditions require authorised human intervention before execution. |
| **REFUSE** | Execution is not currently admissible and must not proceed. |

---

# Engineering Lifecycle

ASVH follows a deterministic engineering lifecycle:

```text
NHS England Guidance
            │
            ▼
Guidance Decomposition
            │
            ▼
Runtime Requirements
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
```

Every runtime decision is traceable back to documented engineering requirements derived from published guidance.

---

# Intended Audience

ASVH has been developed for:

- NHS Trusts
- Ambient Scribing Suppliers
- Clinical Safety Officers
- CNIOs
- CCIOs
- Chief Digital Information Officers
- Enterprise Architects
- Healthcare AI Researchers
- AI Governance Professionals
- Digital Transformation Leaders

---

# Project Status

Current public release includes:

- ✅ Runtime Requirements Engineering Methodology
- ✅ Runtime Authority Specification
- ✅ Guidance-to-Implementation Traceability
- ✅ Reference Architecture
- ✅ Representative Runtime Evidence
- ✅ Sample Runtime Decisions

The reference implementation continues to evolve as additional healthcare scenarios and runtime rules are evaluated.

---

# Relationship to NHS England Guidance

ASVH is an engineering reference project inspired by publicly available NHS England guidance for AI-enabled ambient scribing.

It should not be interpreted as NHS England policy, certification or endorsement.

The project demonstrates one possible implementation-independent approach to engineering deterministic runtime verification within healthcare AI workflows.

---

# Contributing

Constructive feedback from:

- NHS Organisations
- Ambient Scribing Suppliers
- Clinical Safety Professionals
- Healthcare Architects
- Researchers

is welcomed.

If your organisation is deploying AI-enabled ambient scribing and would like to discuss the engineering approach demonstrated by ASVH, please get in touch.

---

# Related FlowSignal Projects

- **ORAI** — Open Runtime Authority Interface
- **IRAI** — Independent Runtime Authority Infrastructure
- **FlowSignal Runtime Authority**
- **Execution Bind Point Architecture**

---

# Licence

**© FlowSignal™**

This repository is published as an engineering reference project for architectural review, discussion and research.

See the accompanying licence for usage terms.

---

## Citation

If referencing this work, please cite:

> **ASVH-001 — NHS Ambient Scribing Runtime Verification Harness**  
> FlowSignal™ Engineering Reference Project  
> Version 1.0

---

**FlowSignal™**

*Independent Runtime Authority for AI Execution.*
