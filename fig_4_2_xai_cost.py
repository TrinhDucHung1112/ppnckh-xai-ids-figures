# Hình 4.2 (HÌNH MỚI) - Chi phí sinh giải thích SHAP theo số mẫu và so sánh thời gian giải thích cục bộ SHAP vs LIME
# Nguồn: Table 15 (Arreche et al., 2024, tr. 23/41). Đơn vị gốc: giờ (SHAP toàn cục), phút (cục bộ).
import matplotlib.pyplot as plt
n = [100, 500, 2500, 10000]
shap_h = {"RF":[.001,.002,.011,.046], "DNN":[.001,.004,.029,.306], "LightGBM":[.001,.001,.002,.006],
          "MLP":[.014,.925,21.18,385.0], "ADA":[.129,3.557,99.00,1512], "SVM":[.041,.841,20.87,343.0],
          "KNN":[1.104,28.33,706.0,1654]}
models = list(shap_h)
lime_local = [.351,.311,.294,.284,.294,.306,.357]   # theo thứ tự RF, DNN, LGBM, MLP, ADA, SVM, KNN (phút)
shap_local = [.001]*7

fig, (a, b) = plt.subplots(1, 2, figsize=(12, 4.6))
for m, v in shap_h.items():
    a.plot(n, v, marker="o", label=m)
a.set_xscale("log"); a.set_yscale("log")
a.axhline(1, color="gray", ls=":", lw=1); a.text(105, 1.3, "1 giờ", fontsize=8, color="gray")
a.axhline(24, color="gray", ls=":", lw=1); a.text(105, 31, "24 giờ", fontsize=8, color="gray")
a.set_xlabel("Số mẫu cần giải thích"); a.set_ylabel("Thời gian SHAP (giờ, thang log)")
a.set_title("(a) Chi phí SHAP toàn cục theo số mẫu", fontsize=10); a.legend(fontsize=8, ncol=2)

import numpy as np
x = np.arange(7); w = 0.38
order = ["RF","DNN","LightGBM","MLP","ADA","SVM","KNN"]
b.bar(x - w/2, shap_local, w, label="SHAP cục bộ")
b.bar(x + w/2, lime_local, w, label="LIME cục bộ")
b.set_yscale("log"); b.set_xticks(x); b.set_xticklabels(order, fontsize=8)
b.set_ylabel("Thời gian / 1 giải thích (phút, thang log)")
b.set_title("(b) Giải thích cục bộ: SHAP vs LIME", fontsize=10); b.legend(fontsize=8)
fig.text(0.01, 0.005, "Nguồn: tự vẽ từ Table 15, Arreche et al. (2024), tr. 23/41. Các ô lớn (vd. 1512 giờ) có thể là ước lượng (bài báo nói một số thí nghiệm không chạy xong).",
         fontsize=7, color="#555555")
plt.tight_layout(rect=(0, 0.03, 1, 1))
plt.savefig("../Hinh_4_2_chi_phi_XAI.png", dpi=200)
