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

```R

.onLoad <- function(libname, pkgname) {
  op <- options()
  op.devtools <- list(
	devtools.path = "~/R-dev",
	devtools.install.args = "",
	devtools.name = "Your name goes here",
	devtools.desc.author = "First Last <first.last@example.com> [aut, cre]",
	devtools.desc.license = "What license is it under?",
	devtools.desc.suggests = NULL,
	devtools.desc = list()
	)
	toset <- !(names(op.devtools) %in% names(op))
	if(any(toset)) options(op.devtools[toset])
	
	invisible()
}

```

## Package metadata

The job of the DESCRIPTION file is to store important metadata about your package. 

### Dependencies: What does your package need?

It’s the job of the DESCRIPTION to list the packages that your package needs to work. 

- Imports: packages listed here must be present for your package to work. 
- Suggests: your package can use these packages, but doesn’t require them. 


```R

## Example need suggests
## There's a fallback method if the package isn't available
my_fun <- function(a, b) {
	if (requireNamespace("pkg", quietly = TRUE)) {
		pkg::f()
	} else {
		g()
	}
}


```

```R
## Adding ggplot2 to Imports
usethis::use_package("ggplot2")

## Adding RColorBrewer to Suggests 
usethis::use_package("RColorBrewer", "Suggests")

```

## Object documentation

### The documentation workflow

1. Add roxygen comments to your .R files.

2. Run devtools::document() (or press Ctrl/Cmd + Shift + D in RStudio) to convert roxygen comments to .Rd files. (devtools::document() calls roxygen2::roxygenise() to do the hard work.)

3. Preview documentation with ?.

4. Rinse and repeat until the documentation looks the way you want.

### Roxygen comments

- The first sentence becomes the title of the documentation. 
- The second paragraph is the description: this comes first in the documentation and should briefly describe what the function does.
- The third and subsequent paragraphs go into the details.

```R
#' Sum of vector elements.
#' 
#' \code{sum} returns the sum of all the values present in its arguments.
#' 
#' This is a generic function: methods can be defined for it directly or via the
#' \code{\link{Summary}} group generic. For this to work properly, the arguments
#' \code{...} should be unnamed, and dispatch is on the first argument.
sum <- function(..., na.rm = TRUE) {}
```

>You can add arbitrary sections to the documentation with the @section tag.

```R
#' @section Warning:
#' Do not operate heavy machinery within 8 hours of using this function.
```
### Documenting functions

Most functions have three tags: @param, @examples and @return .

- @param name description describes the function’s inputs or parameters. 
- @examples provides executable R code showing how to use the function in practice. 
- @return description describes the output from the function. This is not always necessary.

### Special characters

- @, which usually marks the start of a roxygen tag. Use @@ to insert a literal @ in the final documentation.
- Use \% to insert a literal % in the output document. The escape is not needed in examples.
- Use \\ to insert a literal \ in the documentation.


### Do repeat yourself

DRY (don’t repeat yourself) principle.

#### Inheriting parameters from other functions

You can inherit parameter descriptions from other functions using @inheritParams source_function.

```R
#' @param a This is the first argument
foo <- function(a) a + 10

#' @param b This is the second argument
#' @inheritParams foo
bar <- function(a, b) {
  foo(a) * 10
  }

```

#### Documenting multiple functions in the same file

You can document multiple functions in the same file by using either @rdname or @describeIn.

```R
## @describeIn
#' Foo bar generic
#'
#' @param x Object to foo.
foobar <- function(x) UseMethod("foobar")

#' @describeIn foobar Difference between the mean and the median
foobar.numeric <- function(x) abs(mean(x) - median(x))

#' @describeIn foobar First and last values pasted together in a string.
foobar.character <- function(x) paste0(x[1], "-", x[length(x)])

## @rdname

#' Basic arithmetic
#'
#' @param x,y numeric vectors.
#' @name arith

#' @rdname arith
add <- function(x, y) x + y

#' @rdname arith
times <- function(x, y) x * y


```

## Vignettes: long-form documentation

>If you’re thinking without writing, you only think you’re thinking. — Leslie Lamport

A vignette is a long-form guide to your package. 

### Vignette workflow

```R
usethis::use_vignette("my-vignette")
```

There are three important components to an R Markdown vignette:

1. The initial metadata block.
2. Markdown for formatting text.
3. Knitr for intermingling text, code and results.

### Metadata


