import numpy as np
import matplotlib.pyplot as plt
import cv2

def sierpinski_triangle(image, x1, y1, x2, y2, x3, y3, depth, color=(255, 255, 255)):
    """
    Generate Sierpinski Triangle using recursion
    
    Parameters:
    - image: numpy array representing the image
    - x1, y1: coordinates of first vertex
    - x2, y2: coordinates of second vertex  
    - x3, y3: coordinates of third vertex
    - depth: recursion depth (number of iterations)
    - color: RGB color tuple for drawing
    """
    
    # Base case: stop recursion when depth reaches 0
    if depth == 0:
        # Draw the triangle outline
        points = np.array([[int(x1), int(y1)], 
                          [int(x2), int(y2)], 
                          [int(x3), int(y3)]], np.int32)
        cv2.polylines(image, [points], True, color, 1)
        return
    
    # Calculate midpoints of each side
    mid12_x = (x1 + x2) / 2  # Midpoint of side 1-2
    mid12_y = (y1 + y2) / 2
    
    mid23_x = (x2 + x3) / 2  # Midpoint of side 2-3
    mid23_y = (y2 + y3) / 2
    
    mid31_x = (x3 + x1) / 2  # Midpoint of side 3-1
    mid31_y = (y3 + y1) / 2
    
    # Recursive calls for three smaller triangles
    # Top triangle
    sierpinski_triangle(image, x1, y1, mid12_x, mid12_y, mid31_x, mid31_y, depth-1, color)
    
    # Bottom-right triangle
    sierpinski_triangle(image, mid12_x, mid12_y, x2, y2, mid23_x, mid23_y, depth-1, color)
    
    # Bottom-left triangle  
    sierpinski_triangle(image, mid31_x, mid31_y, mid23_x, mid23_y, x3, y3, depth-1, color)

def generate_sierpinski(width=800, height=600, depth=6, save_file=True):
    """
    Generate and display Sierpinski Triangle
    
    Parameters:
    - width, height: image dimensions
    - depth: recursion depth (recommended: 4-8)
    - save_file: whether to save the image as PNG
    """
    
    # Create blank black image
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Define triangle vertices (equilateral triangle)
    margin = 50
    center_x = width // 2
    triangle_height = height - 2 * margin
    triangle_width = int(triangle_height * 2 / np.sqrt(3))  # For equilateral triangle
    
    # Calculate vertices for centered equilateral triangle
    x1 = center_x  # Top vertex
    y1 = margin
    
    x2 = center_x - triangle_width // 2  # Bottom-left vertex
    y2 = height - margin
    
    x3 = center_x + triangle_width // 2  # Bottom-right vertex
    y3 = height - margin
    
    print(f"Generating Sierpinski Triangle with depth {depth}...")
    print(f"Triangle vertices: ({x1}, {y1}), ({x2}, {y2}), ({x3}, {y3})")
    
    # Generate the fractal
    sierpinski_triangle(image, x1, y1, x2, y2, x3, y3, depth, (255, 255, 255))
    
    # Display the image
    plt.figure(figsize=(12, 8))
    plt.imshow(image)
    plt.title(f'Sierpinski Triangle - Depth {depth}\n(Recursive Fractal Algorithm)', 
              fontsize=16, fontweight='bold', color='white', pad=20)
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    
    # Save the image
    if save_file:
        filename = f"sierpinski_triangle_depth_{depth}.png"
        cv2.imwrite(filename, image)
        print(f"Image saved as: {filename}")
    
    return image

