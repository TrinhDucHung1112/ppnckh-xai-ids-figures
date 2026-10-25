# Hình 3.1 - Vẽ lại Figure 1 (trang 3/41) của Arreche et al. (2024) bằng matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(13, 6.2))
ax.set_xlim(0, 13); ax.set_ylim(0, 6.2); ax.axis("off")

def box(x, y, w, h, text, fc="#ffffff", ec="#333333"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.03,rounding_size=0.12",
                                fc=fc, ec=ec, lw=1.3))
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=7.3)

def group(x, y, w, h, label, color):
    ax.add_patch(plt.Rectangle((x, y), w, h, fill=False, ec=color, lw=1.8, ls="--"))
    ax.text(x + 0.1, y + h + 0.07, label, color=color, fontsize=8.5, fontweight="bold")

def arrow(x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color="#444444", lw=1.2))

# Hàng 1: tiền xử lý + mô hình hộp đen
group(0.2, 4.6, 6.1, 1.2, "TIỀN XỬ LÝ", "#2e7d32")
group(6.5, 4.6, 6.3, 1.2, "MÔ HÌNH HỘP ĐEN (BLACK-BOX AI)", "#111111")
w, h, y = 1.7, 0.8, 4.8
xs = [0.35, 2.25, 4.15, 6.65, 8.55, 10.75]
labels = ["Nạp cơ sở dữ liệu\n(Loading Database)", "Chọn cột đặc trưng\n(Choosing Features)",
          "Chuẩn hóa đặc trưng\n(Feature Normalization)", "Huấn luyện mô hình AI\n(Training AI models)",
          "Kiểm thử mô hình AI\n(Testing AI models)", "Tính chỉ số hiệu năng\n(Performance Measures)"]
fcs = ["#e8f5e9"]*3 + ["#eeeeee"]*3
for x, l, fc in zip(xs, labels, fcs):
    box(x, y, w, h, l, fc)
for i in range(5):
    arrow(xs[i] + w, y + h/2, xs[i+1], y + h/2)

# Hàng 2: XAI toàn cục / cục bộ
group(0.2, 2.75, 5.0, 1.2, "XAI TOÀN CỤC (GLOBAL XAI)", "#b71c1c")
group(5.4, 2.75, 7.4, 1.2, "XAI CỤC BỘ (LOCAL XAI)", "#e53935")
box(0.4, 2.95, 2.2, 0.8, "Tính giá trị SHAP\n(Generating SHAPLEY Values)", "#fdecea")
box(2.85, 2.95, 2.2, 0.8, "Đồ thị SHAP toàn cục\n(SHAP Global Graphs)", "#fdecea")
box(5.6, 2.95, 2.1, 0.8, "Đồ thị SHAP cục bộ\n(SHAP Local Graphs)", "#fdecea")
box(8.1, 2.95, 2.1, 0.8, "Mô hình thay thế LIME\n(LIME Surrogate model)", "#fdecea")
box(10.6, 2.95, 2.0, 0.8, "Giải thích cục bộ LIME\n(LIME Local Explanation)", "#fdecea")
arrow(2.6, 3.35, 2.85, 3.35)   # Shapley -> SHAP global
arrow(10.2, 3.35, 10.6, 3.35)  # LIME surrogate -> LIME local
# Từ "Tính chỉ số hiệu năng" đi xuống một đường chung rồi rẽ tới SHAP và LIME
ax.plot([11.6, 11.6], [4.8, 4.35], color="#444444", lw=1.2)
ax.plot([1.5, 11.6], [4.35, 4.35], color="#444444", lw=1.2)
for xt in (1.5, 6.65, 9.15):
    arrow(xt, 4.35, xt, 3.75)
# Hàng 3: trích xuất đặc trưng & giải thích
group(0.2, 0.5, 12.6, 1.5, "TRÍCH XUẤT ĐẶC TRƯNG VÀ GIẢI THÍCH (FEATURE EXTRACTION & EXPLANATION)", "#1565c0")
labs = ["Đặc trưng nổi bật\ntoàn cục", "Đặc trưng nổi bật\ntheo loại tấn công", "Đặc trưng nổi bật\ntheo mô hình AI",
        "Trực quan hóa đặc trưng\nxâm nhập hàng đầu", "Giải thích đặc trưng\nxâm nhập hàng đầu", "Giải thích quyết định\ncủa mô hình AI"]
xx = [0.35, 2.4, 4.45, 6.5, 8.55, 10.6]
for x, l in zip(xx, labs):
    box(x, 0.75, 1.95, 0.85, l, "#e3f2fd")
arrow(3.95, 2.95, 3.4, 1.6)   # SHAP toàn cục -> trích xuất
arrow(6.6, 2.95, 9.5, 1.6)   # SHAP/LIME cục bộ -> giải thích
arrow(11.6, 2.95, 11.6, 1.6)

ax.text(6.5, 0.15, "Nguồn: vẽ lại và Việt hóa từ Figure 1, Arreche, Guntur & Abdallah (2024), Appl. Sci. 14(10), 4170, tr. 3/41.",
        ha="center", fontsize=7.5, color="#555555")
plt.savefig("../Hinh_3_1_framework.png", dpi=200, bbox_inches="tight")
