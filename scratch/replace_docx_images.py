import zipfile, io, os, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

DOCX_PATH = r"01_Naskah_Proposal_Master\PROPOSAL_BAB_1-3_FINAL_SEMPURNA.docx"
TEMP_PATH = r"01_Naskah_Proposal_Master\PROPOSAL_BAB_1-3_FINAL_SEMPURNA_temp.docx"

IMAGE_REPLACEMENTS = {
    "word/media/image3.png": r"gambar_bab3\Gambar_3_1_CRISP_DM.png",
    "word/media/image5.png": r"gambar_bab3\Gambar_3_5_Alur_Perhitungan_Manual.png",
    "word/media/image6.png": r"gambar_bab3\Gambar_3_6_Matriks_Dan_Bobot_Manual.png",
    "word/media/image8.png": r"gambar_bab3\Gambar_3_3_Mockup_CDSS.png"
}

print("Replacing images inside docx zip archive...")

with zipfile.ZipFile(DOCX_PATH, 'r') as zin:
    with zipfile.ZipFile(TEMP_PATH, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename in IMAGE_REPLACEMENTS:
                new_img_path = IMAGE_REPLACEMENTS[item.filename]
                with open(new_img_path, 'rb') as f_img:
                    img_data = f_img.read()
                zout.writestr(item, img_data)
                print(f"[OK] Replaced {item.filename} with {new_img_path} ({len(img_data)} bytes)")
            else:
                zout.writestr(item, zin.read(item.filename))

os.replace(TEMP_PATH, DOCX_PATH)
print(f"[SUCCESS] Replaced images and saved to {DOCX_PATH}")
