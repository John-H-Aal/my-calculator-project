from setuptools import setup, find_packages

setup(
    name="my_calculator",
    version="0.1.0",
    description="En simpel calculator til CI/CD demo",
    author="John-H-Aal",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
        ]
    },
)
