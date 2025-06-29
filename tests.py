from functions.write_file import write_file 

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

# ans = get_file_content("calculator", "main.py")
# print(ans)
#
# ans = get_file_content("calculator", "pkg/calculator.py")
# print(ans)
#
# ans = get_file_content("calculator", "/bin/cat")
# print(ans)

ans = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(ans)

ans = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(ans)

ans = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(ans)
