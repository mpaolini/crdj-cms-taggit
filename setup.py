# -*- coding: utf-8 -*-
from distutils.core import setup
import os

data_dirs = []

for d in os.walk('%s/locale' % 'crdj_cms_taggit'):
    data_dirs.append(d[0][len('crdj_cms_taggit')+1:] + '/*.mo')
    data_dirs.append(d[0][len('crdj_cms_taggit')+1:] + '/*.po')

for d in os.walk('%s/templates' % 'crdj_cms_taggit'):
    data_dirs.append(d[0][len('crdj_cms_taggit')+1:] + '/*.html')

setup(
    name='crdj-cms-taggit',
    version='0.1',
    install_requires = [
        'django',
        'django-cms',
        'django-taggit',
    ],
    packages=['crdj_cms_taggit'],
    package_data = {'crdj_cms_taggit': data_dirs}
)
