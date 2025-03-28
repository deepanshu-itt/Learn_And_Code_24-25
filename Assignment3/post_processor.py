class PostProcessor:

    @staticmethod
    def process_posts(posts: list, start_range: int):
        for i, post in enumerate(posts):
            post_number = start_range + i
            if 'photos' in post:
                for j, photo in enumerate(post['photos']):
                    image_url = photo.get('photo-url-1280') or photo.get('photo-url-640') or photo.get('photo-url-500')
                    if image_url:
                        print(f"{post_number}. {image_url}")
            elif 'photo-url' in post:
                image_url = post['photo-url']
                print(f"{post_number}. {image_url}")
            else:
                print(f"{post_number}. No images found")