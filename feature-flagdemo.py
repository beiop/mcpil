#This turns --printagailvabiotsd into TRUE flagname|FALSE flagothername

import subprocess

def run():
    command = ["./minecraft-pi-reborn-3.0.0-amd64.AppImage","--print-available-feature-flags"]  ##--fix-me--##
    try:
        # Execute the command and capture the output
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        output = result.stdout

        # Replace newlines with | and remove the last character
        settings_string = output.replace("\n", "|")[0:-1]

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    # Convert the string into a dictionary
    settings = {}
    for item in settings_string.split('|'):
        parts = item.strip().split(' ', 1)
        if len(parts) == 2:
            value_str, name = parts
            value = value_str.strip().lower() == "true"
            settings[name.strip()] = value
    return settings



def result():
    result_parts = []
    for name, var in variables.items():
        state_str = "TRUE" if var.get() else "False"
        result_parts.append(f"{state_str} {name}")

    # Join with '|'
    result_string = '|'.join(result_parts)
    print(result_string)

import tkinter as tk

root = tk.Tk()
settings = run()
variables = {}
tk.Button(root, text="OK", command=result).pack()
for name, value in settings.items():
    var = tk.BooleanVar(value=value)
    variables[name] = var
    cb = tk.Checkbutton(root, text=name, variable=var)
    cb.pack()

root.mainloop()