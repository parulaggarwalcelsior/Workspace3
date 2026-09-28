# Feature Specification: Define Evidence-Bounded Test Scope

**Feature Branch**: `not created (no before_specify hook is configured)`

**Created**: 2026-09-28

**Status**: Draft — evidence-bounded documentation-only scope

**Input**: User description: "Build the candidate for run run-461d3f7167fb440d." The operator-declared goal is "test" for a Java-to-Go rebuild.

## Evidence Record and Limits

This candidate is constrained to the legacy documentation under `../../old/docs/`. It does not assert that the legacy estate has no behaviour; it records that the available reading has not identified behaviour that can be tested or translated.

- `overview.md` reports `**Inventory items**: 0`, `| components | 0 |`, `| behaviours | 0 |`, and `| rules | 0 |`, and says: `This is a missing reading, NOT an estate with nothing in it.`
- `prd.md` reports `_No enforced requirements were derived._`
- `data_model.md` reports `**UNAVAILABLE**` and says that this limitation `does not mean the estate stores nothing`. `api_surface.md` reports `**UNAVAILABLE**` and says: `No endpoint was recorded for this estate. Either it exposes none — a batch or library estate does not — or the instrument that read it does not recognise this stack's routing.`
- `security.md`, `edge_cases.md`, and `workflows.md` report `UnsafeEngagementIdError: engagement id is empty or a relative path segment; it must name one directory` rather than a completed search.

## Reviewer-Facing Scope Decision

- **Evidence limitation**: The current reading reports `**Inventory items**: 0`, `| components | 0 |`, `| behaviours | 0 |`, and `| rules | 0 |` in `overview.md`, which also says: `This is a missing reading, NOT an estate with nothing in it.` `prd.md` states `_No enforced requirements were derived._`, and `brd.md` records `**0 rule(s) across 0 business area(s).**`
- **Excluded behavior-specific scope**: No behavior-specific Java or Go test, compatibility claim, or equivalence result is in scope. The quoted reading limitation and the absent derived requirements and rules do not establish that the legacy estate has no behavior; they provide no source-grounded observable Java behavior for this candidate.
- **Recorded decision**: The behavior-specific test scope is empty, with `0` approved Java-to-Go equivalence tests, until a later revision records a cited Java entry point, observable inputs, an outcome, and an executable acceptance criterion.

## Clarifications

### Session 2026-09-28

- Q: Which source-grounded observable Java behavior, including its entry point, inputs, and expected outcome, should define the first behavior-specific test scope? → A: None is identified in the authorized evidence; the first behavior-specific test scope is empty, with 0 approved Java-to-Go equivalence tests. (chosen by the fix run)

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Review an Evidence-Bounded Test Candidate (Priority: P1)

As a candidate reviewer, I need a test scope that separates documented observations from unknown Java behaviour so that a Go rebuild is not evaluated against invented compatibility claims.

**Why this priority**: The declared goal is `test`, but the available record does not provide an observable behaviour, entry point, input, output, state change, or error outcome to test.

**Independent Test**: Review this specification and confirm that every statement about the legacy estate is traceable to the Evidence Record and Limits section, while no behavior-specific Java or Go test is proposed.

**Acceptance Scenarios**:

1. **Given** the documented zero-item inventory, **When** a reviewer reads the candidate, **Then** the candidate records the evidence limitation and does not treat zero recorded items as proof that the estate has no behaviour.
2. **Given** a proposed behavior-specific Java or Go test without source-grounded observable inputs and outcomes, **When** it is assessed against this candidate, **Then** it is outside the candidate's approved scope.
3. **Given** a reviewer can supply a concrete observable Java behavior, **When** they provide its entry point, inputs, outcomes, and evidence, **Then** the candidate can be revised into a behavior-specific scope.

### Edge Cases

- A source document marked `**UNAVAILABLE**` is a reading limitation, not negative evidence about persistence, endpoints, security, errors, or workflows.
- A reported count of `0` inventory items, components, behaviours, or rules is not evidence that the legacy estate contains none of those things.
- A requested test case that has no cited observable behavior remains out of scope unless a later revision records its entry point, inputs, outcomes, and source evidence.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The candidate MUST preserve the distinction between absent recorded evidence and absent legacy behavior, including the quoted limitation: `This is a missing reading, NOT an estate with nothing in it.`
- **FR-002**: The candidate MUST identify the current evidence state as `**Inventory items**: 0`, `| components | 0 |`, `| behaviours | 0 |`, and `| rules | 0 |`, with `overview.md` as its source.
- **FR-003**: The candidate MUST NOT approve, describe, or claim equivalence for a behavior-specific Java or Go test until that behavior has a cited observable input, outcome, state change, or error outcome.
- **FR-004**: The candidate MUST record the scope decision that no source-grounded observable Java behavior is identified and that the behavior-specific test scope is empty with 0 approved Java-to-Go equivalence tests.
- **FR-005**: The candidate MUST identify behavior discovery and the definition of executable acceptance criteria as prerequisites to a behavior-specific Java-to-Go test scope.

### Key Entities

- **Evidence record**: A documented observation from `../../old/docs/`, including its file and verbatim supporting text.
- **Behavioral claim**: A proposed statement of Java behavior that requires a cited observable input, outcome, state change, or error outcome before it can become test scope.
- **Test scope**: The bounded set of behavior-specific claims permitted for evaluation; it is empty in this candidate because no source-grounded observable Java behavior is identified.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of statements about the legacy estate in the candidate cite a document in `../../old/docs/` and quote the supporting observation.
- **SC-002**: The candidate approves 0 behavior-specific Java-to-Go equivalence tests until the required observable behavior is supplied.
- **SC-003**: A reviewer can identify the evidence limitation, the excluded behavior-specific scope, and the single recorded scope decision within 5 minutes of reading the candidate.
- **SC-004**: One reviewer can determine, without interpreting a zero count as negative evidence, whether a proposed test has sufficient cited inputs and outcomes to enter scope.

## Assumptions

- The files under `../../old/docs/` are the only authorized evidence for this work unit.
- No source-grounded behavioral inventory, executable Java observation, or acceptance case has been supplied in this workspace.
- The operator-declared languages and goal provide context only; they do not establish a Java behavior or a Go acceptance requirement.
- A later revision must record source-grounded observable behavior and executable acceptance criteria before a behavior-specific plan, task list, implementation, or characterization test is created.
