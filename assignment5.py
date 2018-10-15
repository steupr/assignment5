'''Assignment 5 (Version 1.0)

Please add your code where indicated. You may conduct a superficial test of
your code by executing this file in a python interpreter.

The documentation strings ("docstrings") for each function tells you what the
function should accomplish. If docstrings are unfamiliar to you, consult the
Python Tutorial section on "Documentation Strings".

This assignment requires the following packages:

- numpy
- pandas

All these packages should be installed if you are using Anaconda.

'''

import os
import unittest

import numpy as np
import pandas as pd

TWITTER_DATA_FILENAME = os.path.join(os.path.dirname(__file__), 'data', 'united-states-congress-house-twitter-2016-grouped-tweets-train.csv')
WORD_VECTORS_FILENAME = os.path.join(os.path.dirname(__file__), 'data', 'united-states-congress-house-twitter-2016-word-vectors-fasttext.csv.xz')


# more API practice

def get_user_agent():
    """Use https://httpbin.org to get the 'user-agent' of `requests`.

    Find the appropriate endpoint at https://httpbin.org/

    The user-agent string is something like this:
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0"

    Returns:
        str: user-agent string used by `requests`

    """
    # YOUR CODE HERE


# semantic word vectors practice

# `load_word_vectors` is provided for you. Do not edit this function.
def load_word_vectors():
    # data loading function; do not modify
    return pd.read_csv(WORD_VECTORS_FILENAME, index_col=0)


def find_similar_word(word):
    """Use the provided word vectors to find a semantically similar word.

    Args:
        word (str): query word

    Returns:
        word (str): semantically related word

    """
    word_vectors = load_word_vectors()
    # YOUR CODE HERE


def word_distance(word1, word2):
    """Use the provided word vectors to calculate the semantic "distance" between two words.

    Use Euclidean or Manhattan distance.

    Args:
        word1 (str): first word
        word2 (str): second word

    Returns:
        float: distance between words

    """
    # YOUR CODE HERE



# challenge problem: minor revision to assignment 4


# `load_twitter_corpus` is provided for you. Do not edit this function.
def load_twitter_corpus():
    """Load US Congress Twitter corpus.

    Returns a pandas DataFrame with the following columns:

    - ``screen_name`` Member of Congress' Twitter handle (unused)
    - ``party`` Party affiliation. 0 is Democratic, 1 is Republican
    - ``tweets`` Text of five tweets concatenated together.

    Each record contains multiple tweets connected by a space. Grouping tweets
    together is not strictly necessary.

    Returns:

        pandas.DataFrame: DataFrame with tweets.

    """
    # data loading function; do not modify
    return pd.read_csv(TWITTER_DATA_FILENAME)


def predict_party_many(tweet_list, twitter_corpus):
    """Predict party affiliations given the text of a tweets.

    See assignment 4 for more details. The difference here is small: your
    function must accept a list of tweets and return a list of integers
    indicating estimated party membership.

    Try to exploit the fact that you are making several predictions in a batch.

    Args:

        tweet_list (list of str): a tweet (or more than one tweet) from a member of Congress as a Python string.
        twitter_corpus (pandas.DataFrame): DataFrame returned by ``load_twitter_corpus``.

    Returns:
        list of int: 0 is Democratic, 1 is Republican.

    """
    # YOUR CODE HERE




# DO NOT EDIT CODE BELOW THIS LINE




class TestAssignment5(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = load_twitter_corpus()

    def test_get_user_agent1(self):
        result = get_user_agent()
        self.assertTrue(isinstance(result, str))

    def test_find_similar_word1(self):
        result = find_similar_word('administration')
        expected = 'government'
        self.assertEqual(result, expected)

    def test_word_distance1(self):
        distance = word_distance('administration', 'government')
        self.assertGreaterEqual(distance, 0)

    def test_predict_party_many1(self):
        df = self.df
        tweet_list = ["""RT @HouseGOP: The #StateOfTheUnion is strong.""",
                      """RT @HouseGOP: The #StateOfTheUnion is strong.""",
                      """Lorem ipsum dolorem @sunt."""] * 1000
        party_list = predict_party_many(tweet_list, df)
        for party in party_list:
            self.assertIn(party, {0, 1})


if __name__ == '__main__':
    unittest.main()
