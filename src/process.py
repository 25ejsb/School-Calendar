import subprocess, signal
subprocess.Popen(['python3', 'app.py'],
                 stdin=subprocess.DEVNULL,
                 stdout=open('nohup.out', 'w'),
                 stderr=subprocess.STDOUT,
                 start_new_session=True,
                 preexec_fn=(lambda: signal.signal(signal.SIGHUP, signal.SIG_IGN)))