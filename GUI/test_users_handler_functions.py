import pytest
from users_handler_functions import *


def sample_df_users():
    """
    Function that creates a sample dataframe for testing.
    """
    sample_df = pd.DataFrame([
        {
            "username": "aalen",
            "password": "123",
            "first_name": "A",
            "last_name": "H",
            "birth_date": "2000-01-01",
            "books_read": '[["Harry Potter 1","111"], ["Harry Potter 2","222"]]'
        }
    ])

    return sample_df

def test_get_user():
    """
    Testing getting a user from the sample df
    """
    sample_df = sample_df_users()

    user = get_user("aalen", sample_df)
    assert type(user) == dict
    assert user["first_name"] == "A"
    assert user["last_name"] == "H"

def test_add_user():
    """
    Testing the adding a user to the sample data.
    """

    sample_df = sample_df_users()

    sample_user = {
            "username": "jas",
            "password": "321",
            "first_name": "Jasmine",
            "last_name": "Qiang",
            "birth_date": "2000-01-01",
            "books_read": '[["Harry Potter 3","333"], ["Harry Potter 4","444"]]'
        }
    
    assert add_user(sample_user, sample_df) == "User added succesfully"