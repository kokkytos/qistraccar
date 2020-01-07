import ConfigParser
import os
    
config = ConfigParser.ConfigParser()

configFile=os.path.join(os.path.dirname(os.path.realpath(__file__)),"settings.cfg")
config.read(configFile)


QSQLDATABASENAME = config.get('postgresql', 'QSqlDatabaseName')
DBDRIVER = config.get('postgresql', 'dbdriver')
HOST = config.get('postgresql', 'host')
PORT = int(config.get('postgresql', 'port'))
SCHEMA = config.get('postgresql', 'schema')
DBNAME = config.get('postgresql', 'dbname')
USERNAME = config.get('postgresql', 'username')
PASSWORD = config.get('postgresql', 'password')

SQL_DEVICES= config.get('queries', 'sql_devices')
SQL_FUN_POS_DEV_BETWN_DATE = config.get('queries', 'sql_fun_pos_dev_betwn_date')
SQL_FUN_POLYLINE_DEV_BETWN_DATE = config.get('queries', 'sql_fun_polyline_dev_betwn_date')

#==============================================================================================================================         
def write(**kwargs):
    """Write Settings for database"""     
      
    if kwargs is not None:
            for key, value in kwargs.iteritems():
                config.set('postgresql', key, value)
    with open(configFile, 'wb') as configfile:
            config.write(configfile)