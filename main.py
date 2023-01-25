from bs4 import BeautifulSoup
import requests

website_url = "https://benz-blog.vercel.app"
posts_data = []

response = requests.get(website_url)
benz_blog = response.text
soup = BeautifulSoup(benz_blog, 'html.parser')

post_container = soup.find(class_="lg:col-span-8")
all_posts = post_container.contents

for post in all_posts:
    post_heading = post.h1.getText()
    post_link = website_url + post.h1.a.get("href")
    publication_date = post.contents[2].contents[1].span.getText()
    post_data = {
        "title": post_heading,
        "link": post_link,
        "published": publication_date
    }
    posts_data.append(post_data)

with open("posts.txt", mode="w") as file:
    for post_data in posts_data:
        file.write(f"{post_data['title']} - {post_data['published']}: {post_data['link']}\n")
