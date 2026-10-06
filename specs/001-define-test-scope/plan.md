# Implementation Plan: Define Evidence-Bounded Test Scope

**Branch**: `001-define-test-scope` | **Date**: 2026-09-28 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/001-define-test-scope/spec.md`

## Summary

Create the documentation artifacts that let a reviewer determine whether a proposed Java-to-Go behavior-specific test has sufficient evidence to enter scope. The candidate records the available reading as a missing reading, not proof that the estate has no behavior; it therefore approves `0` behavior-specific Java-to-Go equivalence tests. No Java or Go runtime, source layout, test framework, executable test, or behavior contract is selected.

## Technical Context

**Language/Version**: Documentation artifacts are Markdown. The legacy reading records `java`; no Java or Go version is recorded.

**Primary Dependencies**: None. The candidate is reviewed against the frozen files in `../../old/docs/`; no software dependency or integration is selected.

**Storage**: N/A for the candidate. `data_model.md` says no table or field was recorded and that this `does not mean the estate stores nothing`.

**Testing**: Manual review using [quickstart.md](quickstart.md). No behavior-specific Java or Go test framework, harness, fixture, or parity oracle is selected because the reading contains no observable behavior.

**Target Platform**: Markdown-capable review environment. No legacy execution or deployment platform is recorded.

**Project Type**: Documentation-only evidence-scope candidate. The legacy project type is not determined: [api_surface.md](../../old/docs/api_surface.md) states that no endpoint being recorded may mean either none exists or that the instrument does not recognize the routing stack.

**Performance Goals**: None for this documentation candidate. No legacy performance criterion is recorded.

**Constraints**: Claims about the legacy estate must cite `../../old/docs/` or an earlier workspace artifact and preserve quoted evidence. A behavior-specific claim needs a cited observable entry point, input, outcome, state change, or error outcome before it can be approved.

**Scale/Scope**: One reviewable scope candidate; `0` approved behavior-specific Java-to-Go equivalence tests. The reading reports `Inventory items: 0`, `components | 0`, `behaviours | 0`, and `rules | 0`; these are limits of the reading, not absence claims about the estate.

## Documentation-Only Reconciliation

The feature structure is limited to the Markdown review artifacts listed below. The legacy [data model reading](../../old/docs/data_model.md) records `**UNAVAILABLE**` and says: `This estate was read by an instrument with no view of persistence, so no table or field was recorded. That is a limit of the reading, not a finding about the system: it does not mean the estate stores nothing.` The legacy [API-surface reading](../../old/docs/api_surface.md) likewise records `**UNAVAILABLE**` and says: `No endpoint was recorded for this estate. Either it exposes none — a batch or library estate does not — or the instrument that read it does not recognise this stack's routing.`

Accordingly, the candidate selects no Java or Go runtime, source layout, test framework, harness, fixture, contract, or machine-consumable interface. The `java` language label in the readings is context only; it does not provide a runtime or source-tree selection. The unavailable readings do not establish that persistence or endpoints are absent, so they cannot justify a storage choice, an API contract, or any other implementation structure. `contracts/` remains absent because this documentation-only candidate defines no API, CLI, grammar, behavior, or equivalence contract.

## Constitution Check

### Pre-Phase 0

| Principle | Result | Evidence / disposition |
|---|---|---|
| I. Evidence-Bounded Claims | PASS | All legacy observations are limited to the quoted material in the feature specification and [research.md](research.md); the plan selects no undocumented runtime behavior. |
| II. Spec-First Delivery | PASS | The feature specification precedes this plan. The plan creates only research and design artifacts; task generation and implementation are later workflow stages. |
| III. Workspace and Source Containment | PASS | Subject evidence comes only from `../../old/docs/` and current feature artifacts; every planned artifact stays under `specs/001-define-test-scope/`. |
| IV. Observable Characterization Before Translation | PASS | No Java-to-Go implementation or characterization test is designed. The plan requires an observable behavior before such work may be scoped. |
| V. Reproducible, Reviewable Artifacts | PASS | The artifacts name their source documents, record their evidence limits, and give a deterministic manual review procedure. |

**Gate result: PASS.** The feature is a documentation-only boundary decision, not a claim of behavioral equivalence.

### Post-Phase 1

| Principle | Result | Evidence / disposition |
|---|---|---|
| I. Evidence-Bounded Claims | PASS | [research.md](research.md), [data-model.md](data-model.md), and [quickstart.md](quickstart.md) distinguish unavailable observations from negative findings and add no Java behavior. |
| II. Spec-First Delivery | PASS | Phase 0 and Phase 1 artifacts derive from [spec.md](spec.md); no implementation work is included. |
| III. Workspace and Source Containment | PASS | Generated artifacts are inside this feature directory and cite only authorized evidence. |
| IV. Observable Characterization Before Translation | PASS | The validation guide permits only review of the scope boundary; it defines no Java or Go behavior test. |
| V. Reproducible, Reviewable Artifacts | PASS | Evidence, decision rule, and validation steps are recorded explicitly. |

**Gate result: PASS.** No complexity exception is required.

## Project Structure

### Documentation (this feature)

```text
specs/001-define-test-scope/
├── plan.md              # This planning record
├── research.md          # Phase 0 evidence decisions
├── data-model.md        # Phase 1 conceptual review entities
├── quickstart.md        # Phase 1 manual validation guide
└── tasks.md             # Created later by /speckit-tasks; not generated here
```

`contracts/` is intentionally absent. No external interface is evidenced: [api_surface.md](../../old/docs/api_surface.md) is marked `**UNAVAILABLE**`; this documentation candidate exposes no API, CLI, grammar, or other machine-consumable interface.

### Source Code

```text
# No source layout is selected.
# This feature produces documentation only and does not authorize Java or Go implementation.
```

**Structure Decision**: Keep all artifacts under `specs/001-define-test-scope/`. A Java or Go source tree would be an unsupported implementation decision because the reading identifies no behavior-specific work.
