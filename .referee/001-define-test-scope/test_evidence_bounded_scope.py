"""Acceptance tests for the evidence-bounded test-scope work order.

Run explicitly from the candidate workspace, for example:
    python -m unittest discover -s .referee/001-define-test-scope -p 'test_*.py'

Set CANDIDATE_ROOT when the command is launched from another directory.
"""

from __future__ import annotations

import os
import re
import unittest
from pathlib import Path


FEATURE = Path("specs") / "001-define-test-scope"
REQUIRED_ARTIFACTS = ("research.md", "data-model.md", "quickstart.md")


def candidate_root() -> Path:
    """Locate the workspace without depending on a runner-specific absolute path."""
    root = Path(os.environ.get("CANDIDATE_ROOT", Path.cwd())).resolve()
    if not (root / FEATURE / "spec.md").is_file():
        raise AssertionError(
            "Run these tests from the candidate workspace or set CANDIDATE_ROOT; "
            f"expected {(root / FEATURE / 'spec.md')}"
        )
    return root


def contains_all(text: str, fragments: tuple[str, ...]) -> list[str]:
    folded = text.casefold()
    return [fragment for fragment in fragments if fragment.casefold() not in folded]


class EvidenceBoundedScopeAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = candidate_root()
        cls.feature_dir = cls.root / FEATURE
        cls.artifacts: dict[str, str] = {}
        for name in REQUIRED_ARTIFACTS:
            path = cls.feature_dir / name
            if not path.is_file():
                raise AssertionError(f"Required review artifact is missing: {path}")
            cls.artifacts[name] = path.read_text(encoding="utf-8")
        cls.all_artifacts = "\n".join(cls.artifacts.values())

    def test_records_the_zero_inventory_as_a_missing_reading_not_an_empty_estate(self) -> None:
        """FR-001/FR-002: literal evidence and its non-negative interpretation remain visible."""
        missing = contains_all(
            self.all_artifacts,
            (
                "overview.md",
                "Inventory items: 0",
                "components | 0",
                "behaviours | 0",
                "rules | 0",
                "This is a missing reading, NOT an estate with nothing in it.",
            ),
        )
        self.assertFalse(missing, f"The evidence limitation is incomplete; missing: {missing}")

        # A reviewer must not have to infer the essential distinction from a count.
        self.assertRegex(
            self.all_artifacts,
            re.compile(
                r"(?:not|does not)\s+(?:mean|prove|establish|show).*?"
                r"(?:estate|legacy).*?(?:no|nothing|empty)|"
                r"(?:missing|unavailable)\s+reading.*?(?:not|does not).*?"
                r"(?:empty|no behavior|nothing)",
                re.IGNORECASE | re.DOTALL,
            ),
            "Artifacts must explicitly say that missing/zero recorded evidence is not "
            "evidence of an empty legacy estate.",
        )

    def test_records_the_empty_approved_behavior_test_scope(self) -> None:
        """FR-004 and SC-002: the decision is explicit, rather than merely omitting tests."""
        missing = contains_all(
            self.all_artifacts,
            (
                "no source-grounded observable Java behavior is identified",
                "behavior-specific test scope is empty",
                "0 approved Java-to-Go equivalence tests",
            ),
        )
        self.assertFalse(missing, f"The empty-scope decision is incomplete; missing: {missing}")

    def test_defines_reviewable_evidence_claim_and_scope_fields(self) -> None:
        """T002: reviewers can apply an admission decision to a proposed claim."""
        model = self.artifacts["data-model.md"]
        missing = contains_all(model, ("Evidence Record", "Behavioral Claim", "Test Scope"))
        self.assertFalse(missing, f"data-model.md lacks required review entities: {missing}")

        # The rule needs both provenance and observable behavior, not a vague request
        # for "more evidence".
        missing = contains_all(
            self.all_artifacts,
            (
                "entry point",
                "input",
                "outcome",
                "state change",
                "error outcome",
                "executable acceptance criterion",
                "cited",
            ),
        )
        self.assertFalse(missing, f"The future-test admission fields are incomplete: {missing}")

    def test_rejects_any_claim_with_missing_required_observable_evidence(self) -> None:
        """FR-003/T008: all required fields gate admission; no partial claim enters scope."""
        text = "\n".join((self.artifacts["research.md"], self.artifacts["data-model.md"], self.artifacts["quickstart.md"]))
        self.assertRegex(
            text,
            re.compile(
                r"(?:missing|without|lacks?).{0,500}?"
                r"(?:entry point|input|outcome|state change|error outcome|acceptance criterion).{0,700}?"
                r"(?:outside|out of scope|reject|not approve|cannot be approved|remains.*scope)",
                re.IGNORECASE | re.DOTALL,
            ),
            "Documentation must show that a claim missing an observable-evidence field "
            "is rejected or remains outside scope.",
        )

    def test_quickstart_is_a_repeatable_manual_review_with_both_outcomes(self) -> None:
        """T003/T007 and SC-003/SC-004: the acceptance check is usable without a runtime."""
        guide = self.artifacts["quickstart.md"]
        self.assertRegex(
            guide,
            re.compile(r"(?:step\s*1|1[.)]).{0,2500}(?:step\s*2|2[.)])", re.IGNORECASE | re.DOTALL),
            "quickstart.md must provide at least two ordered validation scenarios/steps.",
        )
        missing = contains_all(
            guide,
            (
                "Inventory items: 0",
                "This is a missing reading, NOT an estate with nothing in it.",
                "0",
                "outside scope",
            ),
        )
        self.assertFalse(missing, f"quickstart.md cannot validate both outcomes; missing: {missing}")

    def test_all_review_artifacts_preserve_authorized_evidence_provenance(self) -> None:
        """SC-001/T005: each reviewer-facing artifact identifies the authorized evidence set."""
        for name, text in self.artifacts.items():
            self.assertRegex(
                text,
                re.compile(r"(?:\.\./)*old/docs/|old/docs/", re.IGNORECASE),
                f"{name} must cite the authorized ../../old/docs/ evidence location.",
            )

        # These unavailable observations must remain limitations, so a reviewer does
        # not turn missing persistence or routing evidence into a negative claim.
        missing = contains_all(
            self.all_artifacts,
            ("data_model.md", "api_surface.md", "UNAVAILABLE"),
        )
        self.assertFalse(missing, f"Missing-reading provenance is incomplete: {missing}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
