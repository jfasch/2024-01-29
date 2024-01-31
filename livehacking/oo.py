import collections
from datetime import datetime

Messwert = collections.namedtuple('Messwert', ('timestamp', 'wert1', 'wert2'))
mw_a = Messwert(
    timestamp = datetime(year=2024, month=1, day=31, hour=14, minute=30),
    wert2 = [5, 6, 7, 8],
    wert1 = [1, 2, 3, 4],
)
print(mw_a.timestamp, mw_a.wert1, mw_a.wert2)
