import re

try:
    import pdfplumber
except ImportError:
    print("Error: pdfplumber is not installed. Install it using: pip install pdfplumber")
    exit()

try:
    # Step 1: Read resume file
    file_name = input("Enter resume file name (.txt / .pdf): ")
    resume_data = ""

    # Handle TXT files
    if file_name.endswith(".txt"):
        with open(file_name, "r", encoding="utf-8") as file:
            resume_data = file.read()

    # Handle PDF files
    elif file_name.endswith(".pdf"):
        with pdfplumber.open(file_name) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:  # avoid None error
                    resume_data += text

    else:
        print("Unsupported file format (Only .txt and .pdf allowed)")
        exit()

    # Convert to lowercase
    resume_data = resume_data.lower()
    print("\nResume loaded successfully!\n")

    # Step 2: Take job skills input
    skills_input = input("Enter required skills (comma separated): ").lower()
    required_skills = [skill.strip() for skill in skills_input.split(",")]

    total_skills = len(required_skills)
    matched_skills = 0

    print("\nChecking skills...\n")

    # Step 3: Match skills using regex
    for skill in required_skills:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, resume_data):
            print(f"{skill}  Found")
            matched_skills += 1
        else:
            print(f"{skill}  Not Found")

    # Step 4: Calculate score
    if total_skills > 0:
        score = (matched_skills / total_skills) * 100
    else:
        score = 0

    print("\n-------------------------")
    print(f"Matched Skills: {matched_skills}/{total_skills}")
    print(f"Resume Score: {score:.2f}/100")

    # Step 5: Classification
    print("\nResult:")

    if score > 90:
        print("Priority Candidate")
    elif score >= 70:
        print("Shortlisted")
    else:
        print("Not Selected")

except FileNotFoundError:
    print("Error: Resume file not found. Please check file name.")

except Exception as e:
    print("Something went wrong:", e)