from survey import AnonSurvey
from pathlib import Path
import json


#path = Path("/Users/prithvi_vasistha/Documents/ppv-skill-dev/python/Codes-Notebooks/github/chapter-11-testing-with-pytest/Testing-a-class/testcases.json")
#
#testcases = read_text(path)
#testcases = json.loads()

def test_survey_code():
    question = "What language did you first learn to speak?"
    my_survey = AnonSurvey(question)
    my_survey.add_answer("Kannada")
    assert "Kannada" in my_survey.answer

