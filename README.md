# systemd Notification

This is a pure Python implementation of the
[`systemd`](http://www.freedesktop.org/wiki/Software/systemd/)
[`sd_notify`](http://www.freedesktop.org/software/systemd/man/sd_notify.html)
protocol. This protocol can be used to inform `systemd` about service start-up
completion, watchdog events, and other service status changes. Thus, this
package can be used to write system services in Python that play nicely with
`systemd`.

# Example Usage

This is an example of a simple Python service that informs `systemd` when its
startup sequence is complete. It also sends periodic status updates to `systemd`,
which can be viewed with `systemctl status test`.

## `test.py`
    import sdnotify
	import time

	print("Test starting up...")
	time.sleep(10)
	print("Test startup finished")
	n = sdnotify.SystemdNotifier()
	n.notify("READY=1")

	count = 1
	while True:
		print("running... {}".format(count))
		n.notify("STATUS=Count is {}".format(count))
		count += 1
		time.sleep(2)


## `test.service`

    [Unit]
    Description=A test service written in Python

    [Service]
    # Note: setting PYTHONUNBUFFERED is necessary to see the output of this service in the journal
    # See https://docs.python.org/2/using/cmdline.html#envvar-PYTHONUNBUFFERED
    Environment=PYTHONUNBUFFERED=true
    ExecStart=/usr/bin/python /path/to/test.py
    Type=notify

