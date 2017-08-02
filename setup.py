from distutils.core import setup

VERSION='0.3.2'

setup(
    name = 'sdnotify',
    packages = ['sdnotify'],
    version = VERSION,
    description = 'A pure Python implementation of systemd\'s service notification protocol (sd_notify)',
    author = 'Brett Bethke',
    author_email = 'bbethke@gmail.com',
    url = 'https://github.com/bb4242/sdnotify',
    download_url = 'https://github.com/bb4242/sdnotify/tarball/v{}'.format(VERSION),
    keywords = ['systemd'],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description = """\
systemd Service Notification

This is a pure Python implementation of the systemd sd_notify protocol. This protocol can be used to inform systemd about service start-up completion, watchdog events, and other service status changes. Thus, this package can be used to write system services in Python that play nicely with systemd. sdnotify is compatible with both Python 2 and Python 3.
"""
)
