# systemd Service Notification

This is a pure Python implementation of the
[`systemd`](http://www.freedesktop.org/wiki/Software/systemd/)
[`sd_notify`](http://www.freedesktop.org/software/systemd/man/sd_notify.html)
protocol. This protocol can be used to inform `systemd` about service start-up
completion, watchdog events, and other service status changes. Thus, this
package can be used to write system services in Python that play nicely with
`systemd`. `sdnotify` is compatible with both Python 2 and Python 3.

Normally the `SystemdNotifier.notify` method silently ignores exceptions (for example, if the
systemd notification socket is not available) to allow applications to
function on non-systemd based systems. However, setting `debug=True` will
cause this method to raise any exceptions generated to the caller, to
aid in debugging.

# Example Usage

This is an example of a simple Python service that informs `systemd` when its
startup sequence is complete. It also sends periodic status updates to `systemd`,
which can be viewed with `systemctl status test`.

## `test.py`
```python
import sdnotify
import time

print("Test starting up...")
# In a real service, this is where you'd do real startup tasks
# like opening listening sockets, connecting to a database, etc...
time.sleep(10)
print("Test startup finished")

# Inform systemd that we've finished our startup sequence...
n = sdnotify.SystemdNotifier()
n.notify("READY=1")

count = 1
while True:
	print("Running... {}".format(count))
	n.notify("STATUS=Count is {}".format(count))
	count += 1
	time.sleep(2)
```

## `test.service`

    [Unit]
    Description=A test service written in Python

    [Service]
    # Note: setting PYTHONUNBUFFERED is necessary to see the output of this service in the journal
    # See https://docs.python.org/2/using/cmdline.html#envvar-PYTHONUNBUFFERED
    Environment=PYTHONUNBUFFERED=true

	# Adjust this line to the correct path to test.py
    ExecStart=/usr/bin/python /path/to/test.py

    # Note that we use Type=notify here since test.py will send "READY=1"
    # when it's finished starting up
	Type=notify
