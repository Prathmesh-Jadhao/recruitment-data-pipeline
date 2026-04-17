from src.processing.parser import extract_skills

def transform_data(candidates, interviews):
    candidates["skills"] = candidates["resume_text"].apply(extract_skills)

    merged = candidates.merge(interviews, on="candidate_id")

    return merged