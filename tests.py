from functions.get_file_content import get_file_content

# ans = get_files_info("calculator", ".")
# print(ans)
#
# ans = get_files_info("calculator", "pkg")
# print(ans)
#
# ans = get_files_info("calculator", "/bin")
# print(ans)
#
# ans = get_files_info("calculator", "../")
# print(ans)

# ans = get_file_content("calculator", "lorem.txt");
# print(ans)

ans = get_file_content("calculator", "main.py")
print(ans)

ans = get_file_content("calculator", "pkg/calculator.py")
print(ans)

ans = get_file_content("calculator", "/bin/cat")
print(ans)
