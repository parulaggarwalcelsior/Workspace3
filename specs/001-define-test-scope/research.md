# Phase 0 Research: Evidence-Bounded Test Scope

## Decision 1: Treat the zero inventory as a reading limitation, not an empty estate

- **Decision**: Record the available inventory exactly as reported and prohibit an inference that the legacy estate has no behavior.
- **Rationale**: [overview.md](../../old/docs/overview.md) reports `Inventory items: 0` and its shape table reports `components | 0`, `behaviours | 0`, and `rules | 0`. It also states: `This is a missing reading, NOT an estate with nothing in it.`
- **Alternatives considered**:
  - Treat the zero counts as proof there is nothing to test — rejected because the quoted overview statement expressly forbids that inference.
  - Invent a minimal behavior to make a test executable — rejected because no observed behavior or source symbol is documented.

## Decision 2: Approve no behavior-specific Java-to-Go equivalence test

- **Decision**: Set the candidate's approved behavior-specific test count to `0`.
- **Rationale**: [prd.md](../../old/docs/prd.md) states `_No enforced requirements were derived._`; [brd.md](../../old/docs/brd.md) records `0 rule(s) across 0 business area(s).`; [approach.md](../../old/docs/approach.md) says `No behaviours or components are identified; discovery is prerequisite to any testing or translation.` No cited entry point, input, observable outcome, state change, or error outcome exists from which a characterization or parity test can be designed.
- **Alternatives considered**:
  - Select a Java and Go test framework now — rejected because it would not establish the missing behavior or acceptance oracle.
  - Specify a parity strategy now — rejected because there is no behavior to compare.

## Decision 3: Keep legacy runtime and integration characteristics unselected

- **Decision**: Do not choose Java or Go versions, dependencies, storage, platform, project type, performance targets, test harnesses, or external-interface contracts for this feature.
- **Rationale**: The legacy documents do not provide those facts. [data_model.md](../../old/docs/data_model.md) is `**UNAVAILABLE**` and says the absence of a recorded table or field `does not mean the estate stores nothing`. [api_surface.md](../../old/docs/api_surface.md) is `**UNAVAILABLE**` and says a missing endpoint record may mean either no endpoint or an unrecognized routing stack. [security.md](../../old/docs/security.md), [edge_cases.md](../../old/docs/edge_cases.md), and [workflows.md](../../old/docs/workflows.md) state that the code graph could not be searched.
- **Alternatives considered**:
  - Assume a web service, database, or batch process from the available documents — rejected because each would add behavior or structure not present in the evidence.
  - Treat the declared `java` to `go` direction as a selected implementation stack — rejected because it supplies migration context, not runtime versions or a build design.

## Decision 4: Define the admission rule for a later behavior-specific scope

- **Decision**: A future behavior-specific scope must provide a cited Java entry point and observable inputs plus expected output, state change, or error outcome; it must also define executable acceptance criteria.
- **Rationale**: [approach.md](../../old/docs/approach.md) lists as prerequisite work: `Read and inventory the codebase to identify components and entry points`, `Extract and document observable behaviours and business rules from the Java code`, and `Define the acceptance basis concretely (inputs, outputs, invariants) in a testable form`.
- **Alternatives considered**:
  - Allow review intuition or the operator goal `test` to admit a test — rejected because neither identifies observable behavior.
  - Wait only for a Go design — rejected because the Constitution requires observable characterization before translation.

## Resolution of Planning Unknowns

The legacy runtime, dependencies, storage, platform, type, performance needs, and interfaces remain unknown facts about the estate. They are not unresolved design choices for this documentation-only candidate: the chosen design is to leave them unselected and not implement or test them. The only runnable validation is the evidence review in [quickstart.md](quickstart.md).
