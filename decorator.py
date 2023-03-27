def before_after(inner_func):
    
    def before_after():
        print('before')
        inner_func()
        print('after')
    return before_after

@before_after
def test_func():
    print('main logic')

test_func()