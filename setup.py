import setuptools

INSTALL_REQUIRES = [
    "gym>=0.17,<0.20",
    "torch>=1.9.1",
    "numpy",
    "pandas",
    "tqdm",
    "scipy",
    "atari-py==0.2.9",
    "pillow",
    "opencv-python",
    "psutil",
    "PyPrind",
    "tensorboard>=2.2.0",
]
TEST_REQUIRES = [
    # testing and coverage
    'pytest', 'coverage', 'pytest-cov',  
]

setuptools.setup(
    name='rlpyt',
    version='0.1.4',
    python_requires='>=3.8',
    packages=setuptools.find_packages(),
    license='MIT License',
    long_description=open('README.md').read(),
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'test': TEST_REQUIRES + INSTALL_REQUIRES,
    },

)
