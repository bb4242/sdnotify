import socket
import os

class SystemdNotifier:
    """This class holds a connection to the systemd notification socket
    and can be used to send messages to systemd using its notify method."""

    def __init__(self):
        """Instantiate a new notifier object. This will initiate a connection
        to the systemd notification socket."""
        try:
            self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
            addr = os.getenv('NOTIFY_SOCKET')
            if addr[0] == '@':
                addr = '\0' + addr[1:]
            self.socket.connect(addr)
        except:
            self.socket = None

    def notify(self, state):
        """Send a notification to systemd. state is a string; see
        the man page of sd_notify (http://www.freedesktop.org/software/systemd/man/sd_notify.html)
        for a description of the allowable values.

        Returns True if the notification was sent successfully, and False otherwise."""
        try:
            self.socket.sendall(state)
            return True
        except:
            return False
