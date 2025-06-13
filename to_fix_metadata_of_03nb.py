import nbformat

notebook_path = "03_computer_vision_pytorch.ipynb"

# Load the notebook
nb = nbformat.read(notebook_path, as_version=4)

# Delete the bad metadata
if 'widgets' in nb['metadata']:
    del nb['metadata']['widgets']

# Save the notebook back
nbformat.write(nb, notebook_path)

print("Fixed notebook.")
