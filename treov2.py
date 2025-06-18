import os
import sys
import time
import requests
import json
import re
from datetime import datetime
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from time import sleep

# Mã màu ANSI
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
reset_color = "\033[0m"

# Đánh dấu bản quyền
HĐ_tool = trang + " " + trang + "[" + do + "+_+" + trang + "] " + trang + "=> "
mquang = trang + " " + trang + "[" + do + "÷_+" + trang + "] " + trang + "=> "
thanh = trang + "-------------------------------------------------------------------------"

# Màu cầu vồng
rainbow_colors = [
    "\033[91m",  # Đỏ
    "\033[93m",  # Vàng
    "\033[92m",  # Xanh lá
    "\033[96m",  # Xanh dương nhạt
    "\033[94m",  # Xanh dương
    "\033[95m",  # Tím
    "\033[97m"   # Trắng
]

# Hàm in văn bản với hiệu ứng
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)

# Hàm in khung cầu vồng
def in_dong_khung_cau_vong(text):
    khung_tren = "┌"
    khung_duoi = "└"
    
    for i in range(len(text) + 2):
        khung_tren += rainbow_colors[i % len(rainbow_colors)] + "─" + reset_color
    khung_tren += "┐"
    
    noi_dung = ""
    for i, char in enumerate(text):
        noi_dung += rainbow_colors[i % len(rainbow_colors)] + char
    noi_dung = noi_dung + reset_color
    
    dong_duoc_khung = f"{khung_tren}\n{rainbow_colors[6]}│ {noi_dung} │{reset_color}\n{khung_duoi}"
    print(dong_duoc_khung)

# Hàm in văn bản màu cầu vồng
def in_mau(text):
    noi_dung = ""
    for i, char in enumerate(text):
        noi_dung += rainbow_colors[i % len(rainbow_colors)] + char
    noi_dung += reset_color
    print(noi_dung)

# Hàm xóa màn hình
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Banner
def banner():
    clear_screen()
    banner_text = """
███╗░░░███╗██╗███╗░░██╗██╗░░██╗  ██╗░░░░░░█████╗░██╗
████╗░████║██║████╗░██║██║░░██║  ██║░░░░░██╔══██╗██║
██╔████╔██║██║██╔██╗██║███████║  ██║░░░░░██║░░██║██║
██║╚██╔╝██║██║██║╚████║██╔══██║  ██║░░░░░██║░░██║██║
██║░╚═╝░██║██║██║░╚███║██║░░██║  ███████╗╚█████╔╝██║
╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ╚══════╝░╚════╝░╚═╝
════════════════════════════════════════════════
Tool By: Minh Loi X Tool
[->] Nhóm Zalo: https://zalo.me/g/cebxmw597
[->] Zalo: La Minh Lợi
[->] Facebook: https://www.facebook.com/profile.php?id=100087637635614
[->] Tool By Minh Lợi: Admin La Minh Lợi
════════════════════════════════════════════════
"""
    print(Colorate.Diagonal(Colors.blue_to_cyan, banner_text))

# Khởi động tool
clear_screen()
xoss(f'{xanh_la}[●] Đang Chạy Vào Tool Minh Lợi - Treo Mess........')
xoss(f'{xanhnhat}[●] Kiểm tra server.......')
xoss(f'{vang}[●] Kiểm tra bản update')
xoss(f'{xanh_duong}[●] Thành công, đang tiến hành vào tool')
clear_screen()
banner()

