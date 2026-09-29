<!--
Sync Impact Report
Version change: none → 1.0.0
Modified principles: none (initial adoption)
Added sections: Core Principles; Evidence Boundaries; Required Workflow; Governance
Removed sections: none

-->
# Legacy Estate Reconstruction Constitution

## Core Principles

### I. Evidence-Bounded Claims
Every statement about the legacy estate's behavior, rules, symbols, interfaces, or data MUST be
grounded in the frozen artifacts under `../../old/docs/` or in artifacts produced earlier in this
workspace. Identifiers and rule evidence MUST be quoted verbatim from their source. Work MUST NOT
claim, implement, or test behavior that the available evidence does not contain. This preserves a
rebuild's fidelity when the source reading is incomplete.

### II. Spec-First Delivery
Each scoped change MUST proceed in order through specification, plan, tasks, and implementation.
An implementation task MUST cite the governing specification and the evidence that makes the task
actionable. A missing behavior or acceptance criterion MUST be recorded as a clarification marker,
not resolved through inference. This makes each decision reviewable before code changes begin.

### III. Workspace and Source Containment
Work in this unit MUST use `../../old/docs/` and artifacts already written in this workspace as its
subject matter. It MUST NOT treat the surrounding repository, unrelated code, or an intended target
language as evidence of the legacy estate. Changes MUST remain inside this working tree unless an
explicitly authorized task expands that boundary. This prevents accidental substitution of context
for evidence.

### IV. Observable Characterization Before Translation
Any Java-to-Go reconstruction scope MUST define observable inputs, outputs, state changes, and error
outcomes before its Go implementation is accepted as behaviorally equivalent. Characterization tests
MUST trace each asserted behavior to a documented source or specification decision. Where no
observable behavior has been extracted, the work MUST stop at discovery and clarification rather
than create speculative parity tests. This makes test results meaningful rather than self-confirming.

### V. Reproducible, Reviewable Artifacts
Specifications, plans, tasks, and tests MUST identify their assumptions, evidence limitations, and
acceptance conditions. Generated or derived artifacts MUST be deterministic from their declared
inputs where tooling permits; otherwise, the source inputs and nondeterministic factors MUST be
recorded. Reviews MUST reject unsupported behavioral claims and missing traceability. This supports
independent verification of the reconstruction.

## Evidence Boundaries

The declared source language is Java and the intended target language is Go. This context describes
the vocabulary of the work but does not establish any behavior to preserve. The current Discover
artifacts report zero inventory items, components, behaviors, and verified rules; the absence of a
description is not evidence that the estate has no behavior.



## Required Workflow

Before creating or amending project artifacts, contributors MUST read `../../old/docs/README.md`.
They MUST use the legacy documentation to establish only evidenced scope, then produce or update a
feature specification, implementation plan, and dependency-ordered task list before implementation.
Each review MUST verify that proposed behavior has an evidence citation or a clearly marked
specification decision, and that unresolved scope remains visible as a clarification marker.

## Governance

This constitution governs all work in this workspace and supersedes conflicting local practices.
An amendment MUST document the changed principle or section, its rationale, and its semantic version
bump in the Sync Impact Report. Removing or redefining an existing governance rule requires a MAJOR
version increase; adding a principle or materially expanding guidance requires a MINOR increase;
clarifications and non-semantic editorial changes require a PATCH increase. Every specification,
plan, task list, implementation review, and test review MUST check compliance with these principles.

**Version**: 1.0.0 | **Ratified**: 2026-09-28 | **Last Amended**: 2026-09-28
