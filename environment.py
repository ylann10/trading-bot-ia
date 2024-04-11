#!/usr/bin/python3

from os import environ
import warnings

environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.warn = lambda *args, **kwargs: None