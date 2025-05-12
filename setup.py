from setuptools import find_packages, setup
from typing import List

HYPEN_DOT_E = "-e ."

def get_requirements(file_path: str) -> List[str]:

    """ 
    This function will return the list of requirements
    
    """

    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)

    return requirements


## Define local package
setup(
    name="Perplexity 2.0 - Live Web Search Agent",
    version="0.0.1",
    author="Brigunandan Sharma",
    author_email="brigunandan.s@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)