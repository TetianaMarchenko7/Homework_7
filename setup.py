from setuptools import setup, find_namespace_packages


setup ( name='clean_folder',
      version='1',
      description='Folder\'s cleaner',
      url='https://github.com/TetianaMarchenko7/Homework_7.git',
      author='Tetiana Marchenko',
      author_email='tmarchenko@ukr.net',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']})