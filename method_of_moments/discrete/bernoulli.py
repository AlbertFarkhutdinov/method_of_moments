"""
This module contains description of function and class
for Bernoulli distribution.

"""


from typing import Optional, Tuple

from method_of_moments.discrete.base_discrete import BaseDiscrete


class Bernoulli(BaseDiscrete):
    """
    Class for Bernoulli Distribution.

    Parameters
    ----------
    **kwargs : `base.BaseDistribution` properties.

    """

    def __init__(self, **kwargs) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
        super().__init__(**kwargs)
        self.success_probability = self.mean
        self.failure_probability = 1. - self.mean

    def _get_var_as_function_of_mean(self) -> Optional[float]:
        """Return variance of random variable as a function of mean."""
        return self.mean * (1. - self.mean)

    def pmf(self, arg: int) -> float:
        """Return probability mass function at a given argument."""
        if arg == 1:
            return self.success_probability
        if arg == 0:
            return self.failure_probability
        raise ValueError('Unacceptable argument.')

    def get_parameters(self) -> Tuple[float, float]:
        """Return parameters of distribution."""
        return self.success_probability, self.failure_probability
