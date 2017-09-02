import subprocess

# subprocess.Popen(r"C:\Windows\WinSxS\amd64_microsoft-windows-calc_31bf3856ad364e35_10.0.14393.0_none_d7326cb6316e9c64\calc.exe")

subprocess.Popen([r'C:\Windows\WinSxS\wow64_microsoft-windows-notepad_31bf3856ad364e35_10.0.14393.0_none_a6e3a348bb1321d5\notepad.exe', 'hello.txt'],
shell=True)
