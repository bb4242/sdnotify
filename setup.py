from distutils.core import setup
setup(
    name = 'sdnotify',
    packages = ['sdnotify'],
    version = '0.1.0',
    description = 'A pure Python implementation of systemd\'s service notification protocol (sd_notify)',
    author = 'Brett Bethke',
    author_email = 'bbethke@gmail.com',
    url = 'https://github.com/bb4242/sdnotify',
    download_url = 'https://github.com/bb4242/sdnotify/tarball/0.1',
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
)
