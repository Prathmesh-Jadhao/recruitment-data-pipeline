import streamlit as st
import sqlite3
import pandas as pd

st.title("Recuritement Analytics Dashboard")

conn = sqlite3.connect("recruitment.db")

# Selection Rate

query = """
SELECT result, COUNT(*) as count
FROM candidates GROUP BY result
"""

df = pd.read_sql(query,conn)

st.subheader("Selection Distribution")
st.bar_chart(df.set_index("result"))

# # Top Skills

query = """
SELECT cs.skill, COUNT(*) as count
FROM candidates_skills cs
JOIN candidates c
ON cs.candidate_id = c.candidate_id
WHERE c.result = 'Selected'
GROUP BY cs.skill
ORDER BY count DESC
LIMIT 10
"""

df = pd.read_sql(query,conn)

st.subheader("Top Skills of Selected Candidates")
st.bar_chart(df.set_index("skill"))

# Avg Score by Role

query = """
SELECT applied_role, AVG(interview_score) as avg_score
FROM candidates
GROUP BY applied_role
"""

df = pd.read_sql(query,conn)

st.subheader("Average Score by Role")
st.bar_chart(df.set_index("applied_role"))

# Experience vs Selection

query = """
SELECT experience_years,
COUNT(*) as total,
SUM(CASE WHEN result = 'Selected' THEN 1 ELSE 0 END) as selected
FROM candidates
GROUP BY experience_years
"""

df = pd.read_sql(query, conn)

st.subheader("Experience vs Selection")
st.line_chart(df.set_index("experience_years")[["total","selected"]])
