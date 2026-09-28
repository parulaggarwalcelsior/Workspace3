# Acceptance tests: Define Evidence-Bounded Test Scope

Run from the candidate workspace (or set `CANDIDATE_ROOT` to it):

```bash
python -m unittest discover -s .referee/001-define-test-scope -p 'test_*.py'
```

The suite is intentionally documentation-only. It checks the required evidence-review artifacts and admission boundary; it does not prescribe or execute Java/Go behavior tests.
