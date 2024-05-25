import configparser as cfp
import os

cnf_path = './replica.my.cnf'

def load_cnf():
    cnf = cfp.ConfigParser()
    cnf.read(cnf_path)
    return cnf

cnf = load_cnf()
if not os.environ.get( 'TOOLFORGE' ):
    remote = '127.0.0.1'
    user = cnf['client']['user']
    password = cnf['client']['password']
else:
    remote = 'enwiki.db.svc.wikimedia.cloud'
    user = os.environ.get( 'TOOL_REPLICA_USER' )
    password = os.environ.get( 'TOOL_REPLICA_PASSWORD' )


config = {
    'host': remote,
    'username': "s53922",
    'password': "ai5Ndjkm58nSS460"
}