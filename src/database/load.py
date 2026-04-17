import sqlite3
import pandas as pd

def load_to_db(main_df, skills_data):
    conn = sqlite3.connect("recruitment.db")

    main_df = main_df.drop(columns=["skills"])

    main_df.to_sql("candidates", conn, if_exists="replace", index = False)

    skills_df = pd.DataFrame(skills_data)
    skills_df.to_sql("candidates_skills", conn, if_exists="replace", index=False)

    conn.close()