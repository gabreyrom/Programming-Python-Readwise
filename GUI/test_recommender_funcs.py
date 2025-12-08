import pytest
from recommender_funcs import *


def sample_df_recommender():
    """
    Function that creates a sample dataframe for testing.
    """
    sample_df = pd.DataFrame({
        "isbn13": ["111", "222", "333"],
        "title_x": ["A", "B", "C"],
        "author(s)_x": ["X", "Y", "Z"],
        "publication_date_x": ["2020", "2020", "2020"],
        "cluster": [0, 0, 0],
        "f1": [1, 0, 0],
        "f2": [0, 1, 0],
        "f3": [0, 0, 1],
    })

    return sample_df

def test_isbnToIndx():
    """
    Docstring for test_isbnToIndx
    """

    sample_df = sample_df_recommender()

    idx = isbnToIndx("111", sample_df)
    assert idx == 0

