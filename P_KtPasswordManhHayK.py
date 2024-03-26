import re

password = input("Nhập mật khẩu : ")

is_strong = lambda s: len(s) >= 8 and bool(re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?/\\]', s)) and bool(re.search(r'[A-Z]', s)) and bool(re.search(r'\d', s)) and bool(re.search(r'[a-z]', s))

print("Đây là một mật khẩu mạnh." if is_strong(password) else "Đây không phải là một mật khẩu mạnh.")

