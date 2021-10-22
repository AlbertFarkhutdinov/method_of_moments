"""
This module contains description of abstract base class
for probability distributions initialized with mean and variance.

"""


from abc import ABC
from typing import Optional

from pretty_repr import RepresentableObject


class BaseDistribution(RepresentableObject, ABC):
    """
    Abstract class for probability distributions.

    Parameters
    ----------
    mean : float
        Expected value of random variable.
    variance : float, optional
        Variance of random variable.
        If it is None, absolute value of `mean` is used.
    is_negative_parameters_allowed : bool, optional, default: True
        Whether are negative parameters allowed.

    Raises
    ------
    ValueError
        If `mean` or `variance` are negative values,
        while `is_negative_parameters_allowed` is False.

    """

    def __init__(
            self,
            mean: float,
            variance: Optional[float] = None,
            is_negative_parameters_allowed: bool = True
    ) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
        self.is_negative_parameters_allowed = is_negative_parameters_allowed
        self.mean = mean
        self.variance = variance

    @property
    def mean(self) -> float:
        """Expected value of random variable."""
        return self.__mean

    @mean.setter
    def mean(self, mean: float) -> None:
        """Property setter for `self.mean`"""
        if mean < 0 and not self.is_negative_parameters_allowed:
            raise ValueError('Mean value cannot be negative.')
        self.__mean = mean

    @property
    def variance(self) -> float:
        """Variance of random variable."""
        return self.__variance

    @variance.setter
    def variance(self, variance: Optional[float] = None,) -> None:
        """Property setter for `self.variance`"""
        _variance = abs(self.mean) if variance is None else variance
        if _variance < 0 and not self.is_negative_parameters_allowed:
            raise ValueError('Variance value cannot be negative.')
        self.__variance = _variance
