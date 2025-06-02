#IN this code, we have not utilized fixtures
from survey import AnonSurvey
from pathlib import Path
import json


#path = Path("/Users/prithvi_vasistha/Documents/ppv-skill-dev/python/Codes-Notebooks/github/chapter-11-testing-with-pytest/Testing-a-class/testcases.json")
#
#testcases = read_text(path)
#testcases = json.loads()

def test_store_single_response():
    question = "What language did you first learn to speak?"
    my_survey = AnonSurvey(question)
    my_survey.add_answer("Kannada")
    assert "Kannada" in my_survey.answer

def test_store_multiple_responses():
    question = "What language did you first learn to speak?"
    my_survey = AnonSurvey(question)
    lang_list = ["kannada","english","hindi","tamil","telugu","malayalam","konkani","spanish"]
    for language in lang_list:
        my_survey.add_answer(language)

    assert "kannada" in my_survey.answer
    assert "english" in my_survey.answer
    assert "hindi" in my_survey.answer
    


