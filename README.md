# Deep Learning Prerequisite
 Basic Usage of some basic libraries required for deep learning

# NumPy
NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

At the core of the NumPy package, is the ndarray object. This encapsulates n-dimensional arrays of homogeneous data types, with many operations being performed in compiled code for performance. There are several important differences between NumPy arrays and the standard Python sequences:

  - NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size of an ndarray will create     a new array and delete the original.

  - The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory. The exception: one     can have arrays of (Python, including NumPy) objects, thereby allowing for arrays of different sized elements.

  - NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. Typically, such operations are         executed more efficiently and with less code than is possible using Python’s built-in sequences.

  - A growing plethora of scientific and mathematical Python-based packages are using NumPy arrays; though these typically support Python-         sequence input, they convert such input to NumPy arrays prior to processing, and they often output NumPy arrays. In other words, in order       to efficiently use much (perhaps even most) of today’s scientific/mathematical Python-based software, just knowing how to use Python’s         built-in sequence types is insufficient - one also needs to know how to use NumPy arrays.

# MathPlotLib
matplotlib.pyplot is a collection of functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

In matplotlib.pyplot various states are preserved across function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed to the current axes (please note that "axes" here and in most places in the documentation refers to the axes part of a figure and not the strict mathematical term for more than one axis).

# PANDAS
pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real-world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis/manipulation tool available in any language. It is already well on its way toward this goal.

  - pandas is well suited for many different kinds of data:

  - Tabular data with heterogeneously-typed columns, as in an SQL table or Excel spreadsheet

  - Ordered and unordered (not necessarily fixed-frequency) time series data.

  - Arbitrary matrix data (homogeneously typed or heterogeneous) with row and column labels

  - Any other form of observational / statistical data sets. The data need not be labeled at all to be placed into a pandas data structure

# SciPy
SciPy is an open-source Python library which is used to solve scientific and mathematical problems. It is built on the NumPy extension and allows the user to manipulate and visualize data with a wide range of high-level commands. As mentioned earlier, SciPy builds on NumPy and therefore if you import SciPy, there is no need to import NumPy.

Both NumPy and SciPy are Python libraries used for used mathematical and numerical analysis. NumPy contains array data and basic operations such as sorting, indexing, etc whereas, SciPy consists of all the numerical code. Though NumPy provides a number of functions that can help resolve linear algebra, Fourier transforms, etc, SciPy is the library that actually contains fully-featured versions of these functions along with many others. However, if you are doing scientific analysis using Python, you will need to install both NumPy and SciPy since SciPy builds on NumPy.

# Some basic Machine Learning 
The area of Machine Learning deals with the design of programs that can learn rules from data, adapt to changes, and improve performance with experience. In addition to being one of the initial dreams of Computer Science, Machine Learning has become crucial as computers are expected to solve increasingly complex problems and become more integrated into our daily lives.

Here, we will explore the basic theories of machine learning and also some programs. Further, we will also take a look at a pre-trained model to do some object detection

