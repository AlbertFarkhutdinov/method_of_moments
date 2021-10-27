"""
This module contains description of function and class
for poisson distribution.

References
----------
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html

"""


from typing import Optional

from scipy.stats import poisson

from ._base_discrete import BaseDiscrete


class Poisson(BaseDiscrete):
    """
    Class for Poisson Distribution.

    Parameters
    ----------
    **kwargs : `base.BaseDistribution` properties.

    """

    def __init__(self, **kwargs) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
        super().__init__(**kwargs)

    def _get_var_as_function_of_mean(self) -> Optional[float]:
        """Return variance of random variable as a function of mean."""
        return self.mean

    def pmf(self, arg: int) -> float:
        """Return probability mass function at a given argument."""
        return poisson.pmf(arg, mu=self.mean)
