# Hình 4.1 (HÌNH MỚI) - Chênh lệch F1: (Top 15 Features) - (All Features), 7 mô hình x 3 tập dữ liệu
# Nguồn số liệu: cột F1 của Table 6, Table 7, Table 8 trong Arreche et al. (2024). Không có số liệu tự tạo.
import numpy as np, matplotlib.pyplot as plt
models = ["RF", "ADA", "DNN", "SVM", "KNN", "MLP", "LightGBM"]
# (F1 Top15, F1 All)
t6 = [(.99,.99),(.89,.56),(.99,.99),(.99,.63),(.99,.62),(.99,.99),(.55,.99)]   # RoEduNet-SIMARGL2021
t7 = [(.93,.98),(.99,.89),(.83,.94),(.91,.87),(.97,.97),(.91,.98),(.94,.95)]   # CICIDS-2017
t8 = [(.43,.36),(.31,.21),(.48,.46),(.41,.43),(.34,.73),(.37,.72),(.48,.37)]   # NSL-KDD
data = np.array([[a-b for a,b in t] for t in (t6, t7, t8)])
names = ["RoEduNet-\nSIMARGL2021 (Bảng 6)", "CICIDS-2017\n(Bảng 7)", "NSL-KDD\n(Bảng 8)"]

fig, ax = plt.subplots(figsize=(9, 3.8))
im = ax.imshow(data, cmap="RdBu", vmin=-0.5, vmax=0.5, aspect="auto")
ax.set_xticks(range(7)); ax.set_xticklabels(models)
ax.set_yticks(range(3)); ax.set_yticklabels(names, fontsize=8)
for i in range(3):
    for j in range(7):
        ax.text(j, i, f"{data[i,j]:+.2f}", ha="center", va="center", fontsize=9, color=("white" if abs(data[i,j])>0.3 else "black"))
cb = plt.colorbar(im, ax=ax); cb.set_label("ΔF1 = F1(Top 15) − F1(All)")
ax.set_title("Chênh lệch F1 giữa cấu hình Top 15 và All Features (xanh: Top 15 tốt hơn; đỏ: All tốt hơn)", fontsize=9)
fig.text(0.01, 0.005, "Nguồn: tự tổng hợp từ cột F1 của Table 6, 7, 8 (Arreche et al., 2024, tr. 14–15/41). "
         "Lưu ý: F1 của RF/CICIDS-All (0.98) và KNN/MLP NSL-KDD-All (0.73/0.72) có dấu hiệu bất thường trong bảng gốc.",
         fontsize=6.3, color="#555555")
plt.tight_layout(rect=(0, 0.04, 1, 1))
plt.savefig("../Hinh_4_1_delta_F1_heatmap.png", dpi=200)
