#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==========================================================
  CÔNG CỤ THÊM GAME CARO VÀO APK
  Chạy script này để tạo game_data.js từ file blogger HTML
==========================================================

Cách dùng:
  1. Copy file HTML bài đăng blogger của bạn vào cùng thư mục này
     (hoặc bất kỳ đâu và chỉnh đường dẫn bên dưới)
  2. Chạy: python THEM_GAME.py
  3. Script tự động tạo game_data.js
  4. Build APK bình thường

"""

import re
import os
import sys

def extract_b64_from_blogger_html(html_content):
    """Trích xuất chuỗi b64 từ HTML bài đăng blogger"""
    # Tìm pattern: var b64 = "..." hoặc var b64="..."
    patterns = [
        r'var\s+b64\s*=\s*"([A-Za-z0-9+/=]+(?:"[+\s]*"[A-Za-z0-9+/=]*)*)"',
        r'var b64_?\s*=\s*"([^"]+)"',
        r'"b64"\s*:\s*"([A-Za-z0-9+/=]+)"',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, html_content, re.DOTALL)
        if match:
            # Ghép các chunk nếu b64 bị chia nhỏ
            raw = match.group(1)
            # Xóa dấu nháy kép và dấu + giữa các chunk
            b64 = re.sub(r'"\s*\+\s*"', '', raw)
            b64 = b64.replace('"', '').replace(' ', '').replace('\n', '')
            return b64
    return None

def main():
    print("=" * 60)
    print("  CÔNG CỤ THÊM GAME CARO VÀO APK")
    print("=" * 60)
    print()
    
    # Tìm file HTML blogger
    html_file = None
    
    # Tự động tìm file .html trong thư mục hiện tại
    for f in os.listdir('.'):
        if f.endswith('.html') and f != 'game.html':
            print(f"  Tìm thấy file: {f}")
            choice = input("  Dùng file này? (y/n): ").strip().lower()
            if choice == 'y':
                html_file = f
                break
    
    if not html_file:
        html_file = input("\n  Nhập đường dẫn file HTML blogger: ").strip()
        if not os.path.exists(html_file):
            print(f"\n  LỖI: Không tìm thấy file '{html_file}'")
            input("\n  Nhấn Enter để thoát...")
            sys.exit(1)
    
    print(f"\n  Đang đọc file: {html_file}")
    
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        html_content = f.read()
    
    print(f"  Kích thước file: {len(html_content):,} bytes")
    
    # Trích xuất b64
    print("\n  Đang tìm dữ liệu game (b64)...")
    b64 = extract_b64_from_blogger_html(html_content)
    
    if not b64:
        # Thử tìm thủ công
        print("  Không tìm thấy tự động. Đang thử tìm thủ công...")
        idx = html_content.find('var b64')
        if idx == -1:
            idx = html_content.find('b64 =')
        if idx != -1:
            snippet = html_content[idx:idx+200]
            print(f"  Tìm thấy đoạn: {snippet[:100]}...")
            # Manual extract
            start = html_content.find('"', idx) + 1
            end = html_content.find('";', start)
            if end == -1:
                end = html_content.find('")', start)
            if start > 0 and end > start:
                b64 = html_content[start:end]
        
    if not b64:
        print("\n  LỖI: Không tìm thấy dữ liệu game b64!")
        print("  Hãy chắc chắn đây là file HTML bài đăng blogger chứa game Caro.")
        input("\n  Nhấn Enter để thoát...")
        sys.exit(1)
    
    print(f"  ✅ Tìm thấy! Độ dài b64: {len(b64):,} ký tự")
    
    # Kiểm tra b64 hợp lệ
    import base64
    try:
        padded = b64 + "=" * (4 - len(b64) % 4)
        decoded = base64.b64decode(padded)
        print(f"  ✅ B64 hợp lệ! Game HTML: {len(decoded):,} bytes")
        if b'<!DOCTYPE' in decoded[:50] or b'<html' in decoded[:50]:
            print("  ✅ Xác nhận đây là file game HTML!")
        else:
            print("  ⚠️  Cảnh báo: Nội dung có thể không phải HTML game")
    except Exception as e:
        print(f"  ⚠️  Cảnh báo: {e}")
    
    # Ghi ra game_data.js
    output_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'app', 'src', 'main', 'assets', 'game_data.js'
    )
    
    print(f"\n  Đang ghi file: {output_path}")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f'var GAME_B64="{b64}";')
    
    size_kb = os.path.getsize(output_path) / 1024
    print(f"  ✅ Ghi xong! Kích thước: {size_kb:.1f} KB")
    
    print("\n" + "=" * 60)
    print("  XONG! Bây giờ mở Android Studio và Build APK.")
    print("=" * 60)
    input("\n  Nhấn Enter để thoát...")

if __name__ == '__main__':
    main()
