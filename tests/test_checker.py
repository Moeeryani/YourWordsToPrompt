"""Positive and negative checks prove fixture conformance and rejection behavior."""
import json
import unittest
from scripts.check_conformance import (
    ROOT, HEAD, DIAG, QUEST, FENCE,
    evaluate, manifest_errors, response_errors, source_errors,
)

CASES = json.loads((ROOT/"tests/cases.json").read_text(encoding="utf-8"))["cases"]
ANSWERS = json.loads((ROOT/"tests/reference_responses.json").read_text(encoding="utf-8"))["responses"]


class ConformanceTests(unittest.TestCase):
    def test_canonical_prompt_and_skill_are_unchanged(self):
        self.assertEqual([], source_errors())

    def test_all_twelve_reference_cases(self):
        report = evaluate(CASES, ANSWERS)
        self.assertTrue(report["success"], report)
        self.assertEqual(12, report["automated_passes"])
        self.assertEqual(0, report["models_called"])

    def test_missing_response_is_rejected(self):
        broken = dict(ANSWERS)
        broken.pop("01-simple-writing")
        self.assertTrue(manifest_errors(CASES, broken))

    def test_added_response_is_rejected(self):
        broken = dict(ANSWERS, unexpected="test")
        self.assertTrue(manifest_errors(CASES, broken))

    def test_wrong_heading_is_rejected(self):
        self.assertTrue(response_errors(CASES[0], ANSWERS["01-simple-writing"].replace(HEAD,"## Prompt")))

    def test_extra_prose_is_rejected(self):
        self.assertTrue(response_errors(CASES[0], ANSWERS["01-simple-writing"]+"\nAnother thought."))

    def test_missing_domain_topic_is_rejected(self):
        bad = HEAD+"\n\n"+FENCE+"markdown\nWrite something nice.\n"+FENCE
        self.assertTrue(response_errors(CASES[2], bad))

    def test_questions_cannot_exceed_three(self):
        bad = ANSWERS["11-ambiguous-idea"] + "\nWhere? When? Why?"
        self.assertTrue(response_errors(CASES[10], bad))

    def test_missing_diagnosis_field_is_rejected(self):
        bad = ANSWERS["11-ambiguous-idea"].replace("- **Pruned:**", "- **Omitted:**")
        self.assertTrue(response_errors(CASES[10], bad))

    def test_diagnosis_field_order_is_enforced(self):
        bad = ANSWERS["11-ambiguous-idea"]
        first, second = "- **Task & Complexity:** Strategy / Medium", "- **Secondary Task:** Research"
        bad = bad.replace(first+"\n"+second,second+"\n"+first)
        self.assertTrue(any("order" in x for x in response_errors(CASES[10], bad)))

    def test_no_compiled_prompt_during_calibration(self):
        bad = ANSWERS["11-ambiguous-idea"]+"\n"+HEAD
        self.assertTrue(response_errors(CASES[10], bad))

    def test_no_diagnosis_in_compilation(self):
        bad = ANSWERS["01-simple-writing"].replace("Draft a brief",DIAG+"\nDraft a brief")
        self.assertTrue(response_errors(CASES[0], bad))


if __name__ == "__main__":
    unittest.main()
