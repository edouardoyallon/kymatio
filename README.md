Kymatio: Wavelet scattering in Python
======================================

Kymatio is an implementation of the wavelet scattering transform in the Python programming language, suitable for large-scale numerical experiments in signal processing and machine learning.
Scattering transforms are translation-invariant signal representations implemented as convolutional networks whose filters are not learned, but fixed (as wavelet filters).

[![PyPI](https://img.shields.io/badge/python-3.5%2C%203.6%2C%203.7-blue.svg)](https://pypi.org/project/kymatio/)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Build Status](https://travis-ci.org/kymatio/kymatio.svg?branch=master)](https://travis-ci.org/kymatio/kymatio)
[![Downloads](https://pepy.tech/badge/kymatio)](https://pepy.tech/project/kymatio)
[![codecov](https://codecov.io/gh/kymatio/kymatio/branch/master/graph/badge.svg)](https://codecov.io/gh/kymatio/kymatio)


Use Kymatio if you need a library that:
* supports 1-D, 2-D, and 3-D wavelets,
* integrates wavelet scattering in a deep learning architecture, and
* runs seamlessly on CPU and GPU hardware, with many deep learning API.


### Flexibility

The Kymatio organization associates the developers of several pre-existing packages for wavelet scattering, including `ScatNet`, `scattering.m`, `PyScatWave`, `WaveletScattering.jl`, and `PyScatHarm`.

The resort to PyTorch tensors as inputs to Kymatio allows the programmer to backpropagate the gradient of wavelet scattering coefficients, thus integrating them within an end-to-end trainable pipeline, such as a deep neural network.

### Portability

Each of these algorithms is written in a high-level imperative paradigm, making it portable to any Python library for array operations as long as it enables complex-valued linear algebra and a fast Fourier transform (FFT).

Currently, there are four available frontend-backends, PyTorch (CPU and GPU), PyTorch+SciKit-cuda (GPU only), TensorFlow (CPU and GPU) and NumPy (CPU).

### Scalability

Kymatio integrates the construction of wavelet filter banks in 1D, 2D, and 3D, as well as memory-efficient algorithms for extracting wavelet scattering coefficients, under a common application programming interface.

Running Kymatio on a graphics processing unit (GPU) rather than a multi-core conventional computer processing unit (CPU) allows for significant speedups in computing the scattering transform.
The current speedup with respect to CPU-based MATLAB code is of the order of 10 in 1D and 3D and of the order of 100 in 2D.

We refer to our [official benchmarks](https://www.kymat.io/userguide.html#benchmarks) for further details.

### How to cite

If you use this package, please cite the following paper:

Andreux M., Angles T., Exarchakis G., Leonarduzzi R., Rochette G., Thiry L., Zarka J., Mallat S., Andén J., Belilovsky E., Bruna J., Lostanlen V., Hirn M. J., Oyallon E., Zhang S., Cella C., Eickenberg M. (2019). Kymatio: Scattering Transforms in Python. arXiv preprint arXiv:1812.11214. [(paper)](https://arxiv.org/abs/1812.11214)

## Installation


### Dependencies

Kymatio requires:

* Python (>= 3.5)
* SciPy (>= 0.13)


### Standard installation (on CPU hardware)
We strongly recommend running Kymatio in an Anaconda environment, because this simplifies the installation of other
APIs. You may install the latest version of Kymatio using the package manager `pip`, which will automatically download
Kymatio from the Python Package Index (PyPI):

```
pip install kymatio
```

Linux and macOS are the two officially supported operating systems.


### Frontend

#### NumPy

To explicitely call the `numpy` frontend, simply do for instance:

```
import numpy as np
from kymatio import Scattering2D
scattering = Scattering2D(J=2, shape=(32, 32), frontend='numpy')
```

#### PyTorch

After installing the latest version of `torch`, you can call Scattering2d as a `nn.Module` via for instance:

```
import torch
from kymatio import Scattering2D
scattering = Scattering2D(J, shape=(M, N), L=L, frontend='torch')
```

#### TensorFlow

After installing the latest version of `tensorflow`, you can call Scattering2d as a `tf.Module` via for instance:

```
import tensorflow as tf
from kymatio import Scattering2D
scattering = Scattering2D(J, shape=(M, N), L=L, frontend='tensorflow')
```

### GPU acceleration

The available backends are PyTorch (`torch`), PyTorch+SciKit-cuda (`skcuda`), TensorFlow (`tensorflow`), and NumPy
(`numpy`).

NumPy is the default frontend in 1D, 2D, and 3D scattering. For applications of the 2D scattering transform to large
images (e.g. ImageNet, of size 224x224), however, we recommend the `skcuda` backend, which is substantially faster
than NumPy.

#### PyTorch and scikit-cuda

To run Kymatio on a graphics processing unit (GPU), you can either use the PyTorch-style `cuda()` method to move your
object to GPU. Kymatio is designed to operate on a variety of backends for tensor operations. For extra speed, install
the CUDA library and install the `skcuda` dependency by running the following pip command:

```
pip install scikit-cuda cupy
```

The user may control the choice of backend at runtime via for instance:

```
import torch
from kymatio import Scattering2D
from kymatio.scattering2d.backend.torch_skcuda_backend import backend
scattering = Scattering2D(J, shape=(M, N), L=L, backend=backend, frontend='torch')
```

### Installation from source

Assuming the Kymatio source has been downloaded, you may install it by running

```
pip install -r requirements.txt
python setup.py install
```

Developers can also install Kymatio via:

```
pip install -r requirements.txt
python setup.py develop
```

## Documentation

The documentation of Kymatio is officially hosted on the [kymat.io](https://www.kymat.io/) website.


### Online resources

* [GitHub repository](https://github.com/kymatio/kymatio)
* [GitHub issue tracker](https://github.com/kymatio/kymatio/issues)
* [BSD-3-Clause license](https://github.com/kymatio/kymatio/blob/master/LICENSE.md)
* [List of authors](https://github.com/kymatio/kymatio/blob/master/AUTHORS.md)
* [Code of conduct](https://github.com/kymatio/kymatio/blob/master/CODE_OF_CONDUCT.md)


### Building the documentation from source
The documentation can also be found in the `doc/` subfolder of the GitHub repository.
To build the documentation locally, please clone this repository and run

```
pip install -r requirements_optional.txt
cd doc; make clean; make html
```

## Support

We wish to thank the Scientific Computing Core at the Flatiron Institute for the use of their computing resources for testing.

[![Flatiron](doc/source/_static/FL_Full_Logo_Mark_Small.png)](https://www.simonsfoundation.org/flatiron)

We would also like to thank École Normale Supérieure for their support.

[![ENS](https://www.ens.fr/sites/default/files/inline-images/logo.jpg)](https://www.ens.fr/)

## Kymatio

Kyma (*κύμα*) means *wave* in Greek. By the same token, Kymatio (*κυμάτιο*) means *wavelet*.

Note that the organization and the library are capitalized (*Kymatio*) whereas the corresponding Python module is written in lowercase (`import kymatio`).

The recommended pronunciation for Kymatio is *kim-ah-tio*. In other words, it rhymes with patio, not with ratio.
