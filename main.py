from src.ingestion.ingest import load_candidates, load_interviews
from src.transformation.transform import transform_data
from src.transformation.skills_transform import create_skills_table
from src.database.load import load_to_db

def run_pipeline():
    candidates = load_candidates()
    interviews = load_interviews()

    final_df = transform_data(candidates, interviews)
    skills_data = create_skills_table(final_df)

    load_to_db(final_df,skills_data)

    print("Pipeline completed!")

if __name__ == "__main__":
    run_pipeline()