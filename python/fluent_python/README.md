### chapter6 Design Patterns with First-Class Functions

#### Case Study: Refactoring Strategy

```python

# The promos list is built by introspection of a new promotions module
promos = [func for name, func in
	inspect.getmembers(promotions, inspect.isfunction)]

```

### chapter7 Function Decorators and Closures


#### Memoization with functools.lru_cache

> It implements memoization: an optimization technique that works by saving the results of previous invocations of an expensive function, avoiding repeat computations on previously used arguments.

#### Generic Functions with Single Dispatch

> If you decorate a plain function with @singledispatch, it becomes a generic function: a group of functions to perform the same operation in different ways, depending on the type of the first argument.


#### Parameterized Decorators

So how do you make a decorator accept other arguments? 
> make a decorator factory that takes those arguments and returns a decorator, which is then applied to the function to be decorated.


## PART IV Object-Oriented Idioms

### chapter8 Object References, Mutability, and Recycling

Every object has an identity, a type and a value. An object’s identity never changes once
it has been created; you may think of it as the object’s address in memory. The is operator
compares the identity of two objects; the id() function returns an integer representing
its identity.


#### Choosing Between == and is

The == operator compares the values of objects (the data they hold), while is compares
their identities.


#### The Relative Immutability of Tuples

The immutability of tuples really refers to the physical contents of the
tuple data structure (i.e., the references it holds), and does not extend to the referenced
objects.

#### Copies Are Shallow by Default

Using the constructor or [:] produces a shallow copy (i.e., the outermost
container is duplicated, but the copy is filled with references to the same items held by
the original container).

#### Deep and Shallow Copies of Arbitrary Objects

- make copy of mutable object
- remembers the objects already copied to handle cyclic references gracefully

A deep copy may be too deep in some cases. For example, objects may refer to
external resources or singletons that should not be copied. You can control the behavior
of both copy and deepcopy by implementing the __copy__() and __deepcopy__()

#### Function Parameters as References

The only mode of parameter passing in Python is call by sharing. Call by sharing means that each formal
parameter of the function gets a copy of each reference in the arguments. In other words,
the parameters inside the function become aliases of the actual arguments.

#### Defensive Programming with Mutable Parameters

```python

def __init__(self, passengers=None):
	if passengers is None:
		self.passengers = []
	else:
		self.passengers = list(passengers)
```

#### The WeakValueDictionary Skit

[A WeakKeyDictionary] can be used to associate additional data with an object owned
by other parts of an application without adding attributes to those objects. This can be
especially useful with objects that override attribute accesses.


#### Limitations of Weak References

Not every Python object may be the target, or referent, of a weak reference. Basic list
and dict instances may not be referents, but a plain subclass of either can solve this
problem easily:

```python

class MyList(list):
	"""list subclass whose instances may be weakly referenced"""
	
a_list = MyList(range(10))

wref_to_a_list = weakref.ref(a_list)

```

### chapter9 A Pythonic Object

#### Object Representations

__repr__ , __str__ , __bytes__ and __format__ .

#### classmethod Versus staticmethod

- classmethod: to define a method that operates on the class and not on instances. classmethod changes the way the method is called, so it receives the class itself as the first argument, instead of an instance. Its most common use is for alternative constructors
- staticmethod: In essence, a static method is just like a plain function that happens to live in a class body, instead of being defined at the module level.

#### Formatted Displays

The Format Specification Mini-Language is extensible because each class gets to inter‐
pret the format_spec argument as it likes. For instance, the classes in the datetime
module use the same format codes in the strftime() functions and in their __for
mat__ methods.

```python

from datetime import datetime
now = datetime.now()
format(now, '%H:%M:%S')
"It's now {:%I:%M %p}".format(now)

```

#### A Hashable Vector2d

1. implement __hash__ ( __eq__ is also required)
2. make vector instances immutable

#### Saving Space with the __slots__ Class Attribute

If you are dealing with millions of instances with few attributes, the
__slots__ class attribute can save a lot of memory, by letting the interpreter store the
instance attributes in a tuple instead of a dict .

#### The Problems with __slots__

- You must remember to redeclare __slots__ in each subclass, because the inherited attribute is ignored by the interpreter.
- Instances will only be able to have the attributes listed in __slots__ , unless you include '__dict__' in __slots__ (but doing so may negate the memory savings).
- Instances cannot be targets of weak references unless you remember to include '__weakref__' in __slots__ .

#### Overriding Class Attributes

```python

from vector2d_v3 import Vector2d

class ShortVector2d(Vector2d):
	typecode = 'f'

```
