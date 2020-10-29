import json
from blog.models import Post


class PostSeeds:

    @staticmethod
    def data_seeds_from_file():
        with open('../../posts.json') as f:
            data_json = json.load(f)
        return data_json

    def seeds_to_post(self):
        data_json = self.data_seeds_from_file()
        posts = Post.objects.all()
        print(posts)

#
# seeds = PostSeeds()
# seeds.seeds_to_post()

