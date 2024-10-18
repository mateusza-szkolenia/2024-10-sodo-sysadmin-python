"""
,

"""

# import dataclasses
# @dataclasses.dataclass


from dataclasses import dataclass, field

@dataclass
class Lotnisko:
    name: str
    continent: str = None
    iso_country: str = None
    municipality: str = None
    iata_code: str = None
    icao_code: str = None
    gps: list[float] = field(default_factory=list)

    def hej(self):
        print(f"Hej jestem w {self.iso_country}")

    @staticmethod
    def qwe():
        print("OK")

    @classmethod
    def from_dict(cls, data: dict) -> 'Lotnisko':
        nowe_lotnisko = cls(**data)

        return nowe_lotnisko

dict_lot =   {
    "name": "Warsaw Chopin Airport",
    "continent": "EU",
    "iso_country": "PL",
    "municipality": "Warsaw",
    "iata_code": "WAW",
    "icao_code": "EPWA",
    "gps": [
      52.165699,
      20.9671
    ]
  }

l1 = Lotnisko("Warszawa", "EU", "PL", "Warsawa", "WAW", "EPWA", [52,21])
