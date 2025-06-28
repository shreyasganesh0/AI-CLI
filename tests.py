from functions.get_files_info import get_files_info

ans = get_files_info("calculator", ".")
print(ans)

ans = get_files_info("calculator", "pkg")
print(ans)

ans = get_files_info("calculator", "/bin")
print(ans)

ans = get_files_info("calculator", "../")
print(ans)
