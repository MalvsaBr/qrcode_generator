from cx_Freeze import setup, Executable
import sys
import os

arquivos = ['logo.ico','QRCode/','img/']

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

configs = Executable(
    script='app.py',
    icon='logo.ico',
    base= base
)

setup(
    name= 'Gerador de QRCode',
    version= '1.0',
    description= 'Gerador de QRCode',
    author= 'Dev Matheus Alves',
    options= {'build_exe': {'include_files': arquivos, 'include_msvcr': True}},
    executables= [configs]

)
