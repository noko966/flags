from PIL import Image
import csv
import os

# Define paths
spriteFileName = "flags"
small_sprite_size = 20
src_folder_path = "spriteSrc"
dist_folder_path = "spriteDist"
csv_file_path = "mapping.csv"
sprite_folder_path = os.path.join(dist_folder_path, "sprite")
css_file_path = os.path.join(sprite_folder_path, "style.css")
html_file_path = os.path.join(sprite_folder_path, "index.html")

# Ensure the sprite directory exists
if not os.path.exists(sprite_folder_path):
    os.makedirs(sprite_folder_path)

# Read the CSV file to get the order and filenames
ordered_filenames = []
with open(csv_file_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        key = row[1]  # Assuming the second column is the key
        filename = f"{key}.png"
        ordered_filenames.append(filename)

# Determine the size of each image (assuming all images are the same size)
img_width, img_height = 24, 24  # Adjust if different

# Load images in the specified order and calculate the total height of the sprite
images = [Image.open(os.path.join(src_folder_path, filename)) for filename in ordered_filenames]
total_height = img_height * len(images)

# Create a new image for the sprite
sprite_image = Image.new('RGBA', (img_width, total_height))

# Initial CSS content
css_content = f""".cHFlag {{
    flex-shrink: 0;
    background-repeat: no-repeat;
    background-image: url("{spriteFileName}.png");
    background-position: 0 -3624px;
    width: {img_width}px;
    height: {img_height}px;
    background-size: {img_width}px {total_height}px;
    overflow: hidden;
}}
"""

# Add CSS for smaller sprite display
css_content_sm = f""".cHFlagSm {{
    flex-shrink: 0;
    background-repeat: no-repeat;
    background-image: url("{spriteFileName}.png");
    background-position: 0 -3624px;
    width: 20px;
    height: 20px;
    background-size: {int(img_width * (small_sprite_size / img_width))}px {int(total_height * (small_sprite_size / img_height))}px;
    overflow: hidden;
}}
"""

# Initial HTML content
html_content = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
    <style>
        *{{
            box-sizing: border-box;
        }}
        .flag_block{{
            background-color: #121212;
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 24px;
            border: 1px solid #181818;
            flex-wrap: wrap;
        }}
    </style>
    <body>
"""

html_medium_sprites = f"""<div class="flag_block">
"""

html_small_sprites = f"""<div class="flag_block">
"""

# Paste each image into the sprite and add CSS rules
current_y = 0
for filename, img in zip(ordered_filenames, images):
    sprite_image.paste(img, (0, current_y))

    # Extract the base name without the extension for CSS class
    base_name = os.path.splitext(filename)[0]
    cssClass_suffix = f"f{base_name}"
    cssClass_suffix_sm = f"fsm{base_name}"

    # Generate CSS for this item
    css_content += f".{cssClass_suffix} {{\n"
    css_content += f"    background-position: 0 -{current_y}px;\n"
    css_content += "}\n"

    css_content_sm += f".{cssClass_suffix_sm} {{\n"
    css_content_sm += f"    background-position: 0 -{int(current_y * (small_sprite_size / img_height))}px;\n"
    css_content_sm += "}\n"


    html_medium_sprites += f"<div class='cHFlag {cssClass_suffix}'></div>"
    html_small_sprites += f"<div class='cHFlagSm {cssClass_suffix_sm}'></div>"

    # Update y_position for the next image
    current_y += img_height

# Save the sprite image
sprite_path = os.path.join(sprite_folder_path, f"{spriteFileName}.png")
sprite_image.save(sprite_path)
print("Vertical sprite created successfully.")

css_content += css_content_sm

# Write CSS file
with open(css_file_path, 'w') as css_file:
    css_file.write(css_content)
print("CSS file has been created successfully.")


# end of HTML content

html_medium_sprites += f"""
    </div>
"""

html_small_sprites += f"""
    </div>
"""

html_content += f"""
        {html_medium_sprites}
        {html_small_sprites}
    </body>
</html>
"""

# Write HTML file
with open(html_file_path, 'w') as html_file:
    html_file.write(html_content)
print("HTML file has been created successfully.")
