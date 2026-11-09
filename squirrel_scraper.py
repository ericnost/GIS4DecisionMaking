# Written with assistance from Google Gemini
# ### DRAFT
# import pandas as pd
from arcgis.gis import GIS

# 1. Connect to your ArcGIS Online organization
# Replace with your AGOL URL and credentials (or use profile='your_profile')
gis = GIS("https://www.arcgis.com", "your_username", "your_password")

# 2. Find the target group by name/title
group_title = "Your_AGOL_Group_Name"
groups = gis.groups.search(f'title: "{group_title}"')

if not groups:
    raise ValueError(f"Group '{group_title}' not found.")

target_group = groups[0]
print(f"Found group: {target_group.title} (ID: {target_group.id})")

# 3. Retrieve all items in the group filtered by Feature Service / Feature Layer
group_items = target_group.content(item_type="Feature Service")
print(f"Found {len(group_items)} hosted feature service item(s) in group.")

compiled_data = {}
master_dfs = []

# 4. Iterate through each feature service/layer and query the data
for item in group_items:
    print(f"Processing item: {item.title} ({item.id})")
    
    # A feature service item can contain multiple layers
    for layer in item.layers:
        layer_name = f"{item.title}_{layer.properties.name}"
        try:
            # Query all records into a Spatially Enabled DataFrame (.sdf)
            # Use .query().df if using standard pandas / spatial dataframe
            sdf = layer.query().sdf
            
            if not sdf.empty:
                # Optional: Add metadata columns tracking the source item and layer
                sdf['source_item_id'] = item.id
                sdf['source_title'] = item.title
                sdf['layer_name'] = layer.properties.name
                
                compiled_data[layer_name] = sdf
                master_dfs.append(sdf)
                print(f"  -> Extracted {len(sdf)} rows from layer: {layer.properties.name}")
            else:
                print(f"  -> Layer {layer.properties.name} is empty.")
                
        except Exception as e:
            print(f"  -> Error querying layer {layer.properties.name}: {e}")

# 5. Combine all layers into a single master DataFrame (if schema compatible)
if master_dfs:
    # ignore_index resets index across combined layers
    master_compiled_df = pd.concat(master_dfs, ignore_index=True)
    print(f"\nCompilation complete. Total combined rows: {len(master_compiled_df)}")
    
    # Example: Export compiled data to a local CSV or File Geodatabase
    # master_compiled_df.spatial.to_table(r"C:\path\to\local.gdb\compiled_table")
    # master_compiled_df.drop(columns=['SHAPE']).to_csv("compiled_data.csv", index=False)
else:
    print("\nNo data was compiled.")
