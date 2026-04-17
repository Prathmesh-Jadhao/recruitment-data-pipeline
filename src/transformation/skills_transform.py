def create_skills_table(df):
    rows=[]

    for _, row in df.iterrows():
        for skill in row["skills"]:
            rows.append({
                "candidate_id": row["candidate_id"],
                "skill": skill
            })

    return rows

