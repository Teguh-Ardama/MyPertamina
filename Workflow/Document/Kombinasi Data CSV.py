import itertools
import pandas as pd

# Daftar elemen dalam setiap kolom
booking_branch = ["KC BOGOR CIBINONG", "KCP DEPOK SAWANGAN RAYA", "KC BOGOR PAJAJARAN BANTARJATI", "KCP BOGOR AHMAD YANI"]
jenis_pembiayaan = ["New Booking", "Top Up", "Take Over", "Take Over dan Top Up", "Top Up Pelunasan"]
status_kepemilikan_object_mmq = ["Pemohon", "Orang Tua", "Anak", "Mertua", "Pasangan", "Saudara Kandung", "Saudara Kandung Pasangan"]
type_payroll = ["Payroll", "Non Payroll", "Commited to Payroll"]
jenis_kelamin = ["Wanita", "Pria"]
marital_status = ["Tunggal", "Cerai", "Duda/Janda", "Menikah"]
target_market = ["PNS PAYROLL BO 2", "PNS PAYROLL NON BO 2", "PNS NON PAYROLL", "LEMBAGA NEGARA", "BUMN", "BUMD", "SWASTA", "YAYASAN", "RUMAH SAKIT", "AMAL USAHA ORGANISASI ISLAM", "TNI/POLRI", "LAINNYA"]
status_pekerjaan = ["Dokter Spesialis", "Dokter Umum/Gigi", "Bidan", "Perawat", "Lainnya"]
jabatan = ["Dokter Spesialis", "Dokter Umum/Gigi", "Bidan", "Perawat", "Lainnya"]
wholesale_sme_flag = ["No", "Yes"]
jenis_sk = ["SK CPNS", "Lainnya", "SK Pegawai Tetap", "SK Pegawai Tidak Tetap", "SK PNS", "SK Kenaikan Golongan"]
sk_an_pegawai = ["No", "Yes"]
required_insurance = ["Asuransi Jiwa","Asuransi Jiwa + Asuransi PHK", "Asueansi Jiwa + Asuransi Wanprestasi + Asuransi PHK"]
insurance_product = ["Askrindo Syariah", "Askrida Syariah", "Jasindo Syariah", "AL AMIN", "Takaful Keluarga"]

# referral_branch = ["KC BOGOR CIBINONG", "KCP DEPOK SAWANGAN RAYA", "KC BOGOR PAJAJARAN BANTARJATI", "KCP BOGOR AHMAD YANI"]
# source_of_lead = ["Self Generated"]
# tujuan_pembiayaan = ["Refinancing"]
# reporting_name_same_as_KTP = ["False", "True"]
# kode_pos_tersedia_pemohon = ["Ya", "Tidak"]
# tempat_kerja = ["Bea & Cukai Kediri - Kediri",
                # "Bea Cukai- Sby Pelabuhan Tg Perak",
                # "BPKP Pontianak-Pontianak Ngurah Rai(deaktf)",
                # "Lembaga Negara 1",
                # "Angkasa Pura II Supadio - Pontianak",
                # "Coca Cola Dist. Ind.cab Sukabumi-Sukabumi Sudirman",
                # "Yys Mandiri Bina Prestasi -Medan ZA",
                # "Rumah Sakit Karya Bhakti - Bekasi",
                # "Berlian Amal Perkasa - Jakarta",
                # "MARKAS BESAR TENTARA NASIONAL INDONESIA-CILANGKAP(REGRESI E2E)",
                # "Yys Pendidikan Farmasi Nasional-Solo Slamet Riyadi"]
# pic_name = ["PIC Triana"]
# bendahara_name = ["Rina"]
# insurance_product_jiwa_wanprestasi = ["Askrindo Syariah", "Askrida Syariah", "Jasindo Syariah", "AL AMIN", "Takaful Keluarga"]
# insurance_product_jiwa_wanprestasi_phk = ["Askrindo Syariah", "Askrida Syariah", "Jasindo Syariah", "AL AMIN", "Takaful Keluarga"]
# bsi_pricing_category = ["Atribusi Interest Rate"]
# margin_bank_ujroh = ["13.00%"]

# Menghasilkan semua kombinasi
all_combinations = list(itertools.product(booking_branch,
                                          jenis_pembiayaan,
                                          type_payroll,
                                          jenis_kelamin,
                                          marital_status,
                                          target_market,
                                          status_pekerjaan,
                                          jabatan,
                                          wholesale_sme_flag,
                                          jenis_sk,
                                          sk_an_pegawai,
                                          required_insurance,
                                          insurance_product,
                                          ))

combinations_list = []

# Prepare combinations for saving
for i, combination in enumerate(all_combinations[:10000000], start=1):
    combination_str = f"{i}. {', '.join(combination)}"
    combinations_list.append([combination_str])

# Create a DataFrame from the list
df = pd.DataFrame(combinations_list, columns=["Combinations"])

# Save to a CSV file
df.to_csv("combinations.csv", index=False)