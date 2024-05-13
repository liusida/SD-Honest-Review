import os

# Path to the directory containing the subfolders with images
root_path = '.'

# Start of the HTML file
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Model Image Gallery</title>
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 20px;
    }
    .category {
        margin-bottom: 30px;
    }
    .category-name {
        font-size: 1.2em;
        margin: 20px 0;
        color: #333;
    }
    .image-gallery {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
    }
    .image-gallery div {
        margin: 10px;
        text-align: center;
    }
    img {
        width: 100%;
        max-width: 300px;
        height: auto;
        border: 1px solid #ccc;
        box-shadow: 2px 2px 6px 0px rgba(0,0,0,0.1);
    }
    p {
        margin: 4px 0;
        font-size: 0.9em;
        color: #333;
    }
</style>
</head>
<body>
<h1>Model Image Gallery</h1>
'''

# Traverse the directory structure
for subdir, dirs, files in os.walk(root_path):
    if files:  # Ensure there are images in the subdirectory
        category_name = os.path.basename(subdir)  # Subfolder name as category name
        html_content += f'<div class="category"><h2 class="category-name">{category_name}</h2><div class="image-gallery">'

        for file in files:
            # Check for image files (by extension)
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                file_path = os.path.join(subdir, file)
                relative_path = os.path.relpath(file_path, start=root_path)
                html_content += f'''
                <div>
                    <img src="{relative_path}" alt="{file}">
                    <p>{file}</p>
                </div>
                '''
        html_content += '</div></div>'

# End of the HTML file
html_content += '''
</body>
</html>
'''

# Write the HTML content to the index.html file
with open('index.html', 'w') as file:
    file.write(html_content)

print("index.html has been generated successfully!")