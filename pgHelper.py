import psycopg2
from qgis.core import *

class pgHelper:
    def __init__(self, host="localhost", port="5432", database=None, user=None, passw=None ):
        self.host =host
        self.port = str(port)
        self.database = database
        self.user = user
        self.passw = passw
        try:
            self.con = psycopg2.connect(database=database, user=user, password=passw, host=host, port=port)
        except TypeError:
            self.con = psycopg2.connect(database=database, user=user, password=passw, host=host)
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()

    def listField(self, table, field, schema='public'):
        sql = """SELECT DISTINCT "{1}" FROM {2}."{0}"
                 ORDER BY "{1}" """.format(table, field, schema)
        self.cur.execute(sql)
        return [n[0] for n in self.cur.fetchall()]

    def listGeoLayers(self, schema='public' ):
        sql= """SELECT DISTINCT table_name
            FROM  information_schema.columns
            WHERE table_schema = '{0}' and udt_name = 'geometry'""".format(schema)
        self.cur.execute(sql)
        return [n[0] for n in self.cur.fetchall()]

    def listSchemas(self):
        sql = "select nspname from pg_catalog.pg_namespace"
        self.cur.execute(sql)
        return [n[0] for n in self.cur.fetchall() 
                if n[0] not in ["pg_toast","pg_temp_1","pg_toast_temp_1","pg_catalog","information_schema"] ]

    def getGeomName(self, table, schema='public'):
        sql= """SELECT DISTINCT column_name
            FROM  information_schema.columns
            WHERE table_schema = '{1}' AND table_name = '{0}'
            AND udt_name = 'geometry'""".format(table, schema)
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if result:
            return  result[0]

    def listTableNames(self, table, schema='public', textFieldOnly=True):
        sql= """SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = '{1}'
                  AND table_name = '{0}'
                  """.format(table, schema)
        if textFieldOnly: sql += " AND ( udt_name LIKE '%char%' OR udt_name = 'text')"
        self.cur.execute(sql)
        return  [n[0] for n in self.cur.fetchall()]


    def spatialWhereClause(self, targetGeom, qryGeom, qryTable, where="1=1", bboxOnly=False, schema='public'):
        if not bboxOnly:
           sql = """ST_Intersects( "{0}" , (
                    SELECT  ST_Collect(
                       ST_SimplifyPreserveTopology( {4}."{2}"."{1}" , 2) )
                    FROM   {4}."{2}"
                    WHERE  {3} )
                 ) """.format(targetGeom, qryGeom, qryTable, where, schema )
        else:
            sql = """ "{0}" && (
                    SELECT ST_Collect( {4}."{2}"."{1}" )
                    FROM   {4}."{2}"
                    WHERE  {3} )
                  """.format(targetGeom, qryGeom, qryTable, where, schema )
        return  sql

    def spatialBBOXClause(self, targetGeom, bbox=[], srid=4326 , schema='public'):
        sql = """ {0} && ST_MakeEnvelope([{1}, {2}, {2}, {3}, {4}, {5})
        """.format(targetGeom, bbox[0], bbox[1], bbox[2], bbox[3], srid, schema )
        return  sql

    def loadPostGISLayer(self, table, geomCol="geom", sql="", schema="public"):
        pguri = QgsDataSourceURI()
        pguri.setConnection(self.host, str(self.port), self.database, self.user, self.passw)
        pguri.setDataSource( schema, table, geomCol, sql)

        vlayer = QgsVectorLayer(pguri.uri(),  table, "postgres")
        if not vlayer.isValid():
            raise "Laag " + table + " kan niet worden geladen"
            return
        QgsMapLayerRegistry.instance().addMapLayer(vlayer)

