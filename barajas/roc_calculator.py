import MySQLdb as Mdb
import numpy as np
import sys
import matplotlib.pyplot as plt

# Hardcoded
DB_HOST = "localhost"
DB_USER = "frav"
DB_PASS = "VXxL4UOLvB6wc01Y3Cxi"
DB_NAME = "piloto_barajas"

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

cur.execute("SELECT `ScoreReconocimientoFacialVivoChip` FROM `completados`;")
data = cur.fetchall()
data = np.asarray(data)

fn_rate = np.empty(shape=0)
tp_rate = np.empty(shape=0)
eer_dif = sys.maxsize
eer = 0
x = [0, 1]

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'cm'
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.figure()

for umbral in np.arange(0, 100.1, 0.1):
    tp = 0
    fn = 0
    for d in data:
        if d[0] >= umbral:
            tp += 1
        else:
            fn += 1
    try:
        fn_rate_eer = fn / (fn + tp)
    except ZeroDivisionError:
        fn_rate_eer = 1
    try:
        tp_rate_eer = tp / (tp + fn)
    except ZeroDivisionError:
        tp_rate_eer = 1
    print(fn_rate_eer)
    print(tp_rate_eer)
    fn_rate = np.append(fn_rate, fn_rate_eer)
    tp_rate = np.append(tp_rate, tp_rate_eer)
    if abs(tp_rate_eer - fn_rate_eer) < eer_dif:
        eer_dif = abs(tp_rate_eer - fn_rate_eer)
        eer = (tp_rate_eer + fn_rate_eer) / 2

plt.plot(x, x, linestyle="dashed", color="red", linewidth=1)
plt.plot(fn_rate, tp_rate, linewidth=1, color="blue", alpha=0.5)
plt.xlabel("False Negative Rate")
plt.ylabel("True Positive Rate")
plt.legend(loc="lower right")
plt.title("eer barajas")
plt.tight_layout()
plt.savefig("eer_barajas.png")
plt.close()
con.close()