from blog import Blog

def user_input_blog_name_range():
    blog_name = input("Enter the Tumblr blog name:\n")
    blog_range = input("Enter the range:\n")
    start_range, end_range = map(int, blog_range.split('-'))
    return blog_name, start_range, end_range


def is_valid_input(start_range: int, end_range: int):
    try:
        if start_range < 1 or end_range < start_range:
            raise ValueError("Invalid range. Start must be >= 1 and end must be >= start.")
    except ValueError as e:
        print(f"Invalid range format: {e}")
        exit()


if __name__ == "__main__":
    blog_name, start_range, end_range = user_input_blog_name_range()

    is_valid_input(start_range, end_range)

    Blog.get_tumblr_blog_info(blog_name, start_range, end_range)