def generate_colored_sierpinski(width=800, height=600, depth=6):
    """
    Generate colorful Sierpinski Triangle with different colors for each recursion level
    """
    
    # Create blank black image
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Define colors for different recursion levels
    colors = [
        (255, 0, 0),    # Red
        (255, 165, 0),  # Orange  
        (255, 255, 0),  # Yellow
        (0, 255, 0),    # Green
        (0, 255, 255),  # Cyan
        (0, 0, 255),    # Blue
        (255, 0, 255),  # Magenta
        (255, 255, 255) # White
    ]
    
    def colored_sierpinski(image, x1, y1, x2, y2, x3, y3, depth, original_depth):
        if depth == 0:
            # Use different color based on current depth
            color_index = (original_depth - depth) % len(colors)
            color = colors[color_index]
            
            points = np.array([[int(x1), int(y1)], 
                              [int(x2), int(y2)], 
                              [int(x3), int(y3)]], np.int32)
            cv2.polylines(image, [points], True, color, 2)
            return
        
        # Calculate midpoints
        mid12_x, mid12_y = (x1 + x2) / 2, (y1 + y2) / 2
        mid23_x, mid23_y = (x2 + x3) / 2, (y2 + y3) / 2
        mid31_x, mid31_y = (x3 + x1) / 2, (y3 + y1) / 2
        
        # Recursive calls
        colored_sierpinski(image, x1, y1, mid12_x, mid12_y, mid31_x, mid31_y, depth-1, original_depth)
        colored_sierpinski(image, mid12_x, mid12_y, x2, y2, mid23_x, mid23_y, depth-1, original_depth)
        colored_sierpinski(image, mid31_x, mid31_y, mid23_x, mid23_y, x3, y3, depth-1, original_depth)
    
    # Setup triangle vertices
    margin = 50
    center_x = width // 2
    triangle_height = height - 2 * margin
    triangle_width = int(triangle_height * 2 / np.sqrt(3))
    
    x1, y1 = center_x, margin
    x2, y2 = center_x - triangle_width // 2, height - margin
    x3, y3 = center_x + triangle_width // 2, height - margin
    
    print(f"Generating Colored Sierpinski Triangle with depth {depth}...")
    
    # Generate colored fractal
    colored_sierpinski(image, x1, y1, x2, y2, x3, y3, depth, depth)
    
    # Display
    plt.figure(figsize=(12, 8))
    plt.imshow(image)
    plt.title(f'Colored Sierpinski Triangle - Depth {depth}\n(Each Level in Different Color)', 
              fontsize=16, fontweight='bold', color='white', pad=20)
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    
    # Save
    filename = f"sierpinski_triangle_colored_depth_{depth}.png"
    cv2.imwrite(filename, image)
    print(f"Colored image saved as: {filename}")
    
    return image

def demonstrate_recursion_levels():
    """
    Demonstrate how Sierpinski triangle evolves with different recursion depths
    """
    depths = [1, 2, 3, 4, 5, 6]
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Sierpinski Triangle Evolution - Different Recursion Depths', 
                 fontsize=16, fontweight='bold')
    
    for i, depth in enumerate(depths):
        row = i // 3
        col = i % 3
        
        # Generate smaller image for subplot
        image = np.zeros((300, 400, 3), dtype=np.uint8)
        
        # Triangle setup
        x1, y1 = 200, 30
        x2, y2 = 50, 270
        x3, y3 = 350, 270
        
        sierpinski_triangle(image, x1, y1, x2, y2, x3, y3, depth, (255, 255, 255))
        
        axes[row, col].imshow(image)
        axes[row, col].set_title(f'Depth {depth}')
        axes[row, col].axis('off')
    
    plt.tight_layout()
    plt.show()

# Main execution
if __name__ == "__main__":
    print("Sierpinski Triangle Generator")
    print("=" * 40)
    
    # Generate basic Sierpinski Triangle
    print("\n1. Basic Sierpinski Triangle:")
    generate_sierpinski(width=800, height=600, depth=6)
    
    # Generate colored version
    print("\n2. Colored Sierpinski Triangle:")
    generate_colored_sierpinski(width=800, height=600, depth=5)
    
    # Demonstrate different recursion levels
    print("\n3. Recursion Level Demonstration:")
    demonstrate_recursion_levels()
    
    print("\n" + "=" * 40)
    print("Generation complete!")
    print("Files saved:")
    print("- sierpinski_triangle_depth_6.png")
    print("- sierpinski_triangle_colored_depth_5.png")