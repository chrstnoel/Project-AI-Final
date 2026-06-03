def logic_compos(label_result):

    for sampah in label_result:
        if sampah in ['plastik', 'logam', 'kaca', 'styrofoam']:
            return{
                "bisa_dikompos" : False,
                "status" : "Gagal",
                "kekurangan": f"Terdeteksi bahan non-organik: {sampah}",
                "solusi": f"Segera pisahkan '{sampah}'!"
            }
        
    if 'kompos_matang' in label_result:
        return{
            "bisa_dikompos": True,
            "status": "Matang Sempurna!",
            "kekurangan": "Tidak ada",
            "solusi": "Kompos sudah siap dipanen!"
        }
    
    ada_hijau = any(x in ['sayur', 'buah', 'daun_hijau'] for x in label_result)
    ada_cokelat = any(x in ['daun_kering', 'kardus', 'ranting'] for x in label_result)

    if 'kompos_basah_busuk' in label_result:
        return{
            "bisa_dikompos" : True,
            "status" : "Kondisi Kurang Baik(Teralu Basah)",
            "kekurangan": "Kurang Oksigen / Teralu Banyak Air",
            "solusi": "Aduk tumpukan"
        }
    
    if "kompos_kering" in label_result:
        return{
            "bisa_dikompos": True,
            "status": "Kondisi teralu kering",
            "kekurangan": "Kurang Air",
            "solusi": "Semprotkan sedikit air"
        }
    
    if ada_hijau and not ada_cokelat:
        return{
            "bisa_dikompos": True,
            "status": "Sedang Diproses",
            "kekurangan": "Kurang Bahan Cokelat",
            "solusi": "Tambahkan daun kering"
        }
    elif ada_cokelat and not ada_hijau:
        return{
            "bisa_dikompos": True,
            "status": "Sedang Diproses",
            "kekurangan": "Kurang Bahan Hijau",
            "solusi": "Tambahkan sisa sayuran dapur"
        }
    
    return{
        "bisa_dikompos": True,
        "status": "🏃 Proses Berjalan Baik",
        "kekurangan": "Tidak ada, rasio sudah seimbang",
        "solusi": "Kondisi tumpukan sudah ideal. Cukup pantau berkala!"
    }

