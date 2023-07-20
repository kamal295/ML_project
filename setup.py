#responsible in  creating ml application as pacakage
#install this pacakage in your project and use it
#using setup.py my entire ml app as pacakage and even deploy in pipi
#-e. map to setup.py 
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return  requirements
    

setup(

name="ml_project",
version="0.0.1",
author="Kamal",
author_email="kamalroosewelt@gmail.com",
packages=find_packages(),
install_requirements=get_requirements("requirements.txt")

)