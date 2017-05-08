import json, sys

of = open("day1.txt", "a")
inf = open(sys.argv[1], "r")
data = json.load(inf)

f_counts = []
eval_count= len(data["_data"]["eval_calls"])
f_counts.append(eval_count)
fun_calls = len(data["_Function_calls"].keys())
f_counts.append(fun_calls)
wscript_saved_files_count = len(data['_wscript_saved_files'].keys())
f_counts.append(wscript_saved_files_count)
wscript_urls_count = len(data["_wscript_urls"])
f_counts.append(wscript_urls_count)
wscript_objects_count = len(data["_wscript_objects"])
f_counts.append(wscript_objects_count)
setTimeout_calls = len(data["_setTimeout_calls"])
f_counts.append(setTimeout_calls)
browser_documents = len(data["_browser_documents"])
f_counts.append(browser_documents)
unescape_call = len(data["_unescape_calls"])
f_counts.append(unescape_call)
res = ""
for each in f_counts:
	res += str(each) + "\n"
of.write(res)
