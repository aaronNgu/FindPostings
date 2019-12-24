"""fills database"""
from cg.models import Post
from cg.scraper import Scraper
from cg.database import Database, db 
import json

def add_post_to_database():
    sc = Scraper()
    sc.get_all_postings_for_item('apa', search_distance='10',postal='V6T1Z4')
    postings = sc.get_postings()

    dtb = Database(db)
    for post in postings:
        post = Post(title=post['title'],price=['price'])
        dtb.add_single_item(post)
    
    return json.dumps(dtb.query_all_from_table(Post))
    
if __name__ == '__main__':
    add_post_to_database()
    
