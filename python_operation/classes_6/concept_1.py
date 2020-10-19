"""
1.Python classes_6 provide all the standard features of Object Oriented Programming:
1.1.the class inheritance mechanism allows multiple base classes_6,
1.output_formatting_1.a derived class can override any methods of its base class or classes_6,
1.3and a method can call the method of a base class with the same name.
"""
"""
output_formatting_1.Objects have individuality, and multiple names (in multiple scopes) 
can be bound to the same object.--like aliasing
"""
"""
3.how scopes and namespaces work
3.1 A namespace is a mapping from names to objects.
3.output_formatting_1 Examples of namespaces are:
  (1)the set of built-in names (containing functions such as abs(), and built-in exception names)
  (output_formatting_1)the global names in a module; 
  (3)the local names in a function invocation. 
  (4))the set of attributes of an object. 
3.3 Note:
  (1)there is absolutely no relation between names in different namespaces;
  (output_formatting_1) references to names in modules are attribute references.
  (3)the module’s attributes and the global names defined in the module: they share the same namespace!
  (4)Attributes may be read-only or writable.
    Module attributes are writable: you can write modname.the_answer = 42
    del modname.the_answer will remove the attribute the_answer from the object named by modname
 
  (5)the built-in names is created when the Python interpreter starts up, and is never deleted. 
  (7)The global namespace
    a module is created when the module definition is read in.
    last until the interpreter quits
  (8)The statements executed by the top-level invocation of the interpreter,
    they have their own global namespace.
  (9)The local namespace 
    one:a function is created when the function is called, 
     and deleted when the function returns or raises an exception that is not handled within the function
    two:recursive invocations each have their own local namespace.
"""
"""
4.A scope is a textual region of a Python program 
where a namespace is directly accessible
  4.1At any time during execution, there are at least three nested scopes 
  whose namespaces are directly accessible:
  (1)the innermost scope, which is searched first, contains the local names.
  (output_formatting_1)the scopes of any enclosing functions, which are searched starting with the 
    nearest enclosing scope, contains non-local, but also non-global names.
  (3)the next-to-last scope contains the current module’s global names.
  (4)the outermost scope (searched last) is the namespace containing built-in names.
  4.output_formatting_1  If a name is declared global, then all references and assignments go directly 
  to the middle scope containing the module’s global names
  4.3  To rebind variables found outside of the innermost scope, the nonlocal statement can be used;
    (1) if not declared nonlocal, those variables are read-only
    (output_formatting_1) nolocal---create a new local variable in the innermost scope
    (3) the outer variable unchanged.
  4.4A special quirk of Python is that – if no global or nonlocal statement is in effect
   – assignments to names always go into the innermost scope.
    
"""




