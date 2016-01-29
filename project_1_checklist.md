- [x] [**Comments**](https://google.github.io/styleguide/pyguide.html#Comments)
    - [x] Block and inline comments

- [x] **DocStrings**
```python
class myClass(object):
      """This is a example showing docstrings
      
      Attributes:
          attr1 (str): This should say something about attr1.
          attr2 (int): This should tell the purpose of attr2 
      
      Etc....
      """

          def func(arg1, arg2):
              """Summary line.

              Extended description of function.

              Args:
                  arg1 (int): Description of arg1
                  arg2 (str): Description of arg2

              Returns:
                  bool: Description of return value

              """
              return True

      print myClass.__doc__
```
- [x] Pep8
	- [x] Python's style guide Pep8 is used
	    - [x] make sure that we write consistent, readable, and maintainable code.
	- [x] The maximum line length is 80 characters
	    - [x] method or a dict or array declaration passes 80 characters. 
	        - [x] You can resolve this by moving arguments to a new line
- [x] Whitespace near comments
	- [x] My awesome comment has a space between the # symbol and text

[README](http://jfhbrook.github.io/2011/11/09/readmes.html)
- [x] Project has a README
- [x] readme gives the user instructions on how to get started running your python code

[Testing](https://www.udacity.com/course/software-testing--cs258)

**Further Improvements**
- [x] Movie
	- [x] add release year
	- [x] add actors
- [x] adjust html template to show new fields
