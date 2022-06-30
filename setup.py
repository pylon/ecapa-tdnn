#!/usr/bin/env python

from distutils.core import setup

setup(
    name="ecapa_tdnn",
    version="0.1.1",
    description=("Unofficial reimplementation of ECAPA-TDNN for speaker recognition"),
    url="https://github.com/pylon/ecapa-tdnn/",
    author="TaoRuijie",
    packages=["ecapa_tdnn"],
    data_files=[("ecapa_tdnn", ["exps/pretrain.model"])],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
