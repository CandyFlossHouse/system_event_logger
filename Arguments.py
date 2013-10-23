# coding=utf-8
'''
Created on 2013-10-22

@author: maisonwan
'''
from Data import LoggerData

class LoadArgument():
    __argv = {}
    __logger_data = None
    ARGV_LOGIN = "-i"
    ARGV_LOGOUT = "-o"
    ARGV_PRINT_DATA = "-s"
    
    EVENT_SYSTEM_ON = 0xF1
    EVENT_SYSTEM_OFF = 0xF2
    
    def __init__(self):
        self.__init_db__()
        
    def __del__(self):
        self.__logger_data.__del__()
        
    def process(self, argv):
        print argv
        if argv.login is not None:
            self.__record_state_login()
        elif argv.logout is not None:
            self.__record_state_logout()
        elif argv.show is not None:
            self.print_event_data()
        
    # 初始化数据库
    def __init_db__(self):
        self.__logger_data = LoggerData()
    
    # 验证参数
    def parse_argv(self, arg):
        if len(arg) <= 1:
            self.print_info()
            return
        arg_result = {self.ARGV_LOGIN  : lambda : self.__record_state_login(),
                      self.ARGV_LOGOUT : lambda : self.__record_state_logout(),
                      self.ARGV_PRINT_DATA : lambda :self.print_event_data()}
        if arg[1] not in arg_result.iterkeys():
            self.print_info()
        else:
            return arg_result[arg[1]]()
#        parser = argparse.ArgumentParser(description="System Event Logger")
#        parser.add_argument(self.ARGV_LOGIN,      "--login", nargs="?",  help="login the System Event.")
#        parser.add_argument(self.ARGV_LOGOUT,     "--logout", nargs="?", help="logout the System Event.")
#        parser.add_argument(self.ARGV_PRINT_DATA, "--show", nargs="?",   help="show all the records.")
#        args = parser.parse_args(arg)
#        return args
        
    # 开启的时候
    def __record_state_login(self):
        self.__logger_data.add(self.EVENT_SYSTEM_ON)
        print 'record_state_login...'
        
    # 关闭的时候
    def __record_state_logout(self):
        self.__logger_data.add(self.EVENT_SYSTEM_OFF)
        print 'record_state_logout...'
    
    # 打印数据
    def print_event_data(self):
        events = self.__logger_data.get_today_all_events()
        print '----Show all the records----'
        for e in events:
            print "ID=%d\tState=%s\tTime=%s" % (e[0], self.__get_state(e[1]), e[2])
        print '----End----'
    
    def __get_state(self, state):  
        if state == self.EVENT_SYSTEM_ON:
            return "Login"
        if state == self.EVENT_SYSTEM_OFF:
            return "Logout"
        
    def print_info(self):
        print 'help:'
        print '-i : login the system.'
        print '-o : logout the system.'
        print '-s : show all the records.'
