from setuptools import setup

setup(
    name="prose",
    version="0.1",
    author="Lionel J. Garcia",
    description="Reduction and analysis of FITS telescope observations",
    py_modules=["prose"],
    url="https://github.com/LionelGarcia/prose",
    # entry_points="""
    #     [console_scripts]
    #     prose=main:cli
    # """,
    install_requires=[
        "numpy",
        "scipy",
        "astropy==4.0",
        "matplotlib",
        "colorama",
        "scikit-image",
        "pandas",
        "tqdm",
        "astroalign",
        "photutils",
        "click",
        "astroquery",
        "pyyaml",
        "sphinx",
        "docutils",
        "tabulate",
        "sphinx_rtd_theme",
        "imageio",
        "george",
        "fpdf",
        "tensorflow",
        "sep"
    ],
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
