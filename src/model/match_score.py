def calculate_skill_match(resume_skills, jd_skills):
    if not resume_skills or not jd_skills:
        return 0
    matched = [skill for skill in jd_skills if skill.lower() in map(str.lower, resume_skills)]
    score = (len(matched) / len(jd_skills)) * 100
    return round(score)
