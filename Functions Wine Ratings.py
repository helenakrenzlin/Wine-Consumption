Functions WineRatings

def clean_wine_locations(df_input):
    # 1. Use the original column that has the dot (likely called 'location')
    # We create a copy so we don't accidentally break the original data
    df_input['location'] = df_input['location'].astype(str)

    # 2. Split the 'location' column at the dot
    split_data = df_input['location'].str.split('·', n=1, expand=True)

    # 3. SAFETY CHECK
    if len(split_data.columns) > 1:
        df_input['country'] = split_data[0].str.strip()
        df_input['region'] = split_data[1].str.strip()
    else:
        df_input['region'] = "General"
        df_input['country'] = split_data[0].str.strip()

    return df_input

----

def global_big_data_clean(df, column):
    # 1. Basic Formatting: Clean spaces and force lowercase for matching
    df[column] = df[column].astype(str).str.lower().str.strip()

    # 2. Define Universal Anchors (Covers major variations)
    # The '|' symbol acts as 'OR'
    anchors = {
        'USA': 'states|u.s.|napa|california|america|us',
        'France': 'fran|bordeaux|provence|rhone|burgundy',
        'Italy': 'ital|piemonte|toscana|veneto|sicily',
        'Spain': 'spain|espa|rioja|cava',
        'United Kingdom': 'england|britain|uk|london',
        'New Zealand': 'zealand|marlborough|nz',
        'South Africa': 'africa',
        'Argentina': 'argen|mendoza',
        'Portugal': 'portu|douro'
    }

    # 3. Apply Anchor Loop
    for clean_name, pattern in anchors.items():
        mask = df[column].str.contains(pattern, na=False, regex=True)
        df.loc[mask, column] = clean_name

    # 4. The "Catch-All": Title Case for the rest
    # This automatically fixes 'georgia' -> 'Georgia', 'moldova' -> 'Moldova', etc.
    df[column] = df[column].str.title()
    
    # 5. Final Acronym Fixes
    df[column] = df[column].replace({'Usa': 'USA', 'Uk': 'UK', 'Nan': 'Unknown', '': 'Unknown'})

    return df

---
def simple_clean(text):
    if pd.isna(text): return ""
    return str(text).lower().strip().replace("winery", "").replace("vineyards", "").strip()

def get_match(name, choices):
    if not name: return None
    matches = difflib.get_close_matches(name, choices, n=1, cutoff=0.6)
    return matches[0] if matches else None

---
def get_wine_type(variety):
    v = str(variety).lower()
    
    # Define keywords for each group
    if any(word in v for word in ['chardonnay', 'blanc', 'grigio', 'riesling', 'white', 'gris']):
        return 'White'
    elif any(word in v for word in ['noir', 'cabernet', 'merlot', 'syrah', 'red', 'malbec', 'tempranillo']):
        return 'Red'
    elif any(word in v for word in ['rosé', 'rose']):
        return 'Rosé'
    elif any(word in v for word in ['sparkling', 'champagne', 'cava', 'prosecco']):
        return 'Sparkling'
    elif any(word in v for word in ['port', 'sherry', 'dessert', 'late harvest']):
        return 'Dessert/Fortified'
    else:
        return 'Other'

---
