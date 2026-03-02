from setuptools import setup, find_packages
setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Manya Kamra',
    author_email='manyakam04@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)