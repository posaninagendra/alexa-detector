rm sandbox_dump_after.json
# for file in ../../datasets/checker/malicious_js/*.js
# for file in malware/**/*.js
  # echo "###############FileName############: $file"
  # node jailme.js --down=y  temp.js
  # echo "###########################################################################FILENAME : ########################################################################:"
  # node jailme.js --down=y $file || echo -e "-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1" >> features.txt
  # python parser.py sandbox_dump_after.json
  # rm sandbox_dump_after.json
  # rm temp.js
  # # exit


  echo "###########################################################################FILENAME########################################################################: $file"
  gtimeout 10 node jailme.js --down=y  temp.js
  if [ $? -eq 124 ]; then
    echo -e "-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1" >> day1.txt
  else
    python parser.py sandbox_dump_after.json
  	rm sandbox_dump_after.json
  	rm temp.js
  # exit
  fi

