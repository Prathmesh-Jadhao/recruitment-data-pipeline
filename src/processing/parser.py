SKILLS = [
    "Python", "SQL", "Machine Learning", "Deep Learning",
    "NLP", "Java", "AWS", "Docker", "Power BI", "Excel"
]

def extract_skills(text):
    found = []
    text = text.lower()

    for skill in SKILLS:
        if skill.lower() in text:
            found.append(skill)
    
    return found