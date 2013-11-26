import subprocess
from unipath import Path

def shell_exec(cmd, wait=True):
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	
	if not wait:
		return p
	
	return p.communicate()[0]

def get_closest_uid(path):
	path = Path(path)
	while not path.isdir():
		path = path.ancestor(1)
		if path == '/':
			return False
	return path.stat().st_uid

def get_name_from_uid(uid):
	output = shell_exec(['getent', 'passwd', str(uid)])
	if not output:
		return False
	return output.split(':', 1)[0]

def su(uid, cmd):
	if uid == 0:
		return False
	if type(cmd) is not list:
		return False
	return shell_exec(['su', str(uid)] + cmd)