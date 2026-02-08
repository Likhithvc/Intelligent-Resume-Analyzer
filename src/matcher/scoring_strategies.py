from src.matcher.matcher import match_candidate


class ScoringStrategy:
    """Base scoring interface."""

    def calculate(self, candidate, job, resume_text, jd_text):
        raise NotImplementedError

class RuleBasedScoring(ScoringStrategy):

    def calculate(self, candidate, job, resume_text, jd_text):

        score_data = match_candidate(
            candidate,
            job,
            resume_text,
            jd_text
        )

        return {
            "final_score": score_data["rule_score"],
            "semantic_score": 0
        }

class HybridWeightedScoring(ScoringStrategy):

    def calculate(self, candidate, job, resume_text, jd_text):

        score_data = match_candidate(
            candidate,
            job,
            resume_text,
            jd_text
        )

        # Example weighting
        final_score = (
            score_data["rule_score"] * 0.6 +
            score_data["semantic_score"] * 0.4
        )

        return {
            "final_score": round(final_score, 2),
            "semantic_score": score_data["semantic_score"]
        }
