import odbc

CONNECTION_STRING="""
Driver={SQL Native Client};
Server=[Insert Server Name Here];
Database=[Insert DB Here];
Trusted_Connection=yes;
"""

def conn():
    return odbc.odbc(CONNECTION_STRING)
