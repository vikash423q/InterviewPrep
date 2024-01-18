from abc import ABC, abstractmethod


class Table(ABC):
    pass


class Chair(ABC):
    pass


class Sofa(ABC):
    pass


class ModernTable(Table):
    pass


class ModernChair(Chair):
    pass


class ModernSofa(Sofa):
    pass


class VictorianTable(Table):
    pass


class VictorianChair(Chair):
    pass


class VictorianSofa(Sofa):
    pass


class Furniture(ABC):
    @abstractmethod
    def create_table(self) -> Table:
        pass

    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

    def create_set(self):
        table = self.create_table()
        chair = self.create_chair()
        sofa = self.create_sofa()

        print(f'Prepared set of furniture - {[table, chair, sofa]}')


class ModernFurniture(Furniture):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()

    def create_sofa(self) -> Sofa:
        return ModernSofa()


class VictorianFurniture(Furniture):
    def create_table(self) -> Table:
        return VictorianTable()

    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


if __name__ == '__main__':
    furniture = ModernFurniture()
    furniture.create_set()

    furniture = VictorianFurniture()
    furniture.create_set()
