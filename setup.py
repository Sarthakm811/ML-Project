from setuptools import setup, find_packages     
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements 
    '''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements
    
setup(

    name='mlprpject',
    version='0.1.0',
    author='Sarthak Mahajan',
    author_email="sarthakm811@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)