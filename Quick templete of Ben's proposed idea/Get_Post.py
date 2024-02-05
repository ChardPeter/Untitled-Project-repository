# Python code Getting user post using api's

import requests

def get_user_posts(username):
    url = f"https://api.example.com/posts?user={username}"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"Post ID: {post['id']}, Content: {post['content']}")
    else:
        print(f"Error fetching posts for user {username}")

# Example usage
get_user_posts("alice")

# Posting a comment under user post

def add_comment(post_id, comment_text):
    # Assuming you have an API endpoint to add comments
    url = f"https://api.example.com/posts/{post_id}/comments"
    data = {"text": comment_text}
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("Comment added successfully!")
    else:
        print("Error adding comment.")

# Example usage
add_comment(123, "Great post, Alice!")
