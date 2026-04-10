================================================================
     CARO ONLINE - ANDROID PROJECT
     Hướng dẫn từng bước tạo APK
================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 BƯỚC 1: CÀI ANDROID STUDIO (lần đầu, bỏ qua nếu đã cài)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Tải tại: https://developer.android.com/studio
2. Cài đặt bình thường (Next → Next → Finish)
3. Mở lần đầu → để nó tải Android SDK (~1-2GB, mất 10-20 phút)
4. Cài JDK 17 nếu chưa có: https://adoptium.net/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 BƯỚC 2: THÊM GAME VÀO PROJECT  ← LÀM TRƯỚC KHI BUILD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Cách A (tự động - khuyên dùng):
  1. Copy file HTML bài đăng blogger chứa game Caro
     vào cùng thư mục với THEM_GAME.py
  2. Chạy THEM_GAME.py (double-click hoặc: python THEM_GAME.py)
  3. Làm theo hướng dẫn trên màn hình
  4. Script tự tạo file game_data.js ✅

Cách B (thủ công):
  1. Mở file HTML blogger → tìm đoạn:  var b64 = "PCFET0..."
  2. Copy toàn bộ chuỗi dài trong dấu nháy
  3. Mở file: app/src/main/assets/game_data.js
  4. Sửa dòng:  var GAME_B64 = "";
     thành:     var GAME_B64 = "PCFET0...toàn bộ chuỗi...";
  5. Lưu file

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 BƯỚC 3: MỞ PROJECT TRONG ANDROID STUDIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Mở Android Studio
2. Chọn "Open" (KHÔNG phải New Project)
3. Tìm đến thư mục CaroOnline này → Click OK
4. Chờ "Gradle sync" xong (thanh xanh dưới màn hình, ~2-5 phút)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 BƯỚC 4: BUILD APK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Trên menu Android Studio:
  Build  →  Build Bundle(s)/APK(s)  →  Build APK(s)

Chờ ~1-2 phút. Khi xong xuất hiện thông báo:
  "Build successful"  →  Click "locate"

File APK ở: app/build/outputs/apk/debug/app-debug.apk

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 BƯỚC 5: CÀI LÊN ĐIỆN THOẠI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Cách 1 - USB (nhanh nhất):
  a. Điện thoại: Cài đặt → Giới thiệu về điện thoại
     → Tap "Số hiệu bản dựng" 7 lần liên tiếp
  b. Cài đặt → Tùy chọn nhà phát triển
     → Bật "Gỡ lỗi USB" (USB Debugging)
  c. Cắm USB vào máy tính
  d. Android Studio: Nhấn nút ▶️ (Run) màu xanh
  e. Chọn điện thoại của bạn → OK
  f. Game tự cài và mở!

Cách 2 - Copy file APK:
  a. Copy file app-debug.apk vào điện thoại qua USB/Zalo/Drive
  b. Trên điện thoại: mở File Manager
  c. Tìm file APK → Nhấn vào để cài
  d. Cho phép "Cài từ nguồn không xác định"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 CẤU TRÚC PROJECT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CaroOnline/
├── README.txt              ← File này
├── THEM_GAME.py            ← Công cụ thêm game (chạy trước)
├── app/
│   ├── build.gradle
│   ├── src/main/
│   │   ├── AndroidManifest.xml
│   │   ├── assets/
│   │   │   ├── game.html       ← Loader chính
│   │   │   └── game_data.js    ← Dữ liệu game (do THEM_GAME.py tạo)
│   │   ├── java/com/carogame/online/
│   │   │   └── MainActivity.java
│   │   └── res/
│   │       ├── mipmap-*/       ← Icon app
│   │       └── values/
├── build.gradle
├── settings.gradle
└── gradle.properties

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 THÔNG TIN KỸ THUẬT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Package ID : com.carogame.online
Min Android: 5.0 Lollipop (API 21)
Target     : Android 14 (API 34)
Màn hình   : Dọc (Portrait)
Quyền      : Internet (load font/icon), Storage (localStorage)

Tính năng WebView:
 ✅ JavaScript enabled
 ✅ LocalStorage (lưu bảng xếp hạng)
 ✅ Web Audio API (âm thanh)
 ✅ Canvas / WebGL
 ✅ Fullscreen / Immersive mode
 ✅ Hardware acceleration

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 LỖI THƯỜNG GẶP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Gradle sync failed"
  → File → Invalidate Caches → Invalidate and Restart

"SDK not found"
  → Tools → SDK Manager → Install Android SDK

"App chỉ hiện màn hình tối"
  → Chưa chạy THEM_GAME.py. Thêm game_data.js trước.

"Âm thanh không có"
  → Bình thường - Web Audio cần tương tác trước. Nhấn vào game.

================================================================
