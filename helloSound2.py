import subprocess

# The text you want eSpeak to say
text = "Hello, Tirotir!"

# Command to run eSpeak
command = ['espeak', text]

# Run the command
subprocess.run(command)