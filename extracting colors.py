import colorgram

# Extract colors from the image
colors = colorgram.extract("images.jpg", 300)

# Create an empty list to store the extracted colors
image_colors = []

# Iterate over each color extracted
for item in colors:
    # Extract the RGB values
    r = item.rgb.r
    g = item.rgb.g
    b = item.rgb.b
    
    # Create a new color tuple
    new_color = (r, g, b)
    
    # Append the new color to the list
    image_colors.append(new_color)

# Print the extracted colors
print(image_colors)
