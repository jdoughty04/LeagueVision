from PIL import Image
import os
import random

def create_augmented_data(map_dir, icons_dir, output_dir, labels_dir, num_images, max_icons, icon_width, icon_height, map_width, map_height):
    # Function to generate data, also prints the icon names and their keys

    # Ensure output directories exist
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(labels_dir, exist_ok=True)

    # Load and resize the map image
    map_image_path = os.path.join(map_dir, os.listdir(map_dir)[0])
    map_image = Image.open(map_image_path).resize((map_width, map_height), Image.Resampling.LANCZOS)
    map_image_base = map_image.copy()

    # Load, resize icons and create a mapping to unique keys
    icon_images = {}
    for icon_file in os.listdir(icons_dir):
        if os.path.isfile(os.path.join(icons_dir, icon_file)):
            with Image.open(os.path.join(icons_dir, icon_file)) as icon:
                icon_images[icon_file.rsplit('.', 1)[0]] = icon.resize((icon_width, icon_height), Image.Resampling.BILINEAR)
    icon_keys = {icon_name: i for i, icon_name in enumerate(icon_images)}

    # Print each icon's name along with its assigned key
    for icon_name, key in icon_keys.items():
        print(f"Icon: {icon_name}, Key: {key}")

    for i in range(num_images):
        map_image = map_image_base.copy()

        # File for storing labels
        label_file_path = os.path.join(labels_dir, f"img_{i}.txt")
        with open(label_file_path, 'w') as label_file:

            # Randomly select and place icons
            for _ in range(random.randint(1, max_icons)):
                icon_name = random.choice(list(icon_images.keys()))
                icon_key = icon_keys[icon_name]
                resized_icon = icon_images[icon_name]

                # Random position for the center of the icon
                center_x = random.randint(icon_width // 2, map_width - icon_width // 2)
                center_y = random.randint(icon_height // 2, map_height - icon_height // 2)

                # Top-left corner position
                x = center_x - icon_width // 2
                y = center_y - icon_height // 2

                # Normalize center coordinates
                normalized_x = center_x / map_width
                normalized_y = center_y / map_height

                # Overlay icon onto the map image
                map_image.paste(resized_icon, (x, y), resized_icon)

                # Write label with space-separated values, including the two additional zeroes
                label_file.write(f"{icon_key} {normalized_x:.2f} {normalized_y:.2f} 0.15 0.15\n")

        # Save the augmented image
        augmented_image_path = os.path.join(output_dir, f"img_{i}.png")
        map_image.save(augmented_image_path)


map_dir = 'map'
icons_dir = 'Icons'
output_dir = 'images'
labels_dir = 'labels'
num_images = 50000
max_icons = 5
icon_width = 300 
icon_height = 170
map_width = 640  
map_height = 640  


create_augmented_data(map_dir, icons_dir, output_dir, labels_dir, num_images, max_icons, icon_width, icon_height, map_width, map_height)