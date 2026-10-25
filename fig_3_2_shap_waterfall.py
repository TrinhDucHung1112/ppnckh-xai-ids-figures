# Hình 3.2 - Vẽ lại Figure 3 (trang 11/41): SHAP waterfall, RF, mẫu DoS, RoEduNet-SIMARGL2021
# DỮ LIỆU: đọc từ các nhãn số trong hình gốc (làm tròn 2 chữ số) -> sai số làm tròn khoảng ±0.01
import matplotlib.pyplot as plt

base = 0.334  # E[f(X)] ghi trên hình gốc
# (nhãn, giá trị đặc trưng chuẩn hóa min-max, đóng góp SHAP) theo thứ tự từ trên xuống như hình gốc
rows = [("TCP_WIN_MAX_IN", "0.98", -0.18), ("TCP_WIN_MIN_IN", "0.98", -0.13),
        ("TCP_WIN_SCALE_IN", "0.5", -0.08), ("TCP_WIN_MAX_OUT", "0", +0.02),
        ("TCP_WIN_MIN_OUT", "0", +0.01), ("FLOW_DURATION_MILLISECONDS", "0.008", +0.01),
        ("TCP_FLAGS", "0.008", +0.01), ("SRC_TOS", "0", 0.0), ("DST_TOS", "0", 0.0),
        ("9 đặc trưng còn lại", "", 0.0)]

# Waterfall của SHAP cộng dồn từ DƯỚI lên: bắt đầu ở E[f(X)], kết thúc ở f(x)
cum = base
bars = []
for name, val, c in reversed(rows):
    bars.append((name, val, c, cum, cum + c))
    cum += c
bars = list(reversed(bars))

fig, ax = plt.subplots(figsize=(10, 5.6))
n = len(bars)
for i, (name, val, c, start, end) in enumerate(bars):
    y = n - 1 - i
    color = "#e91e63" if c > 0 else ("#1e88e5" if c < 0 else "#9e9e9e")
    ax.barh(y, end - start, left=start, color=color, height=0.6)
    sign = f"{c:+.2f}" if c != 0 else "≈0"
    ax.text(max(start, end) + 0.006, y, sign, va="center", fontsize=8, color=color)
ax.set_yticks(range(n))
ax.set_yticklabels([f"{v} = {nm}" if v else nm for nm, v, *_ in reversed(bars)][::-1][::-1], fontsize=8)
ax.set_yticklabels([f"{v} = {nm}" if v else nm for nm, v, *_ in bars][::-1], fontsize=8)
ax.axvline(base, ls="--", color="gray", lw=0.8)
ax.axvline(cum, ls="--", color="gray", lw=0.8)
ax.text(base, -0.9, f"E[f(X)] = {base}", ha="center", fontsize=8, color="gray")
ax.text(cum, n - 0.35, f"f(x) ≈ {cum:.3f} (hình gốc ghi f(x) = 0)", ha="left", fontsize=8, color="gray")
ax.set_xlim(-0.05, 0.5); ax.set_ylim(-1.2, n)
ax.set_xlabel("Đầu ra của mô hình cho lớp được giải thích")
ax.set_title("SHAP waterfall – Random Forest, 1 mẫu DoS, RoEduNet-SIMARGL2021 (vẽ lại)", fontsize=10)
fig.text(0.01, 0.005, "Nguồn: vẽ lại từ Figure 3, Arreche, Guntur & Abdallah (2024), Appl. Sci. 14(10), 4170, tr. 11/41. "
         "Hồng: đóng góp dương (sang phải); xanh: đóng góp âm (sang trái). Số liệu đọc từ nhãn hình gốc, đã làm tròn.",
         fontsize=6.5, color="#555555")
plt.tight_layout(rect=(0, 0.03, 1, 1))
plt.savefig("../Hinh_3_2_shap_waterfall.png", dpi=200)
