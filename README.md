# Markdown LaTeX

This is a Python script that looks for a README written with Markdown + ![equation](http://latex.codecogs.com/png.latex?%24%24%5CLaTeX%24%24) and outputs a README.md with the ![equation](http://latex.codecogs.com/png.latex?%24%24%5CLaTeX%24%24) equations replaced by images rendered by [CodeCogs].

You can use it with other Markdown files, just pass the path to the file as an argument to the script:

```
python insert_equations.py [MARKDOWN_FILE_PATH]
```

## How to write the equations

To type the equations in the original document, just put them between double dolar signs ($). This is standard, just don't put any newline beetween the double solar signs.

As an example, this is a README.md generated by the README in this repo using that script, so we can type things like this:

![equation](http://latex.codecogs.com/png.latex?%24%24%20J%28%5Cmathbf%7BW_1%7D%2C%20%5Cmathbf%7Bb_1%7D%2C%20%5Cmathbf%7BW_2%7D%2C%20%5Cmathbf%7Bb_2%7D%29%20%3D%20%5Cfrac%7B1%7D%7B2t%7D%5Cmathbf%7B1_v%7D%5ET%20%5Ccdot%20%5B%28%28%5Cmathbf%7Ba_3%7D%20-%20%5Cmathbf%7BX%7D%29%20%5Codot%20%28%5Cmathbf%7Ba_3%7D%20-%20%5Cmathbf%7BX%7D%29%29%20%5Ccdot%20%5Cmathbf%7B1_t%7D%5D%20%2B%20%5Cfrac%7B%5Clambda%7D%7B2%7D%5B%5Cmathbf%7B1_h%7D%5ET%20%5Ccdot%20%28%5Cmathbf%7BW_1%7D%5Codot%20%5Cmathbf%7BW_1%7D%29%20%5Ccdot%20%5Cmathbf%7B1_v%7D%20%2B%20%5Cmathbf%7B1_v%7D%5ET%20%5Ccdot%20%28%5Cmathbf%7BW_2%7D%5Codot%20%5Cmathbf%7BW_2%7D%29%20%5Ccdot%20%5Cmathbf%7B1_h%7D%20%5D%20%2B%20%5Cbeta%5Cmathbf%7B1_h%7D%5ET%20%5Ccdot%20%5B%5Crho%20%5Clog%28%5Crho%5Cmathbf%7B1_h%7D%20%5Coslash%20%5Cboldsymbol%7B%5Chat%20%5Crho%7D%29%20%2B%20%281%20-%20%5Crho%29%5Clog%28%28%5Cmathbf%7B1_h%7D-%5Crho%5Cmathbf%7B1_h%7D%29%20%5Coslash%20%28%5Cmathbf%7B1_h%7D%20-%20%5Cboldsymbol%7B%5Chat%20%5Crho%7D%29%29%5D%24%24).

Now compare the README and the raw version of this README.md.

That's a simple way to write equations here in Github. 

Have ![equation](http://latex.codecogs.com/png.latex?%24%24f%20%5Ccup%20%5Cmathbb%7BN%7D%24%24)! 

[CodeCogs]:http://www.codecogs.com/latex/eqneditor.php