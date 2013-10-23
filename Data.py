#coding=utf-8
'''
Created on 2013-10-22

@author: maisonwan
'''
import os
import sqlite3

class LoggerData():
    cur = None
    db = None
    def __init__(self):
        self.db = sqlite3.connect(os.getcwd() + "\\system_event.db")
        self.cur = self.db.cursor()
        self.cur.execute("create table if not exists event (id integer primary key autoincrement, state integer, event_time datetime not null)")
    
    def __del__(self):
        self.cur.close()
        
    def add(self, eventType):
        self.cur.execute("insert into event (state, event_time) values(%d, datetime('now', 'localtime'))" % eventType)
        self.db.commit()
    
    # 得到今天的列表
    def get_today_all_events(self):
        self.cur.execute("select * from event where strftime('%Y-%m-%d', event_time) = date()")
        return self.cur.fetchall()
        
    # 得到今天的列表
    def get_today_events(self, eventType):
        self.cur.execute("select * from event where strftime('%%Y-%%m-%%d', event_time) = date() and state = %d" % eventType)
        return self.cur.fetchall()
        
    '''
        测试
    '''
    def test(self):
#        self.cur.execute("insert into catalog (pid, name) values(0, 'name1')")
#        self.cur.execute("insert into catalog (pid, name) values(1, 'name2')")
#        self.cur.execute("insert into catalog (pid, name) values(2, 'name3')")
#        self.cur.execute("insert into catalog (pid, name) values(3, 'name4')")
#        self.cur.execute("insert into catalog (pid, name) values(4, 'name5')")
#        self.db.commit()
        
        self.cur.execute("select * from event")
        print self.cur.fetchall()
        
