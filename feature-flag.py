import subprocess

def run():
    command = ["./minecraft-pi-reborn-3.0.0-amd64.AppImage","--print-available-feature-flags"]
    try:
        # Execute the command and capture the output
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        output = result.stdout

        # Replace newlines with | and remove the last character
        formatted_output = output.replace("\n", "|")[0:-1]
        return formatted_output

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
run()