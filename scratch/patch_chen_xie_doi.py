import os
import re

files_to_update = [
    'BAB_1_Draft_Final.md',
    'BAB_2_Draft_Final.md',
    'OUTLINE_PROPOSAL_REVISI_FINAL.md',
    'scratch/generate_bab1_docx.py',
    'scratch/generate_bab2_docx.py',
    'scratch/generate_proposal_docx.py'
]

# The wrong reference:
wrong_ref_1 = "Chen, T., Guo, Q., Wang, H., Zhang, Q., Ding, C., Zhang, L., & Wu, J. (2024). Identifying influencing factors associated with sleep quality in undergraduates based on partial least squares regression and XGBoost. *Frontiers in Public Health*, 12, 1373504. https://doi.org/10.3389/fpubh.2024.1373504"
wrong_ref_2 = "Chen, T., Guo, Q., Wang, H., Zhang, Q., Ding, C., Zhang, L., & Wu, J. (2024). Identifying influencing factors associated with sleep quality in undergraduates based on partial least squares regression and XGBoost. Frontiers in Public Health, 12, 1373504. https://doi.org/10.3389/fpubh.2024.1373504"
wrong_ref_3 = "Chen, T., Guo, Q., Wang, H., Zhang, Q., Ding, C., Zhang, L., & Wu, J. (2024)."

# The true corrected reference:
correct_ref_md = "Xie, Y., Chen, Y., Han, Y., Zhai, S., Xiao, L., Yin, D., & Chen, Y. (2026). Identifying influencing factors associated with sleep quality in undergraduates based on partial least squares regression and XGBoost. *Frontiers in Psychology*, 16, 1732946. https://doi.org/10.3389/fpsyg.2025.1732946"
correct_ref_plain = "Xie, Y., Chen, Y., Han, Y., Zhai, S., Xiao, L., Yin, D., & Chen, Y. (2026). Identifying influencing factors associated with sleep quality in undergraduates based on partial least squares regression and XGBoost. Frontiers in Psychology, 16, 1732946. https://doi.org/10.3389/fpsyg.2025.1732946"

for fpath in files_to_update:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace wrong references
        updated = content.replace("https://doi.org/10.3389/fpubh.2024.1373504", "https://doi.org/10.3389/fpsyg.2025.1732946")
        updated = updated.replace("Frontiers in Public Health, 12, 1373504", "Frontiers in Psychology, 16, 1732946")
        updated = updated.replace("*Frontiers in Public Health*, 12, 1373504", "*Frontiers in Psychology*, 16, 1732946")
        updated = updated.replace("Chen, T., Guo, Q., Wang, H., Zhang, Q., Ding, C., Zhang, L., & Wu, J. (2024)", "Xie, Y., Chen, Y., Han, Y., Zhai, S., Xiao, L., Yin, D., & Chen, Y. (2026)")
        updated = updated.replace("Chen, T., Guo, Q., Wang, H., Zhang, Q., Ding, C., Zhang, L., & Wu, J. (2024).", "Xie, Y., Chen, Y., Han, Y., Zhai, S., Xiao, L., Yin, D., & Chen, Y. (2026).")
        
        # Replace in-text citations if appropriate:
        # e.g., "Chen et al. (2024)" -> "Xie et al. (2026)"
        updated = updated.replace("Chen et al. (2024)", "Xie et al. (2026)")
        updated = updated.replace("Chen et al. (2024):", "Xie et al. (2026):")
        
        # In BAB 2 status note for this entry:
        updated = updated.replace("[Status di Berkas: Rujukan SOTA Utama - Tersedia Dokumen Ringkasan]", "[Status di Berkas: Tersedia di folder jurnal/Xie_Chen_2026_Sleep_Quality_PLSR_XGBoost.pdf]")

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"[OK] Patched {fpath}")
