"""fills database"""
from cg.models import Post
from cg.scraper import Scraper
from cg.database import Database, db 
from flask_restful import Resource, fields, marshal_with
import json

resource_fields = {
    'title': fields.String,
    'price': fields.String,
}

class Scheduler(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def add_post_to_database(self):
        sc = Scraper()
        sc.get_all_postings_for_item('apa', search_distance='10', postal='V6T1Z4')
        postings = sc.get_postings()

        dtb = Database(db)
        for post in postings:
            post = Post(title=post['title'], price=post['price'])
            dtb.add_single_item(post)

        print(dtb.query_all_from_table(Post))
        return dtb.query_all_from_table(Post)


def delete_table():
    dtb = Database(db)
    dtb.delete_all_rows_from_table(Post)

    
if __name__ == '__main__':
    add_post_to_database()

