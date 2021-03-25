# flake8-kwarger
kwarger is a Flake8 plugin which enforces named kwargs or trasterisks in your function arguments.

```
$ pip install git+https://github.com/madhavajay/flake8-kwarger#egg=flake8-kwarger
```

# Rules
```
FKO100 Non Keyword-Only Arguments not allowed. Try adding a '*'.
```

```python
class A:
    @staticmethod
    def foo_bad(forcenamed):
        print(forcenamed)

    @staticmethod
    def foo_good(*, forcenamed):
        print(forcenamed)

    def bar_bad(self, forcenamed):
        print(self, forcenamed)

    def bar_good(self, *, forcenamed):
        print(self, forcenamed)

    def bar_bad_ignore(_self):  # noqa: FKO100
        print(_self)

    @classmethod
    def baz_bad(cls, forcenamed):
        print(forcenamed)

    @classmethod
    def baz_good(cls, *, forcenamed):
        print(forcenamed)
```
