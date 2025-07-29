from setuptools import setup,find_packages
from typing import List

def get_requirements(filename:str)->List[str]:
    requirements=[]
    try:
        with open(filename, 'r') as file_obj:
            for line in file_obj:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirements.append(requirement)
                
    except FileNotFoundError:
        print("requirements.txt file not found. Please create it with the necessary dependencies.") 
    return requirements

    
setup(
    name = "mlproject",
    author = "Abhiram S R",
    author_email="abhiramsr173@gmail.com",
    packages=find_packages(),
    version="0.0.1",
    install_requires=get_requirements('requirements.txt')
)

