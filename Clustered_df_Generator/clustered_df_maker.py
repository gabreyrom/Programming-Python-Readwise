# This file is not meant to be run as part of the program-
# It is included in case clustered_df.csv
# is not available or needs to be remade.

import pandas as pd
import ast
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import MiniBatchKMeans

# recommended for minibatchkmeans
import os
os.environ["OMP_NUM_THREADS"] = "2"

# load data
filepath = ".\\data\\final_df.csv"
df = pd.read_csv(filepath)

# some additional data cleaning & organizing

# remove duplicate and uninformative features
# df = data.drop(['publisher_x', 'title_y', 'author(s)_y', 'average_rating_y', 'ratings_count_y', 'text_reviews_count_y',
#                  'language_code_y', 'num_pages_y', 'publisher_y', 'publication_date_y'], axis=1)

# consolidate english language tags
df.replace(['en-US', 'en-GB', 'en-CA'], 'eng', inplace=True)

# change genre data into lists
df['genres'] = df['genres'].apply(ast.literal_eval)

# one-hot encoding for language codes
onehot = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
langs = pd.DataFrame(onehot.fit_transform(pd.DataFrame(df['language_code'])), columns=onehot.categories_[0])
langs *= 3 # heavier weights for languages than other features
df = pd.concat([df, langs], axis=1)

# multi-hot encoding for genres
mlb = MultiLabelBinarizer()
genre_matrix = mlb.fit_transform(df['genres'])
genres = pd.DataFrame(genre_matrix, columns=mlb.classes_)
df = pd.concat([df, genres], axis=1)

# remove redundant and irrelevant columns
df.drop(['language_code', 'genres', 'publisher'], axis=1, inplace=True)

# data scaling for KMeans
scaler = StandardScaler()
feats = ['num_pages', 'average_rating', 'ratings_count', 'text_reviews_count']
X = df[feats]
df.drop(feats, axis=1, inplace=True)
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=feats)
df = pd.concat([df, X_scaled], axis=1)

# create dataframe of only prepared features
feat_df = df.drop(['isbn13', 'title', 'author(s)', 'publication_date'], axis=1)

do_cluster = 'y'
while do_cluster != 'n':

    # clustering
    kmeans = MiniBatchKMeans(n_clusters=50, batch_size=512)
    clusters = kmeans.fit_predict(feat_df)

    # df['cluster'] = kmeans.labels_
    df['cluster'] = clusters

    # preview the DataFrame
    print("\nDataFrame head:\n", df.head())
    print("\nDataFrame tail:\n", df.tail())
    print("\nCluster value counts:\n", df['cluster'].value_counts())

    do_cluster = input("\nRe-cluster the data? [y/n] ").lower()
    while do_cluster != 'y' and do_cluster != 'n':
        do_cluster = input("Unexpected input; re-cluster the data? [y/n] ").lower()


do_save = input("Save data to .csv? Data will be discarded otherwise. [y/n] ").lower()
while do_save != 'y' and do_save != 'n':
    do_save = input("Unexpected input; save data to .csv? [y/n] ").lower()
if do_save == 'y':
    pd.to_csv("new_cluster_df.csv", index=False)