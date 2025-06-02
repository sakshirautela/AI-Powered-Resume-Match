def calculate_skill_match(resume_skills, jd_skills):
    resume_set = set(map(str.lower, resume_skills))
    jd_set = set(map(str.lower, jd_skills))
    if not jd_set:
        return 0.0
    match = resume_set & jd_set
    return round(len(match) / len(jd_set) * 100, 2)
