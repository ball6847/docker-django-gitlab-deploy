import subprocess

def shell_exec(cmd, wait=True):
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	
	if not wait:
		return p
	
	return p.communicate()[0]