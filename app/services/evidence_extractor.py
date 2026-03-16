import re


def extract_evidence(resume_text, skills):

    evidence = {}

    # Split resume into sentences
    sentences = re.split(r'[.\n]', resume_text)

    for skill in skills:

        skill_lower = skill.lower()

        matches = []

        for sentence in sentences:

            if skill_lower in sentence.lower():

                cleaned = sentence.strip()

                if len(cleaned) > 20:
                    matches.append(cleaned)

        if matches:
            evidence[skill] = matches[:2]  # keep top 2

    return evidence