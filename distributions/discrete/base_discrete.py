"""
This module contains description of abstract base class
for discrete probability distributions initialized with mean and variance.

"""


from abc import abstractmethod

from distributions.base import BaseDistribution
from errors import NotDefinedError


class BaseDiscreteDistribution(BaseDistribution):
    """
    Abstract class for discrete probability distributions.

    Methods
    -------
    pmf(arg)
        Return probability mass function.
    cmf(arg)
        Return cumulative mass function.

    """

    @abstractmethod
    def pmf(self, arg: int) -> float:
        """Return probability mass function."""
        raise NotDefinedError(self)

    def cmf(self, arg: int) -> float:
        """Return cumulative mass function."""
        result = 0.0
        for k in range(0, arg):
            result += self.pmf(k)
        return result
