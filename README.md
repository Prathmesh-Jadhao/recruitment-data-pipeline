# Recruitment Analytics Data Pipeline

## Overview
Built an end-to-end data engineering pipeline to process and analyze recruitment data, transforming unstructured resume data into actionable hiring insights.

## Tech Stack
- Python (Pandas)
- SQL (SQLite)
- Streamlit
- Faker (data generation)

## Architecture
Raw Data → Processing → Transformation → Database → Dashboard

## Features
- Resume parsing to extract candidate skills
- Normalized database design (candidates + skills)
- SQL-based analytics:
  - Selection rate
  - Top skills of selected candidates
  - Experience vs hiring trends
- Interactive dashboard using Streamlit

## Project Structure
- data/ → raw & processed data
- src/ → pipeline code
- sql/ → analysis queries
- dashboard/ → Streamlit app

## How to Run
```bash
python src/ingestion/generate_data.py
python main.py
streamlit run dashboard/app.py
