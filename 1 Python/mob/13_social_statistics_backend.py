
import json
import random
from faker import Faker
from flask import Flask


app = Flask(__name__)
faker = Faker()

# functions for generating fake posts =======================================

# generate fake posts
def generate_posts():
    num_comments = random.randint(50, 100)
    num_users = random.randint(10, 20)
    users = [faker.word() + str(faker.random_int()) for _ in range(num_users)]
    posts = []
    for i in range(num_comments):
        posts.append({
            'id': i,
            'user': random.choice(users),
            'title': ' '.join([faker.word().title() for _ in range(5)]),
            'text': faker.text(),
            'upvotes': random.randint(1, 200),
            'comments': generate_comments(users, 1)
        })
    data = {
        'users': users,
        'posts': posts
    }
    return data

# generate fake comments for posts
def generate_comments(users, depth):
    n_children = random.randint(0,10)//depth
    comments = []
    for i in range(n_children):
        child_comments = generate_comments(users, depth+1)
        comments.append({
            'user': random.choice(users),
            'text': faker.text(),
            'upvotes': random.randint(1, 100),
            'comments': child_comments,
        })
    return comments



# API endpoints ==========================

# get a list of users
@app.route('/users/')
def users():
    return { 'users': post_data['users'] }

# get a list of posts
@app.route('/posts/')
def posts():
    output = []
    for post in post_data['posts']:
        output.append({
            'id': post['id'],
            'user': post['user'],
            'text': post['text'],
            'upvotes': post['upvotes']
        })
    return {'posts': output}

# get the details for a post (including comments)
@app.route('/posts/<int:post_id>/')
def post_detail(post_id):
    for post in post_data['posts']:
        if post['id'] == post_id:
            return post
    return {}

post_data = generate_posts()

with open('social.json', 'w') as file:
    file.write(json.dumps(post_data, indent=4))

# print(json.dumps(post_data, indent=4))

app.run(debug=True)