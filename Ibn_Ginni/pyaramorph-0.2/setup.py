from setuptools import setup

setup(name='pyaramorph',
        version='0.2',
        description='An Arabic morphological analyzer and lexicon',
        url='https://bitbucket.org/alexlee/pyaramorph',
        author='Alex Lee',
        author_email='alexlee@fastmail.net',
        license='GPLv2',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Education',
            'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
            'Natural Language :: Arabic',
            'Natural Language :: English',
            'Programming Language :: Python :: 3 :: Only',
            'Topic :: Education',
        ],
        packages=['pyaramorph'],
        include_package_data=True,
        entry_points='''
            [console_scripts]
            pyaramorph=pyaramorph.command:main
        ''',
        zip_safe=False)

