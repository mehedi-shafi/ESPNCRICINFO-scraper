#imports
import sqlite3 as sqlite



class databaseHandler:
    
    def __init__(self, dbname):
        self.con  sqlite.connect(dbname)
    
    def __del__(self):
        self.con.close()

    def dbCommit(self):
        self.con.commit()

    def createTables(self):
        self.con.execute('create table players(playerId, name, country)')
        self.con.execute('create table t20 (playerId, bft20s_match,	bft20s_innings,	bft20s_no,	bft20s_runs, bft20s_hs,	bft20s_ave,	bft20s_bf,	bft20s_sr,	bft20s_100,	bft20s_50,	bft20s_4, bft20s_6,	bft20s_ct, bft20s_st, bwt20s_match, bwt20s_innings, bwt20s_balls, bwt20s_runs, bwt20s_wkts, bwt20s_bbi, bwt20s_bbm, bwt20s_ave, bwt20s_econ, bwt20s_sr, bwt20s_4w, bwt20s_5w, bwt20s_10w)')
        self.con.execute('create table odi (playerId, bfodi_match, bfodi_innings, bfodi_no, bfodi_runs,	bfodi_hs, bfodi_ave, bfodi_bf, bfodi_sr, bfodi_100, bfodi_50, bfodi_4, bfodi_6, bfodi_ct, bfodi_st, bwodi_match, bwodi_innings, bwodi_balls, bwodi_runs, bwodi_wkts, bwodi_bbi, bwodi_bbm, bwodi_ave, bwodi_econ, bwodi_sr, bwodi_4w, bwodi_5w, 10, bwodi_10w)')
        
        
