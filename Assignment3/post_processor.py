class PostProcessor:

    @staticmethod
    def process_posts(posts: list, start_range: int):
        for post_index, post in enumerate(posts):
            post_number = start_range + post_index
            PostProcessor.get_image_url(post_number, post)
    

    @staticmethod
    def get_image_url(post_number, post):
        if 'photos' in post:
            for photo_index, photo in enumerate(post['photos']):
                image_url = (
                photo.get('photo-url-1280') or 
                photo.get('photo-url-640') or 
                photo.get('photo-url-500')
            )
                PostProcessor.is_image_url_exist(image_url, post_number)
                
        elif 'photo-url' in post:
            PostProcessor.is_image_url_exist(image_url, post_number)

        else:
            PostProcessor.print_image_url(post_number)


    @staticmethod
    def is_image_url_exist(image_url, post_number):
        if image_url:
            PostProcessor.print_image_url(post_number, image_url)
        else:
            print("no url exist.")


    @staticmethod 
    def print_image_url(post_number, image_url = "No images found"):
        print(f"{post_number}. {image_url}")
