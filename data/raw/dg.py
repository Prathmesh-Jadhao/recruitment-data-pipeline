from faker import Faker
import random
import pandas as pd

fake = Faker()

skills_pool = [
    "Python", "SQL", "Machine Learning", "Deep Learning",
    "NLP", "Java", "AWS", "Docker", "Power BI", "Excel"
]

roles = ["Data Scientist", "Data Analyst", "ML Engineer", "Backend Developer"]
educations = ["BTech", "MTech", "BSc", "MSc"]

def generate_candidates(n=100):
    data = []

    for i in range(n):
        skills = random.sample(skills_pool, k=random.randint(3, 6))
        resume_text = "Experienced in " + " ".join(skills)

        data.append({
            "candidate_id": i,
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "experience_years": random.randint(0, 5),
            "education": random.choice(educations),
            "resume_text": resume_text,
            "applied_role": random.choice(roles),
            "application_date": fake.date_this_year()
        })

    return pd.DataFrame(data)


def generate_interviews(candidates_df):
    data = []

    for _, row in candidates_df.iterrows():
        base_score = random.randint(40, 80)

        if "Python" in row["resume_text"]:
            base_score += 10

        score = min(base_score, 95)

        result = "Selected" if score > 70 else "Rejected"

        data.append({
            "candidate_id": row["candidate_id"],
            "interview_score": score,
            "interview_round": random.choice(["HR", "Technical", "Final"]),
            "result": result,
            "interview_date": fake.date_this_year()
        })

    return pd.DataFrame(data)


if __name__ == "__main__":
    candidates = generate_candidates(100)
    interviews = generate_interviews(candidates)

    candidates.to_csv(r"E:\recruitment-data-pipeline\data\raw\candidates.csv", index=False)
    interviews.to_csv(r"E:\recruitment-data-pipeline\data\rawinterviews.csv", index=False)

    print("Data generated!")