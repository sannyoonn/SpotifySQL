import pandas as pd
df = pd.read_json(r'/Users/sanyoon/Documents/cs/spotify_data.json')
export_csv = df.to_csv(r'/Users/sanyoon/Documents/cs/spotify_data.csv', index = None, header=True)