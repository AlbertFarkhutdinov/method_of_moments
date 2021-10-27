"""
This module contains description of class
for beta distribution initialized with mean and variance.

References
----------
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.beta.html

"""

from typing import Tuple

from scipy.stats import beta

from method_of_moments.continuous._base_continuous import BaseContinuous


class Beta(BaseContinuous):
    """
    Class for Beta distribution.

    Parameters
    ----------
    max_bin : int
        The value of `scale` parameter for scipy.stats.beta.
    **kwargs : `base.BaseDistribution` properties.

    """

    def __init__(
            self,
            loc: float = 0.,
            scale: float = 1.,
            **kwargs,
    ) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
        super().__init__(**kwargs)
        self.loc = loc
        self.scale = scale
        _mean = (self.mean - loc) / scale
        _variance = self.variance / scale ** 2
        _factor = _mean * (1 - _mean) / _variance - 1.0
        self.a_param = _factor * _mean
        self.b_param = _factor * (1 - _mean)

    @property
    def scale(self) -> float:
        """The value of `scale` parameter for scipy.stats.beta."""
        return self.__scale

    @scale.setter
    def scale(
            self,
            scale: float = 1.,
    ) -> None:
        """Property setter for `self.scale`."""
        if scale < 0:
            raise ValueError('`scale` value must be positive.')
        self.__scale = scale

    def pdf(self, arg: float) -> float:
        """Return probability density function at a given argument."""
        return beta.pdf(
            arg,
            a=self.a_param,
            b=self.b_param,
            loc=self.loc,
            scale=self.scale,
        )

    def cdf(self, arg: float) -> float:
        """Return cumulative density function at a given argument."""
        return beta.cdf(
            arg,
            a=self.a_param,
            b=self.b_param,
            loc=self.loc,
            scale=self.scale,
        )

    def get_parameters(self) -> Tuple[float, float]:
        """Return parameters of distribution."""
        return self.a_param, self.b_param
