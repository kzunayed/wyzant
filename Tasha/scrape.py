# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# vector of column names to be used in a data frame
columnHeaders = ['Title', 'Price', 'Rating', 'Link']

#Create an empty pandas dataframe called "df" with column headers given in the vector columnHeaders
##################
df = pd.DataFrame(columns=columnHeaders)
df
##################


# Create a counter for the while loop to follow, will denote page number in loop
counter = 1

# Create a loop to loop through all the different pages on the webpage
while counter <= 50:

    # Define a dynamic url to get to the next page in every iteration of the while-loop.
    # The variable url should be a string, which changes from iteration to iteration
    # in the way described in the markdown cell above
    #########################
    url = 'http://books.toscrape.com/catalogue/page-' + str(counter) + '.html'
    #########################

    # Use the requests library to send a get-request for the current url
    page = requests.get(url)

    # Use Beautiful Soup library to create a soup object that allows us to parse the html content of the page we got
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find all the tags that contain the information we would like to collect per book using Beautiful Soup find_all method
    # and store them into lists
    price = soup.find_all('p', attrs={'class': 'price_color'})  # p-tags (paragraphs) whose class is named 'price_color'
    title = soup.find_all('h3')  # h3-tags (level 3 headers)
    rating = soup.find_all('p', attrs={'class': 'star-rating'})  # p-tags whose class is named 'star-rating'
    # create a list called 'link' which consists of div-tags (div is one of the html tags), whose class
    # is named 'image_container'; this list should be created in similar fashion as lists price, title and rating
    ##################
    link = soup.find_all('div', attrs={'class': 'image_container'})
    ##################

    # Note: The length of the lists created in the last step are all the same, since those specific tags only exist per book.
    # iterating through the ranges of the list, append each book's information to the dataframe created earlier
    for i in range(len(price)):
        df = df.append({'Title': title[i].a.get('title'), 'Price': price[i].get_text(),
                        'Rating': rating[i].get('class')[1], 'Link': link[i].a.get('href')}, ignore_index=True)

        # Print Counter to ensure loop is running properly, optional
    # print(counter)

    # Increase counter at the end of the loop to change the url during next loop iteration
    counter = counter + 1


# Print the head of the dataframe to sanity check
# print(df.head())


# Print the tail of the dataframe to sanity check (there shold be 1000 observations in total, so the last index is 999)
# print(df.tail())


type(df['Price'][0])


#drop the first character (i.e. symbol £) from all entries of column Price
df['Price'] = df['Price'].str[1:]

#convert the type of Price entries from strings (str) to reals (float)
df['Price'] = df['Price'].astype(float)

# print(df.head(3))


#convert prices from pounds to dollars (change values of Price column by factor of 1.3)
##################
df['Price'] = df['Price'] * 1.3
# print(df.head(3))
##################


#change column name 'Price' into '$Price'
df.rename(columns={'Price':'$Price'})


# Create a data frame df_sorted which consists of data from df, sorted by price
# from the cheapest to the most expensive (i.e. in ascending order)
##################
df_sorted = df.sort_values(by='Price')
##################

#print first 10 rows of the data frame df_sorted (note the index labels, which are from the original data frame)
##################
print(df.head(10))
##################

# Reset the index so that df_sorted is re-indexed 0,1,2,3,... with the new order of the list
df_sorted = df_sorted.reset_index(drop=True)
df_sorted.head(10) #print first 10 rows of df_sorted


# Print the title of the cheapest book
print(df_sorted['Title'][0])

# Print the price of the cheapest book
##################
print(df_sorted['Price'][0])
##################


# Print the title of the most expensive book
##################
print(df_sorted['Title'][999])
##################

# Print the price of the most expensive book
##################
print(df_sorted['Price'][999])
##################


plt.hist(df_sorted['Price'], bins=20, edgecolor='black')  # 20 bins and edgecolor for better visibility
plt.xlabel('Price (in dollars)')
plt.ylabel('Frequency')
plt.title('Histogram of Prices')
plt.show()


# finding the rating frequency distribution (count of books) for all star ratings.
# Rating Distribution found by getting the length of the "list" where the rating value equals the specified rating
print("One Star: " + str(len(df[df['Rating'] == 'One'])))
print("Two Star: " + str(len(df[df['Rating'] == 'Two'])))
print("Three Star: " + str(len(df[df['Rating'] == 'Three'])))
print("Four Star: " + str(len(df[df['Rating'] == 'Four'])))
print("Five Star: " + str(len(df[df['Rating'] == 'Five'])))


# Create a list for the x and y axis labels for a bar plot
x_bar = ['One', 'Two', 'Three', 'Four', 'Five']
y_bar = [len(df[df['Rating'] == 'One']), len(df[df['Rating'] == 'Two']), len(df[df['Rating'] == 'Three']),
        len(df[df['Rating'] == 'Four']), len(df[df['Rating'] == 'Five'])]


# Use matplotlib to plot the bar plot
##################
plt.bar(x_bar, y_bar, color=['red', 'orange', 'yellow', 'green', 'blue'])
##################

# Change the x axis title, y axis title, and main title of plot
plt.xlabel("Star Rating")
plt.ylabel("Number of Books")
plt.title("Number of Books per Rating")

plt.show()  #needed in script files .py (eg in spyder)
