### **1. Basic Function Logger**

Write a decorator that prints `"Function started"` before the wrapped function runs.

### **2. Timestamp Decorator**

Create a decorator that prints the current time just before the function executes.

### **3. Multiple Calls**

Make a decorator that calls the wrapped function twice.

### **4. Preserve Metadata**

Write a decorator that wraps a function but preserves its `__name__` and docstring.

### **5. Argument Printer**

Create a decorator that prints all positional and keyword arguments before calling the function.

### **6. Result Logger**

Write a decorator that logs the return value of a function.

### **7. Type Checker**

Make a decorator that checks whether all arguments passed to a function are of a specified type (provided to the decorator as an argument).

### **8. Retry Decorator**

Create a decorator that retries the function a specified number of times if it raises an exception.

### **9. Access Control**

Build a decorator that allows the function to run only if a user role matches a required one.

### **10. Execution Timer**

Write a decorator that measures how long the function takes to run and prints the duration.

### **11. Cache/Memoization**

Create a decorator that caches results of function calls based on argument values.

### **12. Conditional Execution**

Make a decorator that prevents execution unless a certain condition function returns `True`.

### **13. Decorator With Optional Arguments**

Build a decorator that can be used with or without arguments:

```python
@decorator
@decorator(flag=True)
```

### **14. Apply Decorator to Methods**

Write a decorator that works correctly on both regular functions and class instance methods.

### **15. Enforce Return Type**

Create a decorator that ensures the function returns a value of a given type.

### **16. Rate Limiter**

Make a decorator that limits how often the function can be called within a certain time window.

### **17. Async-Aware Decorator**

Create a decorator that works on both synchronous and asynchronous (`async def`) functions.

### **18. Decorator That Takes Another Function as Parameter**

Write a decorator that receives a callback function to transform the wrapped function’s output.

### **19. Class-Based Decorator**

Implement a decorator as a class with `__call__`.

### **20. Compose Multiple Decorators**

Write a decorator that itself applies multiple decorators to a function (a decorator-composer).
