# Conceptual Data Model: Evidence-Bounded Test Scope

This is a model of the candidate's review records, not a claim about the legacy estate's persisted data. [data_model.md](../../old/docs/data_model.md) is `**UNAVAILABLE**` and states that no recorded table or field `does not mean the estate stores nothing`.

## Evidence Record

| Field | Description | Validation |
|---|---|---|
| source document | Authorized legacy document relative to `../../old/docs/` | Must name a document used by the candidate. |
| verbatim observation | Exact text supporting the record | Must be quoted exactly; interpretation alone is insufficient. |
| reading limitation | Whether the text reports a limitation of the reading | Must not be translated into a negative claim about the estate. |

## Behavioral Claim

| Field | Description | Validation |
|---|---|---|
| proposed claim | Statement proposed for test scope | Cannot assert undocumented behavior. |
| cited evidence | Evidence Record(s) supporting the claim | Must cite the Java entry point and include source-grounded observable evidence. |
| Java entry point | The observed Java symbol or entry point | Required before behavior-specific scope approval and must be cited by the claim's Evidence Record(s). |
| observable inputs | Inputs used to exercise the behavior | Required before approval. |
| observable outcome | Expected output, state change, or error outcome | At least one is required before approval. |
| acceptance criterion | Executable condition for the proposed test | Required before approval. |

## Test Scope

| Field | Description | Validation |
|---|---|---|
| approved claims | Behavioral Claims admitted to evaluation | Every claim must pass the Behavioral Claim validation. |
| approved test count | Count of approved behavior-specific Java-to-Go equivalence tests | Is `0` for this candidate. |
| decision | Scope outcome | Must distinguish missing reading from absent legacy behavior. |

## Future-Test Admission Rule

A Behavioral Claim may enter a future behavior-specific Test Scope only when all four required fields are present: a cited Java entry point, observable inputs, at least one observable outcome (output, state change, or error outcome), and an executable acceptance criterion. This rule defines admission only; satisfying it permits later review and does not approve a claim automatically.

## Relationships and State

```text
Evidence Record(s) --> Behavioral Claim --> Test Scope
                         (complete observable evidence required)
```

- A Behavioral Claim without its required observable evidence is **outside scope**.
- A Behavioral Claim with cited, complete observable evidence may be **proposed for later review**; this plan does not approve it automatically.
- The current Test Scope is **empty** and has `0` approved behavior-specific Java-to-Go equivalence tests.
