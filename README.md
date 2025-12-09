# Readwise: Smart Book Recommendation System

### Team:
Jasmine Qiang\
Shen-Chun Huang\
Gabriel Reynoso

## Objective
Readwise is a desktop app (developed under a Tkinter environment) intended to be used as a lecture companion app, where you can see what’s trending, keep a record of what books you have read and also get recommendations of similar books based on a specific title or author of your preference.

## Main Features
### Login Page
In this page the user is either able to login with its credentials (username and password) or create an account in the bottom part.

If one of the boxes is not filled, it will get a warning. Also, if the password does not match the password saved for its username.

### Create Account Page
In the create account page the user can input its First Name, Last Name, username, password and birthday.

If the account creation is successful then a message will appear.

### Main Page
Once logged in, the user will see this window, in here the user can:
a) Search for a book, author or ISBN in the search box, by entering the text and clicking search or just clicking enter.
	If the user types something that does not match anything a messagebox will appear.

b) Open the Chat Assistant page
c) Open the Top 500 Books by Avg Rating
d) See their Account information
e) Click in Readwise Info an see the version of the project and the team members
f) Close the app

### Search Page
This page shows the result from the search that the user provided in the main page. Here the user can save the books that they have already read by checking the box in each book and then clicking in the button “"Save checked books” a message will appear and the information will be saved in the account page.

Also, at the top between “” it will appear the searched term and the user can select to display 3,5,10 books not sorted in any particular order.

### Chat Page
In this window the user will get the top 3 recommendations (from doing cosine similarity) from the input in the textbox of the button. It can ask recommendations on a book title, author or isbn. To send the message it should just click the “send button”.

### Top 500 books by average rating
In this view the user can explore the top 500 books with at least 100 ratings sorted by average rating and ratings count. It will see the Average rating, the rating count, book title, author(s) and ISBN13. It can scroll down to get the whole list.

### Account Page
In the account page the user will see the information provided at the registration window and also the books that have been marked as read in the search window. Here it can remove the books marked as read, just in case it was marked by accident or wants to read it again.

### Info Page
This is a small window that presents the information of the authors of the project and the version of the MVP.

## Code Project Structure
The code is divided in 4 main folders:
#### 1. Clustered_df_Generator
 -- Here is the code  used to generated the clustered_df.csv that has the clusters for all the books (using a Kmeans algorithm) in order to perform in the recommender_handler_functions.py file (Inside GUI) the cosine similarity between the elements of the cluster.
#### 2. Data
-- All the dataframes used across the project, but the principals are:
         i.final_df.csv: all the book features
        ii.clustered_df.csv: csv containing the books clusters
        iii. users.csv: Mock DB used to store the users information
#### 3.EDA
 -- Contains two ipynb files that were used to explore the data and generate the final_df.csv
#### 4, GUI
    a) Contains a file for each window, in each file it contains a class per window with its constructor and “callback methods”
      i.start_page.py: login window
      ii.RegistrationWindow.py: Create Account Page
      iii.main_page.py: main window
      iv.BooksRead.py: Search Page
      v.Chat.py: Chat Page
      vi.Rating.py: Top 500 books by average rating
      vii.AccountWindow.py: Account Page
      viii.Info.py : Info Page
    b) We defined two helper classes
      1. recommender_funcs.py: for the functions to compute the recommendations used in Chat.py. It has its test file: test_recommender_funcs.py
      2. user_handler_functions.py: for the helper functions to load the user information session and also handle the books read process. It has its test tile test_user_handler_functions.py
    c) And 3 auxiliary files:
      i. run.py: to execute the code
      ii. paths.py: auxiliary code to change the three used csv files depending if it run in windows or mac.
      iii. palette.py: similar to an css style file, but the palette of colors used across the project.

## How to run it

### Windows
1. Go to path.py and make sure the windows paths are not commented and mac ones are.
2. While standing in the root directory of the project run: python .\\GUI\\run.py. Otherwise the relative directories of the csv files will not work.

### Mac
1. Go to path.py and make sure the mac paths are not commented and window ones are
2. While standing in the GUI directory of the project run: python run.py. Otherwise the relative directories of the csv files will not work.

