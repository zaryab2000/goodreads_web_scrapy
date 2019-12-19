import sqlite3


class BooksPipeline(object):


	def __init__(self):
		self.create_connection()
		self.create_table()


	def create_connection(self):
		self.conn = sqlite3.connect("HumorBooks.db")
		self.curr = self.conn.cursor()

	def create_table(self):
		self.curr.execute("""DROP TABLE IF EXISTS books_db""")

		self.curr.execute(""" create table books_db(
			bookTitle text,
        	authorName text,
        	rating text,
        	category text
			) 
			""")

	def process_item(self, item, spider):
		self.store(item)
		return item

	def store(self,item):
		self.curr.execute("""insert into books_db values(?,?,?,?)""",(
			item['bookTitle'][0],
			item['authorName'][0],
			item['rating'][0],
			item['category'][0]
        	 ))
		self.conn.commit()



