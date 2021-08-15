from setuptools import setup, version, find_packages
with open("multilabeler\README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup (name ="multilabeler",
        version =0.4,
        description ='Prediction of two dependent labels',
        #packages = ["multilabeler"],
        zip_safe =False,
        author = 'Abraham Owodunni',
        author_name = 'owodunniabraham@gmail.com',
        long_description = long_description,
        long_description_content_type = 'text/markdown',
        url = 'https://github.com/owos/Multilabeler',
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    
    package_dir="" ,
    packages= find_packages(where=""),
    python_requires=">=3.6",
)