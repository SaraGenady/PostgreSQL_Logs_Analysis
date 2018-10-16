# import psycopg2 #
import psycopg2
# connect db news #
conn= psycopg2.connect(database="news")
# init cursor #
c = conn.cursor()

# What are the most popular three articles of all time? 
c.execute("""select articles.title, count(*) as views_num from log,articles where log.status='200 OK' and articles.slug = substr(log.path, 10) group by log.path,articles.title order by views_num desc limit 3""")
top_three_articles=c.fetchall()
# Print question
print("What are the most popular three articles of all time?")
# Loop on articles and print
for title, views_num in top_three_articles:
     print(" \"{}\" -- {} views".format(title, views_num))

# Who are the most popular article authors of all time?
c.execute("""select authors.name, count(*) as views_num
              from articles, authors, log
              where log.status='200 OK'
              and authors.id = articles.author
              and articles.slug = substr(log.path, 10)
              group by authors.name
              order by views_num desc""")
top_authors =c.fetchall()
# Print question
print("Who are the most popular article authors of all time?")
# Loop on authors and print
for title, views_num in top_authors:
     print(" \"{}\" -- {} views".format(title, views_num))

# On which days did more than 1% of requests lead to errors?
# used limit because it takes more time 
c.execute("""select dateerror,percentage from tb_percentage limit 1 """)
error_requests =c.fetchall()
# Print question
print("On which days did more than 1% of requests lead to errors?")
# Loop on error_requests and print
for dateerror, percentage in error_requests:
     if percentage > 1 :
          print(" \"{}\" -- {} % errors".format(dateerror, percentage))
     else :
          print("Not found")
     


# conn commit #
conn.commit()

# conn close #
conn.close()