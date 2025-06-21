# %%
import re
def grades():
    with open ("grades.txt", "r") as file:
        grades = file.read()
        #print(grades)
    # YOUR CODE HERE
    result = re.findall(r'[A-Z][a-z]+\s[A-Z][a-z]+:\sB', grades)
    print(result)
    return len(result)
print(grades())
# %%
import re

def logs():
    with open("logdata.txt", "r") as file:
        logdata = file.read()
    
    # YOUR CODE HERE
    host_patt = r'(?P<host>[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})'
    user_name_p = r'(?P<user_name>[\w]*|\-)'
    time_patt = r'(?P<time>[\w0-9:\s\-\/]*)'
    request_patt = r'(?P<request>[\w0-9:\s\-\/\.\%\\]*)'
    pattern = host_patt + r'\s*\-\s*' + user_name_p + r'\s*\[' + time_patt + r'\]\s*\"' + request_patt #+ '*\"' 
    dict_r = []
    for r in re.finditer(pattern, logdata):
         print(r.groupdict())
         dict_r.append(r.groupdict())

    return(dict_r)

log = logs()
print(len(log))
print(log)

one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in log, "Sorry, this item should be in the log results, check your formating"
# %%
