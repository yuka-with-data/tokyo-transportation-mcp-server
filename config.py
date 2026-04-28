""" 
Transit backend config toggle

USE_EXPERIMENTAL controls which data source is used for route calculations.
- True: Uses experimental scraping-based implementation
        (temporary, unstable, not production-safe)
- False: Uses structured / stable data source implementation
        (e.g., ODPT, publicly available, open sourced data)

 """
USE_EXPERIMENTAL = False