class Messenger:
    def __init__(self, cookie):
        self.cookie = cookie
        self.user_id = self.id_user()
        self.fb_dtsg = None
        self.init_params()

    def id_user(self):
        try:
            c_user = re.search(r"c_user=(\d+)", self.cookie).group(1)
            return c_user
        except:
            raise Exception("Cookie không hợp lệ")

    def init_params(self):
        headers = {
            'Cookie': self.cookie,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate', 
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1'
        }

        try:
            response = requests.get('https://www.facebook.com', headers=headers)
            fb_dtsg_match = re.search(r'"token":"(.*?)"', response.text)
            
            if not fb_dtsg_match:
                response = requests.get('https://mbasic.facebook.com', headers=headers)
                fb_dtsg_match = re.search(r'name="fb_dtsg" value="(.*?)"', response.text)
                
                if not fb_dtsg_match:
                    response = requests.get('https://m.facebook.com', headers=headers)
                    fb_dtsg_match = re.search(r'name="fb_dtsg" value="(.*?)"', response.text)

            if fb_dtsg_match:
                self.fb_dtsg = fb_dtsg_match.group(1)
            else:
                raise Exception("Không thể lấy được fb_dtsg")

        except Exception as e:
            raise Exception(f"Lỗi khi khởi tạo tham số: {str(e)}")

    def gui_tn(self, recipient_id, message):
        timestamp = int(time.time() * 1000)
        offline_threading_id = str(timestamp)
        message_id = str(timestamp)

        data = {
            'thread_fbid': recipient_id,
            'action_type': 'ma-type:user-generated-message',
            'body': message,
            'client': 'mercury',
            'author': f'fbid:{self.user_id}',
            'timestamp': timestamp,
            'source': 'source:chat:web',
            'offline_threading_id': offline_threading_id,
            'message_id': message_id,
            'ephemeral_ttl_mode': '',
            '__user': self.user_id,
            '__a': '1',
            '__req': '1b', 
            '__rev': '1015919737',
            'fb_dtsg': self.fb_dtsg
        }

        headers = {
            'Cookie': self.cookie,
            'User-Agent': 'python-http/0.27.0',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.facebook.com',
            'Host': 'www.facebook.com',
            'Referer': f'https://www.facebook.com/messages/t/{recipient_id}'
        }

        try:
            response = requests.post(
                'https://www.facebook.com/messaging/send/',
                data=data,
                headers=headers
            )
            if response.status_code != 200:
                return {
                    'success': False,
                    'error': 'HTTP_ERROR',
                    'error_description': f'Status code: {response.status_code}'
                }

            if 'for (;;);' in response.text:
                clean_text = response.text.replace('for (;;);', '')
                try:
                    result = json.loads(clean_text)
                    
                    if 'error' in result:
                        return {
                            'success': False,
                            'error': result.get('error'),
                            'error_description': result.get('errorDescription', 'Unknown error')
                        }
                        
                    return {
                        'success': True,
                        'message_id': message_id,
                        'timestamp': timestamp
                    }
                except json.JSONDecodeError:
                    pass 
            
            return {
                'success': True,
                'message_id': message_id,
                'timestamp': timestamp
            }
                
        except Exception as e:
            return {
                'success': False,
                'error': 'REQUEST_ERROR',
                'error_description': str(e)
            }

def send_messages_in_loop(messengers, recipient_ids, message_content, delay):
    while True:
        for recipient_id in recipient_ids:
            # Gửi tin nhắn từ tất cả tài khoản cùng lúc vào một box
            for messenger in messengers:
                result = messenger.gui_tn(recipient_id, message_content)
                if result['success']:
                    in_dong_khung_cau_vong(f"Đã gửi vào box {recipient_id} - user_id: {messenger.user_id}")
                else:
                    in_dong_khung_cau_vong(f"Không thể gửi vào box {recipient_id} với user_id {messenger.user_id}: {result['error_description']}")
            # Delay sau khi tất cả tài khoản gửi vào một box
            time.sleep(delay)
        # Delay thêm sau khi gửi hết tất cả các box
        time.sleep(delay)

def input_page():
    clear_screen()
    banner()
    in_mau("Treo Mess - Tool Treo Messenger")
    print(Colorate.Diagonal(Colors.green_to_cyan, "════════════════════════════════════════════════"))
    in_dong_khung_cau_vong("Nhập thông tin để bắt đầu gửi tin nhắn")
    print(Colorate.Diagonal(Colors.green_to_cyan, "════════════════════════════════════════════════"))

