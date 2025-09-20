# import os

# print(os.getcwd())


# os.chdir("test")
# print(os.getcwd())
# print(os.listdir("."))


# os.rmdir("practice_dir")
# os.mkdir("practice_dir")
# os.chdir("..")
# with open ("demo.txt","w") as de:
#     de.write("this is a new file \n")
# os.rename("demo.txt","renamed_demo.txt")

# os.remove("renamed_demo.txt")

# if os.path.exists("data.csv"):
#     print("if data.csv exist")

# if os.path.isdir("data.csv"):
#     print("data.csv is dir")

# if os.path.isfile("data.csv"):
#     print("data.csv is file")

# if os.path.exists("my_folder"):
#     print("folder exist")
# else:
#     print("folder does not exist")

# print(os.path.join("folder","subfolder","file.txt"))
# testpath="/home/user/docs/report.pdf"
# print(os.path.basename(testpath))
# print(os.path.dirname(testpath))

# print(os.path.split(testpath))

# print(os.environ.get("HOME"))
# os.environ["GET"]="BYE"
# print(os.environ.get("GET"))


# os.system("ls -ltra")
# print(os.getlogin())
# print(os.cpu_count())


# stats = os.stat("data.csv")
# print(stats)


# print(os.path.abspath("1.py"))
# print(os.environ.get("SHELL"))


import shutil as s
import os
# os.mkdir("project_files")
# os.chdir("project_files")
# with open("report.txt","w") as r:
#     r.write("this is new file\n")
# s.copy2("report.txt","test")

# s.rmtree("project_backup")
# s.rmtree("project_files")
# os.mkdir("project_backup")
# os.mkdir("project_files")
# filepath=os.path.join("project_files","report.txt")
# with open(filepath,"w") as r:
#     r.write("this is new file\n")

# s.copytree("project_files","project_backup")


# s.copy2("data.txt","backup.txt")
# os.mkdir("archive")
# filepathreport=os.path.join("archive","reports_copy.pdf")
# with open("reports.pdf" ,"w") as re:
#     re.write("hello this is new file")
# # s.copy2("reports.pdf",filepathreport)


# print(s.disk_usage("/"))

# # s.make_archive("proje","zip","project_files")
# # s.unpack_archive("project_files.zip","sfg")
# print(s.which("sh"))