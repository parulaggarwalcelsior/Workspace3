# Quickstart: Validate the Evidence-Bounded Test Scope

## Prerequisites

- Access to this feature's [specification](spec.md), [research decisions](research.md), and [conceptual data model](data-model.md).
- Access to the authorized legacy reading under `../../old/docs/`.
- No Java runtime, Go runtime, source checkout, dependency, fixture, or test harness is required or selected.

## Manual evidence-review procedure

1. Open `../../old/docs/overview.md` and record its literal inventory: `**Inventory items**: 0`, `| components | 0 |`, `| behaviours | 0 |`, and `| rules | 0 |`. Record with it the verbatim limitation: `This is a missing reading, NOT an estate with nothing in it.` Do not turn either the counts or that limitation into a claim that the estate has no behaviour.
2. Open `../../old/docs/data_model.md` and record this observation verbatim: `**UNAVAILABLE** — This estate was read by an instrument with no view of persistence, so no table or field was recorded. That is a limit of the reading, not a finding about the system: it does not mean the estate stores nothing.` Do not treat it as evidence that the estate lacks persistence.
3. Open `../../old/docs/api_surface.md` and record this observation verbatim: `**UNAVAILABLE** — No endpoint was recorded for this estate. Either it exposes none — a batch or library estate does not — or the instrument that read it does not recognise this stack's routing.` Do not select either alternative as a fact about the estate.
4. Review each statement about the legacy estate in the candidate. For every statement, record the source path under `../../old/docs/` and its exact supporting observation. Mark a statement with no such path and verbatim observation as unsupported; do not use it to define test scope.
5. Review the candidate's Test Scope in [data-model.md](data-model.md). Confirm that its approved behavior-specific Java-to-Go equivalence-test count is `0` and that its decision distinguishes missing readings from absent legacy behaviour.
6. Within five minutes, identify for a reviewer: the three evidence limitations above, the excluded behavior-specific test scope, and the recorded zero-test decision. Then determine whether a proposed test presents cited observable inputs and an outcome; a zero count or an unavailable reading alone is not negative evidence.

## Expected outcomes

- Every legacy-estate statement retained by the review names an authorized document and quotes its supporting observation.
- The review approves `0` behavior-specific Java-to-Go equivalence tests.
- A reviewer can locate the evidence limitation, excluded scope, and recorded decision within five minutes.
- A reviewer can distinguish a reading limitation from negative evidence and decide whether a proposed test has cited observable inputs and an outcome without inventing behaviour.

## Review boundary

This procedure records only what the authorized reading reports. It creates no Java or Go test, behavior contract, API contract, source layout, or equivalence result.
