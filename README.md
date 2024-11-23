### README: Plotting the "Selamat Hari Guru 2024" Visualization

This Python script generates a custom plot in celebration of *Hari Guru 2024*. The plot includes a combination of geometric and algebraic elements such as vertical lines, horizontal segments, linear equations, parabolas, and circles, arranged artistically to create a visually appealing tribute.

---

### **File Overview**
- **Script Purpose**: Generate a customized mathematical visualization that displays "Selamat Hari Guru 2024" with artistic line and curve elements.
- **Libraries Used**:
  - `numpy`: For numerical calculations, including generating sequences for function plotting.
  - `matplotlib.pyplot`: For creating and customizing the plot.

---

### **Elements of the Plot**
The visualization is composed of the following components:

#### 1. **Vertical Lines**
- Defined by a series of coordinates `(x, ymin, ymax)`.
- Plotted using `plt.vlines`, where each line spans vertically from `ymin` to `ymax` at the x-coordinate `x`.

#### 2. **Horizontal Segments**
- Defined by tuples `(x_start, x_end, y)`.
- Plotted as horizontal lines at a constant `y` value between `x_start` and `x_end` using `plt.plot`.

#### 3. **Linear Segments**
- Represented as straight lines using functions in the form \( y = f(x) \).
- Defined by start and end intervals `[start, end]` and a lambda function for `y=f(x)`.
- Plotted using `numpy.linspace` for generating x-values and applying the function `f(x)` to compute y-values.

#### 4. **Parabolas**
- Two parabolas are plotted:
  - First parabola: \( x = -3.2(y + 3.5)^2 - 4.1 \)
  - Second parabola: \( x = -3.2(y + 3.5)^2 + 0.9 \)
- Special masking is applied using `numpy.where` to limit the visible portions of the second parabola for aesthetic purposes.

#### 5. **Circles**
- Two semicircles (top and bottom) are created using trigonometric equations:
  - \( x = \cos(\theta) - 6 \)
  - \( y = \sin(\theta) \)
- Masking ensures that only specific portions of the circles are visible.

---

### **Key Functions and Their Role**
- **`plt.vlines(x, ymin, ymax, color, linewidth)`**: Draws vertical lines.
- **`plt.plot(x, y, color, linewidth)`**: Plots a line or curve given `x` and `y` coordinates.
- **`numpy.linspace(start, end, num)`**: Generates evenly spaced values in a given range.
- **`numpy.where(condition, x, y)`**: Masks data by replacing values where a condition is false.

---

### **Visualization Layout**
- **Figure Size**: `12 x 10` inches for clarity and balance.
- **Grid**: Enabled to guide the viewer.
- **Axis Labels**: Labeled as `x` and `y`.
- **Title**: "Selamat Hari Guru 2024."
- **Axis Bounds**:
  - \( x \): From `-8` to `8`.
  - \( y \): From `-6` to `4`.

---

### **How to Run the Script**
1. **Prerequisites**:
   - Python installed on your system.
   - Required libraries: `numpy` and `matplotlib`. Install them using:
     ```bash
     pip install numpy matplotlib
     ```
2. **Run the Script**:
   Save the script as `selamat_hari_guru.py` and execute it using:
   ```bash
   python selamat_hari_guru.py
   ```

---

### **Customizing the Plot**
- **Adding New Shapes**:
  - Vertical and horizontal lines: Append tuples to `vertical_lines` or `horizontal_segments`.
  - Linear equations: Add new intervals and lambda functions to `linear_segments`.
  - Parabolas and circles: Modify the equations for the desired transformations.
- **Colors and Styles**:
  - Change the `color` or `linewidth` parameters in the plotting functions for different styles.

---

### **Output**
Running the script will generate a detailed plot that combines mathematical artistry and programming to celebrate Hari Guru 2024. The plot will be displayed in a pop-up window and can be saved as an image using the `matplotlib` save functionality (e.g., `plt.savefig("hari_guru_2024.png")`).

Enjoy the visual representation of mathematics and creativity!
