"""
This package contains description of several probability distributions
and corresponding classes initialized with mean and variance.

"""

from .continuous.beta import Beta
from .continuous.generalized_negative_binomial import GenNBD
from .continuous.normal import Norm
from .discrete.generalized_poisson import GPD
from .discrete.hypergeometric import HGD
from .discrete.negative_binomial import NBD
from .discrete.poisson import Poisson
from .discrete.quasigeometric import QGD
from .discrete.zero_inflated_negative_binomial import ZiNBD
