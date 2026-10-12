import os
import shutil
import subprocess

file_mappings = {
    # 01_Naskah_Proposal_Master
    "PROPOSAL_BAB_1-3_FINAL_SEMPURNA.docx": "01_Naskah_Proposal_Master/PROPOSAL_BAB_1-3_FINAL_SEMPURNA.docx",
    "OUTLINE_PROPOSAL_REVISI_FINAL.docx": "01_Naskah_Proposal_Master/OUTLINE_PROPOSAL_REVISI_FINAL.docx",
    "OUTLINE_PROPOSAL_REVISI_FINAL.md": "01_Naskah_Proposal_Master/OUTLINE_PROPOSAL_REVISI_FINAL.md",
    "PANDUAN_PENGAJUAN_JUDUL_DAN_TANYA_JAWAB_SKRIPSI.docx": "01_Naskah_Proposal_Master/PANDUAN_PENGAJUAN_JUDUL_DAN_TANYA_JAWAB_SKRIPSI.docx",
    "PANDUAN_PENGAJUAN_JUDUL_DAN_TANYA_JAWAB_SKRIPSI.md": "01_Naskah_Proposal_Master/PANDUAN_PENGAJUAN_JUDUL_DAN_TANYA_JAWAB_SKRIPSI.md",

    # 02_Draft_Per_Bab/Bab_1
    "BAB_1_Draft_Final.docx": "02_Draft_Per_Bab/Bab_1/BAB_1_Draft_Final.docx",
    "BAB_1_Draft_Final.md": "02_Draft_Per_Bab/Bab_1/BAB_1_Draft_Final.md",
    "Latar_Belakang_Revisi.md": "02_Draft_Per_Bab/Bab_1/Latar_Belakang_Revisi.md",

    # 02_Draft_Per_Bab/Bab_2
    "BAB_2_Draft_Final.docx": "02_Draft_Per_Bab/Bab_2/BAB_2_Draft_Final.docx",
    "BAB_2_Draft_Final.md": "02_Draft_Per_Bab/Bab_2/BAB_2_Draft_Final.md",
    "BAB_2_Draft_Final_Revisi.docx": "02_Draft_Per_Bab/Bab_2/BAB_2_Draft_Final_Revisi.docx",
    "SOTA_GAP.md": "02_Draft_Per_Bab/Bab_2/SOTA_GAP.md",

    # 02_Draft_Per_Bab/Bab_3
    "BAB_3_Draft_Final.docx": "02_Draft_Per_Bab/Bab_3/BAB_3_Draft_Final.docx",
    "BAB_3_Draft_Final.md": "02_Draft_Per_Bab/Bab_3/BAB_3_Draft_Final.md",
    "BAB_3_Draft_Final_Revisi.docx": "02_Draft_Per_Bab/Bab_3/BAB_3_Draft_Final_Revisi.docx",
    "CRISP-DM.md": "02_Draft_Per_Bab/Bab_3/CRISP-DM.md",
    "Preprocessing.md": "02_Draft_Per_Bab/Bab_3/Preprocessing.md",

    # 03_Catatan_dan_Panduan_Sidang
    "pertanyaan.md": "03_Catatan_dan_Panduan_Sidang/pertanyaan.md",
    "penjelasan_apk.md": "03_Catatan_dan_Panduan_Sidang/penjelasan_apk.md",
    "counter.md": "03_Catatan_dan_Panduan_Sidang/counter.md",
    "k3027_panduan-skripsi.pdf": "03_Catatan_dan_Panduan_Sidang/k3027_panduan-skripsi.pdf",
    "skripsi_softfile_perpus.pdf": "03_Catatan_dan_Panduan_Sidang/skripsi_softfile_perpus.pdf",

    # 04_Eksperimen_dan_Model
    "preprocessing_catboost.ipynb": "04_Eksperimen_dan_Model/preprocessing_catboost.ipynb",
    "debug_notebook.py": "04_Eksperimen_dan_Model/scripts_notebook/debug_notebook.py",
    "update_notebook.py": "04_Eksperimen_dan_Model/scripts_notebook/update_notebook.py",
    "update_notebook_native.py": "04_Eksperimen_dan_Model/scripts_notebook/update_notebook_native.py",
    "update_notebook_pool.py": "04_Eksperimen_dan_Model/scripts_notebook/update_notebook_pool.py",
    "update_notebook_safety.py": "04_Eksperimen_dan_Model/scripts_notebook/update_notebook_safety.py",

    # 05_Arsip_dan_Backup/arsip_outline
    "OUTLINE.docx": "05_Arsip_dan_Backup/arsip_outline/OUTLINE.docx",
    "OUTLINE.pdf": "05_Arsip_dan_Backup/arsip_outline/OUTLINE.pdf",
    "OUTLINE_1438.pdf": "05_Arsip_dan_Backup/arsip_outline/OUTLINE_1438.pdf",
    "OUTLINE_PROPOSAL_1438.docx": "05_Arsip_dan_Backup/arsip_outline/OUTLINE_PROPOSAL_1438.docx",
    "OUTLINE_PROPOSAL_AHMAD NOVIAN.pdf": "05_Arsip_dan_Backup/arsip_outline/OUTLINE_PROPOSAL_AHMAD NOVIAN.pdf",
    "OUTLINE_revisi_1438.pdf": "05_Arsip_dan_Backup/arsip_outline/OUTLINE_revisi_1438.pdf",
    "Proposal_Outline.md": "05_Arsip_dan_Backup/arsip_outline/Proposal_Outline.md",

    # 05_Arsip_dan_Backup/arsip_bab1
    "BAB 1_1438.pdf": "05_Arsip_dan_Backup/arsip_bab1/BAB 1_1438.pdf",
    "BAB 1_1438_backup.docx": "05_Arsip_dan_Backup/arsip_bab1/BAB 1_1438_backup.docx",
    "BAB_1_1438_temp.docx": "05_Arsip_dan_Backup/arsip_bab1/BAB_1_1438_temp.docx",

    # 05_Arsip_dan_Backup/arsip_proposal_temp
    "PROPOSAL BAB 1-3.docx": "05_Arsip_dan_Backup/arsip_proposal_temp/PROPOSAL BAB 1-3.docx",
    "PROPOSAL BAB 1-3.docx.bak": "05_Arsip_dan_Backup/arsip_proposal_temp/PROPOSAL BAB 1-3.docx.bak",
    "PROPOSAL_BAB_1-3_backup_before_perfect_dp.docx": "05_Arsip_dan_Backup/arsip_proposal_temp/PROPOSAL_BAB_1-3_backup_before_perfect_dp.docx",
    "PROPOSAL_BAB_1-3_Revisi.docx": "05_Arsip_dan_Backup/arsip_proposal_temp/PROPOSAL_BAB_1-3_Revisi.docx",
    "temp_inspect_proposal.docx": "05_Arsip_dan_Backup/arsip_proposal_temp/temp_inspect_proposal.docx",
    "temp_work_proposal.docx": "05_Arsip_dan_Backup/arsip_proposal_temp/temp_work_proposal.docx",
}

for src, dst in file_mappings.items():
    if os.path.exists(src):
        # Coba git mv dulu agar riwayat git terjaga
        res = subprocess.run(["git", "mv", src, dst], capture_output=True, text=True)
        if res.returncode != 0:
            # Jika gagal git mv (misal file untracked), pakai shutil.move
            shutil.move(src, dst)
            print(f"[MOVE] {src} -> {dst}")
        else:
            print(f"[GIT-MV] {src} -> {dst}")
    else:
        print(f"[SKIP] {src} tidak ditemukan.")
print("Semua file berhasil dipindahkan!")
