from name_function import *
def test_first_and_last_names():
    formatted_name = get_formatted_name("prithvi", "vasistha")
    assert formatted_name == "Prithvi Vasistha"
    formatted_name = get_formatted_name("kyouka","jiro", "middle" )   
    assert formatted_name == "Kyouka Middle Jiro"
    formatted_name = get_formatted_name("hatsune", "miku")
    assert formatted_name == "Hatsune Miku"
