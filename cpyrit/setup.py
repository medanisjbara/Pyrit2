#!/usr/bin/python
from distutils.core import setup, Extension

cmodule = Extension('_cpyrit',
                    libraries = ['cuda','ssl'],
                    sources = ['cpyrit.c'],
                    extra_compile_args = ['-O0','-ggdb','-I/opt/cuda/targets/x86_64-linux/include'],
                    include_dirs = ['/opt/cuda/targets/x86_64-linux/include','/opt/cuda/targets/x86_64-linux/lib'],
                    extra_objects = ['cpyrit_cuda.o']
                    )

setup (name = 'cpyrit',
       version = '1.0',
       description = 'Fast WPA/WPA2 HMAC through openssl',
       py_modules = ['cpyrit'],
       ext_modules = [cmodule]) 
