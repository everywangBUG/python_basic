import pymysql

# 替换掉底层python自带的mySqlDB
pymysql.install_as_MySQLdb()