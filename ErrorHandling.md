    Traceback (most recent call last):
      File "/usr/local/lib/python3.9/site-packages/tornado/http1connection.py", line 273, in _read_message
        delegate.finish()
      File "/usr/local/lib/python3.9/site-packages/tornado/routing.py", line 268, in finish
        self.delegate.finish()
      File "/usr/local/lib/python3.9/site-packages/tornado/web.py", line 2290, in finish
        self.execute()
      File "/usr/local/lib/python3.9/site-packages/tornado/web.py", line 2309, in execute
        self.handler = self.handler_class(
      File "/usr/local/lib/python3.9/site-packages/tornado/websocket.py", line 224, in __init__
        super().__init__(application, request, **kwargs)
      File "/usr/local/lib/python3.9/site-packages/tornado/web.py", line 209, in __init__
        super().__init__()
      File "/usr/local/Cellar/python@3.9/3.9.7_1/Frameworks/Python.framework/Versions/3.9/lib/python3.9/typing.py", line 1083, in _no_init
        raise TypeError('Protocols cannot be instantiated')
    TypeError: Protocols cannot be instantiated

<b>Solution: 'brew upgrade'</b>


