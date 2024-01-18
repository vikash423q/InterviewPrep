from abc import ABC, abstractmethod
from enum import Enum, auto


class Regime(Enum):
    OLD = auto()
    NEW = auto()


class TaxRegime(ABC):
    @abstractmethod
    def calculate_tax(self, total: int) -> int:
        pass


class OldTaxRegime(TaxRegime):
    def calculate_tax(self, total: int) -> int:
        print('Calculating with old tax regime!')
        if total > 1000000:
            return int(0.3*(total-1000000))
        return 0


class NewTaxRegime(TaxRegime):
    def calculate_tax(self, total: int) -> int:
        print('Calculating with new tax regime!')
        if total > 1500000:
            return int(0.3*(total-1500000)) + int(2.5*500000)
        if total > 1000000:
            return int(2.5*(total-1000000))
        return 0


class TaxCalculator:
    def __init__(self):
        self.regime = None

    def set_regime(self, regime: Regime):
        self.regime = regime

    def calculate(self, gross_amount: int) -> int:
        calculator = None
        if self.regime == Regime.OLD:
            calculator = OldTaxRegime()

        elif self.regime == Regime.NEW:
            calculator = NewTaxRegime()

        return calculator.calculate_tax(gross_amount)


if __name__ == '__main__':
    tax_calculator = TaxCalculator()

    tax_calculator.set_regime(Regime.OLD)
    print(tax_calculator.calculate(1200000))

    tax_calculator.set_regime(Regime.NEW)
    print(tax_calculator.calculate(1200000))



