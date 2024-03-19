<h1>Image Color Extractor</h1>

  <p>This Python script extracts colors from an image using the <code>colorgram</code> library. It reads an image file, extracts the prominent colors, and stores them in a list of RGB tuples.</p>

  <h2>Installation</h2>

  <ol>
    <li>Ensure you have Python installed on your system. You can download Python from the official website: <a
        href="https://www.python.org/downloads/">python.org</a>.</li>
    <li>Install the <code>colorgram</code> library using pip:
      <pre><code>pip install colorgram.py</code></pre>
    </li>
  </ol>

  <h2>Usage</h2>

  <ol>
    <li>Place your image file (e.g., <code>image.jpg</code>) in the same directory as the Python script (<code>extract_colors.py</code>).</li>
    <li>Update the file name in the script to match your image file name:
      <pre><code>colors = colorgram.extract("image.jpg", 300)</code></pre>
    </li>
    <li>Run the script using the following command:
      <pre><code>python extract_colors.py</code></pre>
    </li>
    <li>The script will extract the colors from the image and print the RGB tuples of the extracted colors.</li>
  </ol>

  <h2>Example Output</h2>

  <p>After running the script, you'll see the extracted colors printed in the console. Here's an example of the output:</p>
  <pre><code>[(237, 245, 255), (52, 68, 86), (152, 178, 197), (86, 142, 184), (35, 101, 149), ...]</code></pre>

  <h2>Dependencies</h2>

  <ul>
    <li>Python 3.x</li>
    <li>colorgram.py</li>
  </ul>

  <h2>Contributing</h2>

  <p>Contributions are welcome! If you have any suggestions, bug fixes, or improvements for the script, feel free to submit
    a pull request or open an issue on GitHub.</p>

  <h2>License</h2>

  <p>This Image Color Extractor script is released under the <a href="LICENSE">MIT License</a>.</p>
