from tumblr_api  import TumblrAPI
from post_processor import PostProcessor


class Blog:

    def __init__(self, title: str, name: str, description: str, total_posts: int):
        self.title = title
        self.name = name
        self.description = description
        self.total_posts = total_posts


    @staticmethod
    def get_tumblr_blog_info(blog_name: str, start_range: int, end_range: int):

        api_url = TumblrAPI.create_api_url(blog_name, start_range, end_range)

        try:
            blog_json_data = TumblrAPI.fetch_data(api_url)


            blog = Blog(
                title = blog_json_data['tumblelog']['title'],
                name = blog_json_data['tumblelog']['name'],
                description = blog_json_data['tumblelog']['description'],
                total_posts = blog_json_data['posts-total']
            )

            blog.print_blog_details()

            PostProcessor.process_posts(blog_json_data.get('posts', []), start_range)

        except RuntimeError as e:
            print(f"An error occurred: {e}")


    def print_blog_details(self):
        print(f"Blog Title: {self.title}")
        print(f"Blog Name: {self.name}")
        print(f"Blog Description: {self.description}")
        print(f"Total Blog Posts: {self.total_posts}")
