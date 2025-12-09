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
    Given a ISBN return de index in the dataframe that corresponds to that index
    """
    # Generate the sample df
    sample_df = sample_df_recommender()
    # Retrieve the index
    idx = isbnToIndx("111", sample_df)
    # It should be the first index
    assert idx == 0

def test_matchCluster():
    """
    Given an index we get all the indexes in that cluster
    """
    # Generate the sample df
    sample_df = sample_df_recommender()
    # Get the matches for the index in the sample df
    matches = matchCluster(0,sample_df)
    # Check the set is correct
    assert set(matches) == {0,1,2}

def test_recommend():
    """
    Test given an isbn return the top n results
    """
    # Generate the sample df
    sample_df = sample_df_recommender()
    # Isbn sample
    isbn = "111"
    # Recommend indexes
    rec_indexes = recommend(isbn, sample_df, n=2)
    # The order two indexes in the sample
    assert rec_indexes == [2,1]
    
