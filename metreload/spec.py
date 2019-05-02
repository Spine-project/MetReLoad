"""
Specifications for PyInstaller
"""

from PyInstaller.building.build_main import Analysis, PYZ
from PyInstaller.utils.hooks import copy_metadata, collect_data_files

from . import __version__ as version


BLOCK_CIPHER = None
UPX = True
BASENAME = 'metreload'

name_with_version = '{}-{}'.format(BASENAME, version)  # pylint: disable=C0103

# Do analysis
a = Analysis(['metreload/cli.py'],
             pathex=[],
             binaries=[],
             datas=copy_metadata('pydap')\
                   + collect_data_files('distributed')\
                   + [('docs/_build/html', 'documentation')],
             hiddenimports=['pandas._libs.tslibs.np_datetime',
                            'pandas._libs.skiplist',
                            'pydap.responses.das',
                            'pydap.responses.html',
                            'pydap.responses.ascii',
                            'pydap.responses.version'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=BLOCK_CIPHER)

pyz = PYZ(a.pure, a.zipped_data,
          cipher=BLOCK_CIPHER)

options = dict(strip=False,
               upx=True)

exe_options = dict(name=BASENAME,
                   debug=False,
                   console=True)
