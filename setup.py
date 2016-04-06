from distutils.core import setup
files = ["NTV/*"]

setup(name = "NTV",
version="0.5",
description="Astronomical Data Viewer",
author="Nate Lust",
author_email="nlust@astro.princeton.edu",
packages=['NTV'],
requires=['numpy','matplotlib','astropy','PyQt4','scipy'],
license="revised BSD",
scripts=['ntviewer'])
