# Data analysis
    #sudo -H pip3 install pandas

#!/usr/bin/env python3
import pandas
visitors = [1235, 6424, 9345, 8464, 2345]
errors = [23, 45,33, 45, 76]

#generate the DataFrame
df = pandas.DataFrame( {"visitors": visitors, "errors": errors}, index=["Mon", "Tues", "Wed", "Thu", "Fri"] )

print(df)

print(df["errors"].mean())
