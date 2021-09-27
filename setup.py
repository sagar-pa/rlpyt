import setuptools

INSTALL_REQUIRES = [
    "gym>=0.20",
    "torch>=1.9.1"
    "numpy",
    "pandas",
    "tqdm",
    "scipy",
    "atari-py",
    "opencv-python",
    "psutil",
    "PyPrind"
]
TEST_REQUIRES = [
    # testing and coverage
    'pytest', 'coverage', 'pytest-cov',
]

setuptools.setup(
    name='rlpyt',
    version='0.1.3',
    python_requires='>=3.8',
    packages=setuptools.find_packages(),
    license='MIT License',
    long_description=open('README.md').read(),
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'extra': TEST_REQUIRES + INSTALL_REQUIRES,
    },

)
