from bs4 import BeautifulSoup
import sys,json, os

with open(sys.argv[1], 'r') as f:
	json_data = json.load(f)
for each in json_data:
	tf = open('temp.js', 'w')
	soup = BeautifulSoup(each["Body"], 'html.parser')
	all_scripts = soup.findAll('script')
	sc = []
	for each in all_scripts:
	        if len(each.contents) > 0: 
		        s = each.contents[0]
			sc.append(s)
	script = '\n'.join(sc).encode('utf-8')
	tf.write(script)
	tf.close()
	cmd = 'bash main_main.sh temp.js'
	os.system(cmd)
