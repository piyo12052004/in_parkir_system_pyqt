from db.conection import connect_db


def simpan_data(id_tiket, plat, foto):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        query = """
        INSERT INTO parkir (id_tiket, plat_nomer_kendaraan, photo_kendaraan, jam_masuk,status)
        VALUES (%s, %s, %s, NOW(),%s)
        """

        cursor.execute(query, (id_tiket, plat, foto, 'masuk'))
        conn.commit()

        cursor.close()
        conn.close()

        return True

    except Exception as e:
        print("Error simpan data:", e)
        return False