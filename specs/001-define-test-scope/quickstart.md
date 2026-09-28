# Quickstart: Validate the Evidence-Bounded Test Scope

## Prerequisites

- Access to this feature's [specification](spec.md), [research decisions](research.md), and [conceptual data model](data-model.md).
- Access to the authorized legacy reading under `../../old/docs/`.
- No Java runtime, Go runtime, source checkout, dependency, fixture, or test harness is required or selected.

## Validation scenario: review the current candidate

1. Open `../../old/docs/overview.md` and confirm its literal reported inventory: `Inventory items: 0`, `components | 0`, `behaviours | 0`, and `rules | 0`.
2. Confirm that `overview.md` also says `This is a missing reading, NOT an estate with nothing in it.`
3. Read [research.md](research.md) and confirm that Decisions 1–3 preserve this limitation and select no legacy runtime behavior, storage, interface, or test framework.
4. Read [data-model.md](data-model.md) and confirm that the current Test Scope has `0` approved behavior-specific Java-to-Go equivalence tests.
5. Confirm that no Java or Go test command, source layout, API contract, behavior contract, or equivalence result is claimed anywhere in this feature.

**Expected outcome**: The candidate is reviewable as a documentation-only scope boundary. It does not equate unavailable evidence with absent legacy behavior and does not approve a behavior-specific Java-to-Go test.

## Validation scenario: assess a proposed future test

1. Record the proposed test as a Behavioral Claim using the fields and validation rules in [data-model.md](data-model.md).
2. Verify that it cites authorized evidence and includes a Java entry point, observable inputs, observable outcome (output, state change, or error outcome), and executable acceptance criterion.
3. If any item is missing, leave the claim outside scope. If all items are present, submit it for a later specification revision; this candidate still does not approve it automatically.

**Expected outcome**: Missing evidence prevents a behavior-specific test from entering scope without inventing behavior.