def main():
    try:
        # Chuyển sang trang nhập thông tin
        input_page()

        # Nhập số lượng ID box
        while True:
            try:
                in_mau("Nhập số lượng ID box:")
                num_boxes = int(input(f"{HĐ_tool}{xanhnhat}"))
                if num_boxes < 1:
                    raise ValueError("Số lượng ID box phải lớn hơn 0")
                break
            except ValueError:
                in_mau("Vui lòng nhập một số hợp lệ")

        # Nhập danh sách ID box
        recipient_ids = []
        in_mau(f"Nhập {num_boxes} ID box (mỗi ID trên một dòng, nhấn Enter sau mỗi ID):")
        for i in range(num_boxes):
            while True:
                in_mau(f"ID box {i+1}:")
                box_id = input(f"{HĐ_tool}{xanhnhat}").strip()
                if box_id and box_id.isdigit():
                    recipient_ids.append(box_id)
                    break
                in_mau("ID box phải là số hợp lệ, vui lòng nhập lại")

        if len(recipient_ids) != num_boxes:
            raise Exception(f"Đã nhập {len(recipient_ids)} ID box, nhưng yêu cầu {num_boxes} ID box")

        in_dong_khung_cau_vong(f"Đã tải {len(recipient_ids)} ID box")

        # Nhập tên file chứa cookie
        in_mau("Nhập tên file chứa cookie (mỗi cookie trên một dòng):")
        cookie_file = input(f"{HĐ_tool}{xanhnhat}").strip()
        try:
            with open(cookie_file, 'r', encoding='utf-8') as f:
                cookies = [line.strip() for line in f if line.strip()]
                
            if not cookies:
                raise Exception("File cookie không chứa cookie nào hợp lệ")

        except FileNotFoundError:
            raise Exception(f"Không tìm thấy file: {cookie_file}")

        in_dong_khung_cau_vong(f"Đã tải {len(cookies)} cookie")

        # Khởi tạo danh sách Messenger
        messengers = []
        for i, cookie in enumerate(cookies, 1):
            try:
                messenger = Messenger(cookie)
                messengers.append(messenger)
                in_dong_khung_cau_vong(f"Cookie {i}: Đã lấy được user_id: {messenger.user_id}")
            except Exception as e:
                in_dong_khung_cau_vong(f"Cookie {i}: Không hợp lệ - {str(e)}")
        
        if not messengers:
            raise Exception("Không có cookie nào hợp lệ")

        # Nhập tên file nội dung tin nhắn
        in_mau("Nhập tên file txt chứa nội dung tin nhắn:")
        file_name = input(f"{HĐ_tool}{xanhnhat}").strip()
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                message_content = f.read().strip()
                
            if not message_content:
                raise Exception("File txt không có nội dung")

        except FileNotFoundError:
            raise Exception(f"Không tìm thấy file: {file_name}")

        # Nhập delay
        while True:
            try:
                in_mau("Nhập delay (giây):")
                delay = float(input(f"{HĐ_tool}{xanhnhat}"))
                if delay <= 0:
                    raise ValueError("Delay phải lớn hơn 0")
                break
            except ValueError:
                in_mau("Vui lòng nhập một số hợp lệ")

        # Chuyển sang trang chạy tool
        clear_screen()
        banner()
        in_dong_khung_cau_vong(f"La Minh Lợi...")
        in_dong_khung_cau_vong(f"Bắt đầu gửi tin nhắn vào {len(recipient_ids)} box với {len(messengers)} cookie, delay {delay}s")
        print(Colorate.Diagonal(Colors.green_to_cyan, "════════════════════════════════════════════════"))

        # Chạy vòng lặp gửi tin nhắn
        send_messages_in_loop(messengers, recipient_ids, message_content, delay)

    except Exception as e:
        in_dong_khung_cau_vong(f"Lỗi: {str(e)}")
        time.sleep(3)
    except KeyboardInterrupt:
        in_dong_khung_cau_vong("Đã Dừng Treo Messenger")
        time.sleep(2)

if __name__ == "__main__":
    main()