## Introduction

Anything that can be automated, should be automated.

### R package component

- R code: the most important directory is R/, where your R code lives. 
- Package metadata: the DESCRIPTION lets you describe what your package needs to work. 
- Documentation: if you want other people (including future-you!) to understand how to use the functions in your package, you’ll need to document them.
- Vignettes: function documentation describes the nit-picky details of every function in your package.
- Tests: to ensure your package works as designed (and continues to work as you make changes), it’s essential to write unit tests which define correct behaviour, and alert you when functions break. 
- Namespace: to play nicely with others, your package needs to define what functions it makes available to other packages and what functions it requires from other packages. 
- External data: the data/ directory allows you to include data with your package. 
- Compiled code: R code is designed for human efficiency, not computer efficiency, so it’s useful to have a tool in your back pocket that allows you to write fast code. The src/ directory allows you to include speedy compiled C and C++ code to solve performance bottlenecks in your package.


## Package structure

### Create a package

1. File | New Project.
2. New Directory
3. R Package
4. Create Project

or

```R
devtools::create("path/to/package/pkgname")
```

## R code

### R code workflow

1. Edit an R file.

2. Press Ctrl/Cmd + Shift + L.

3. Explore the code in the console.

4. Rinse and repeat.

### When you do need side-effects

Occasionally, packages do need side-effects. This is most common if your package talks to an external system — you might need to do some initial setup when the package loads. To do that, you can use two special functions: .onLoad() and .onAttach(). 




