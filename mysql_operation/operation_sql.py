"""
install mysql_module:
pip install mysql
"""
import MySQLdb

con = MySQLdb.connect(host='localhost', user='root',
                      passwd='root56&*', db='mydb_one',
                      port=3306, charset='utf-8')
cur = con.cursor()
cur.execute('create table person (id int not null auto_increment primary key,name varchar(20),age int)')
