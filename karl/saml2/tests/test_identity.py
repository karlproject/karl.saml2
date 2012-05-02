import unittest


class Test_sign_on(unittest.TestCase):

    def _callFunc(self, context, request):
        from karl.saml2.identity import sign_on
        return sign_on(context, request)

    def test_GET_no_REMOTE_USER_no_query_string(self):
        context = DummyContext()
        request = DummyRequest()
        result = self._callFunc(context, request)
        self.assertEqual(sorted(result['hidden']), [])

    def test_GET_no_REMOTE_USER_w_query_string(self):
        context = DummyContext()
        request = DummyRequest(GET={'foo': 'bar', 'baz': 'qux'})
        result = self._callFunc(context, request)
        self.assertEqual(sorted(result['hidden']),
                         [('baz', 'qux'), ('foo', 'bar')])


class DummyContext(object):
    def __init__(self, **kw):
        for k, v in kw.items():
            setattr(self, k, v)


class DummyRequest(object):
    def __init__(self, GET={}, POST={}, **kw):
        self.GET = {}
        for k, v in GET.items():
            self.GET[k] = v
        self.POST = {}
        for k, v in POST.items():
            self.POST[k] = v
        self.environ = {}
        for k, v in kw.items():
            self.environ[k] = v
