


import requests


# Part 1 =======================================================================

# Get Latest Post User
# an example function for getting the user of the most recent post
def get_latest_post_user():
    response = requests.get('http://localhost:5000/posts/')
    posts = response.json()['posts']
    return posts[-1]['user']

print(get_latest_post_user()) # situation5839



# Count User Post Upvotes
# returns a dictionary where the keys are the usernames
# and the values are the total number of upvotes they received from posts
def count_user_post_upvotes():
    ...

# print(count_user_post_upvotes()) # {'partner5084': 806, 'space9330': 430, 'green1898': 560, 'whom5856': 89, ...}



# Find Most Upvoted Post
# finds and returns the most upvoted post
def find_most_upvoted_post():
    ...

# print(find_most_upvoted_post()) # {'id': 44, 'text': '...', 'upvotes': 199, 'user': 'whom5856'}



# Part 2 =======================================================================

# Print Comments
# print out all the comments for a given post
def print_comments(post_id):
    response = requests.get(f'http://localhost:5000/posts/{post_id}/')
    post = response.json()
    print(post['user'] + ': ' + post['text'][:40])
    for comment in post['comments']:
        print_comments_recursive(comment, 1)

def print_comments_recursive(comment, depth):
    print('\t'*depth + comment['user'] + ': ' + comment['text'][:40])
    for comment in comment['comments']:
        print_comments_recursive(comment, depth+1)

print_comments(0)


# Count Comment Upvotes
# returns a dictionary where the keys are the usernames
# and the values are the number of comment upvotes they've received
def count_comment_upvotes(post_id):
    ...

#print(count_comment_upvotes(0)) # {'partner5084': 806, 'space9330': 430, 'green1898': 560, 'whom5856': 89, ...}


# Find Most Upvoted Comment
# returns a dictionary representing the comment which has received the most upvotes
def find_most_upvoted_comment(post_id):
    ...

# print(find_most_upvoted_comment(0)) # {'text': '...', 'upvotes': 199, 'user': 'whom5856'}