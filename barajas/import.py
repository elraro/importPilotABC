import MySQLdb as Mdb

from barajas import queries as queries

# Hardcoded
DB_HOST = "localhost"
DB_USER = "frav"
DB_PASS = "VXxL4UOLvB6wc01Y3Cxi"
DB_NAME = "frav_ABC"
FOLDER = "/home/alberto/piloto_algeciras/"

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

cur.execute(queries.create_data_table_calidad())
cur.execute(queries.create_data_table_completados())
con.commit()


def insert_data(file, con, cur, completados=True):
    with open(file) as f:
        print("Leyendo " + file)
        lines = f.readlines()
        data = lines[1:]  # remove first 1 elements
        for line in data:
            l = line.replace("\n", "").split(";")
            if completados:
                query = queries.generate_query_completados()
            else:
                query = queries.generate_query_calidad()
            try:
                cur.execute(query, l)
                con.commit()
            except Exception as e:
                print("Error en completados=" + str(completados))
                print(l)
                print(query)
                print("Error: " + str(e))
                con.rollback()


insert_data(FOLDER + "InformeCalidad.csv", con, cur, False)
insert_data(FOLDER + "InformeCompletados.csv", con, cur)