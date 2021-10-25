"""
This module contains description of abstract base class
for continuous probability distributions initialized with mean and variance.

"""


from abc import abstractmethod
from typing import Optional

from scipy.integrate import quad

from method_of_moments.base import BaseDistribution
from method_of_moments.errors import NotDefinedError


class BaseContinuous(BaseDistribution):
    """
    Abstract class for continuous probability distribution.

    Methods
    -------
    pdf(arg)
        Return value of probability density function for a given argument.
    cdf(arg)
        Return value of cumulative density function for a given argument.

    """

    @abstractmethod
    def pdf(self, arg: float) -> float:
        """
        Return value of probability density function for a given argument.

        """
        raise NotDefinedError(self)

    def cdf(self, arg: float, low_limit: Optional[float]) -> float:
        """Return value of cumulative density function for a given argument."""
        _low_limit = low_limit or (
            -float('inf') if self.is_negative_allowed else 0.0
        )
        return quad(func=self.pdf, a=_low_limit, b=arg)[0]
