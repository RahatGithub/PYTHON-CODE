import sys, os, requests, webbrowser as wb

arguments = sys.argv

file_name1, file_name2 = arguments[1], arguments[2]

url_python = "https://www.python.org/"

url_java = "https://docs.oracle.com/en/java/"

res_python = requests.get(url_python)

res_java = requests.get(url_java)

with open(file_name1, "w", encoding = res_python.encoding) as f1:
    f1.write(res_python.text)

with open(file_name2, "w", encoding = res_java.encoding) as f2:
    f2.write(res_java.text)

wb.open(file_name1)

wb.open(file_name2)