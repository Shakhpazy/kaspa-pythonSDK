
class Conversions:
    @staticmethod
    def sompi_to_kaspa(sompi: int) -> float:
        return sompi / 100_000_000

    @staticmethod
    def kaspa_to_sompi(kaspa: float) -> int:
        return int(kaspa * 100_000_000)