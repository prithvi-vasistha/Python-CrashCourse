
"""======================================= Using test fixtures ==========================================="""
#############################################################################################################
""" initiating the class multiple times in multiple functions for small codes can be fine but, when we are working with a large file, it becomes hectic hence we use fixtures which is a built-in method of pytest"""


import pytest
from survey import AnonSurvey

@pytest.fixture

def my_survey():
    """ This is a survey which is available to all functions """
    question = "What language do you speak???"
    my_survey = AnonSurvey(question)
    return my_survey

def test_store_single_response_survey(my_survey):
    """Test if a single response is stored properly"""
    response = "kannada"
    my_survey.add_answer(response)
    assert 'kannada' in my_survey.answer

def test_multiple_values(my_survey):
    """Test if a multiple response is stored properly"""
    response = ["kannada","english","tamil","telugu","malayalam","hindi","arabic","spanish"]
    for resp in response:
        my_survey.add_answer(resp)

    for resp in response:
        assert resp in my_survey.answer
