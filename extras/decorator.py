# def fence(func):

#     def wraper():
#         print("+"*10)
#         func()
#         print("+"*10)

#     return wraper

# @fence
# def log():
#     print("Ludo")

# #under the hood what's happening
# another_log = fence(log)
# another_log()

# log()

def custom_fence(fence:str = "+"):
    def add_fence(func):
        def wrapper(text:str):
            print(fence*len(text))
            func(text)
            print(fence*len(text))
        return wrapper
    return add_fence

@custom_fence("-")
def log(text: str):
    print(text)

log("books")

#typing module stuff for decorators
from typing import Callable, Any

def decorator(func: Callable[[Any], None]):
    pass