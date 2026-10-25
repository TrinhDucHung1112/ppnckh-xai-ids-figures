# Mã nguồn vẽ hình – Báo cáo giữa kỳ PPNCKH trong CNTT

Mã Python dùng để tạo các hình trong báo cáo phân tích bài báo:

> O. Arreche, T. Guntur, and M. Abdallah, "XAI-IDS: Toward proposing an explainable artificial intelligence framework for enhancing network intrusion detection systems," *Applied Sciences*, vol. 14, no. 10, Art. no. 4170, May 2024, doi: 10.3390/app14104170.

Học phần: Phương pháp nghiên cứu khoa học trong Công nghệ thông tin – Trường Đại học Sài Gòn.

## Các file

| File | Hình trong báo cáo | Nội dung | Nguồn dữ liệu |
|---|---|---|---|
| `fig_3_1_framework.py` | Hình 3.1 | Sơ đồ khung XAI-IDS (vẽ lại và Việt hóa Figure 1) | Cấu trúc sơ đồ, trang 3/41 của bài báo |
| `fig_3_2_shap_waterfall.py` | Hình 3.2 | SHAP waterfall, Random Forest, một mẫu DoS (vẽ lại Figure 3) | Nhãn số trên hình gốc, trang 11/41 (đã làm tròn, sai số khoảng ±0,01) |
| `fig_4_1_delta_f1.py` | Hình 4.1 | Bản đồ nhiệt ΔF1 = F1(Top 15) − F1(All Features) | Cột F1 của Table 6, 7, 8 (trang 14–15/41) |
| `fig_4_2_xai_cost.py` | Hình 4.2 | Chi phí SHAP theo số mẫu; SHAP và LIME ở mức cục bộ | Table 15 (trang 23/41) |

Các file `.png` cùng tên hình là kết quả đã tạo sẵn.

## Cách chạy

Cần Python 3 và hai thư viện:

```
pip install matplotlib numpy
```

Chạy từng file từ thư mục chứa mã:

```
python fig_3_1_framework.py
python fig_3_2_shap_waterfall.py
python fig_4_1_delta_f1.py
python fig_4_2_xai_cost.py
```

Mỗi file lưu ảnh PNG ở thư mục cha (đường dẫn `../Hinh_...png` trong dòng `savefig`). Nếu muốn lưu cùng thư mục với mã, xóa `../` trong dòng đó.

## Lưu ý về dữ liệu

- Toàn bộ số liệu lấy từ bài báo gốc; không có số liệu tự tạo và không huấn luyện lại mô hình.
- Hình 3.2 dùng giá trị đã làm tròn đọc từ hình gốc nên không phải giá trị SHAP chính xác. Muốn có giá trị chính xác cần chạy mã của tác giả bài báo: https://github.com/ogarreche/XAI_NIDS
- Hình 4.2: bài báo ghi chú một số thí nghiệm ở Table 15 không chạy xong, nên các giá trị rất lớn có thể là ước lượng.

## Tác giả

[ĐIỀN: Họ tên – MSSV – lớp]
