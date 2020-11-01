import setuptools

setuptools.setup(
    name="lipreading_tcn", 
    version="1.0",
    author="Pingchuan Ma",
    description="Pingchuans lipreading repo, that I modified very slightly",
    url="https://github.com/miraodasilva/Lipreading_using_Temporal_Convolutional_Networks",
    package_dir={"lipreading_tcn":"../lipreading_tcn"},
    packages=setuptools.find_packages(),
    package_data={"lipreading_tcn":["configs/*.json"]}
)
