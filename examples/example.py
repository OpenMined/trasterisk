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

