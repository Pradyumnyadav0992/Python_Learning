import subprocess as s
# s.run(["echo", "Hello"])
# verion=s.run(["python3","--version"],capture_output=True,text=True)
# print(verion.stdout)
# print(verion.returncode)
# s.run("ls ",shell=True)

# s.run(["python3","---version"])

# if s.run(["ls"],capture_output=True).returncode == 0:
#     print("success")

# s.run()

# def run_command(cmd):
#     test=s.run(cmd,capture_output=True)
#     (stdout, stderr, returncode)=(test.stdout,test.stderr,test.returncode)
#     return (stdout, stderr, returncode)

# print(run_command(["ls","-ltra"]))
# s.run(["python3","sys.py"])


with open("test.txt","+a") as test:
    s.run(["echo","Redirect","Test"],stdout=test,stderr=test)

# result = s.run(
#     ["python3", "-c", "print(input())"],
#     input="Hello from Python\n",
#     text=True,
#     capture_output=True
# )
# print(result.stdout)  


# input_data = "banana\napple\ncherry\n"

# # Run 'sort' command and pass input via stdin
# result = s.run(
#     ["sort"], 
#     input=input_data, 
#     text=True, 
#     capture_output=True
# )

# print("Sorted output:")
# print(result.stdout)

# process = s.Popen(
#     ["ping", "-c", "3", "google.com"],  # -c 3 = send 3 pings
#     stdout=s.PIPE,
#     stderr=s.STDOUT,
#     text=True
# )

# # Read live output line by line
# for line in process.stdout:
#     print("LIVE:", line.strip())

# process.wait()  # Wait for process to finish
# print("Process exited with code:", process.returncode)
# import logging

# logging.basicConfig(level=logging.CRITICAL,

#                     format="%(asctime)s - %(levelname)s - %(message)s"
                    
#                     )  # set minimum level to DEBUG

# logging.debug("Debugging details")
# logging.info("Just some info")
# logging.warning("This is a warning")
# logging.error("This is an error")
# logging.critical("Critical issue!")

import json
data = {"name": "Alice", "age": 25, "is_student": True}

# # Convert to JSON string
# json_str = json.dumps(data)
# print(json_str)   # {"name": "Alice", "age": 25, "is_student": true}

# Save JSON to file
with open("data.json", "w") as f:
    json.dump(data, f)

parsed = json.loads('{"name": "Alice", "age": 25}')
print(parsed["name"])   # Alice

# From JSON file
with open("data.json", "r") as f:
    parsed_file = json.load(f)
    print(parsed_file)