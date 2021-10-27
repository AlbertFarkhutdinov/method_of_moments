"""
This module contains description of function and class
for normal (Gauss) distribution.

References
----------
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html

"""


from typing import Tuple

from scipy.stats import norm

from method_of_moments.continuous._base_continuous import BaseContinuous


class Norm(BaseContinuous):
    """
    Class for Normal (Gauss) Distribution.

    Parameters
    ----------
    **kwargs : `base.BaseDistribution` properties.

    """

    def __init__(self, **kwargs) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
        super().__init__(**kwargs)
        self.loc = self.mean
        self.scale = self.variance ** 0.5

    def pdf(self, arg: float) -> float:
        """Return probability density function at a given argument."""
        return norm.pdf(arg, loc=self.loc, scale=self.scale)

    def cdf(self, arg: float, low_limit=-float('inf')) -> float:
        """Return cumulative density function at a given argument."""
        return norm.cdf(arg, loc=self.loc, scale=self.scale)

    def get_parameters(self) -> Tuple[float, float]:
        """Return parameters of distribution."""
        return self.loc, self.scale
