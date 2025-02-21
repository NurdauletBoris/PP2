from datetime import datetime

date1 = datetime(2025, 2, 22, 12, 0, 0)
date2 = datetime(2025, 2, 23, 14, 30, 0)

difference = (date2 - date1).total_seconds()

print("Difference in seconds:", difference)
