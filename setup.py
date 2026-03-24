from setuptools import setup, find_packages

setup(
    name="sap_agent_toolkit",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "pyodbc",
        # Add other dependencies here
    ],
    entry_points={
        "console_scripts": [
            # Define any CLI tools here if needed
        ],
    },
    author="Your Name",
    description="A toolkit for creating SAP to SQL pipelines with agentic workflows.",
    long_description=open("AGENT_WORKFLOW.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-repo-url",  # Replace with your repository URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)