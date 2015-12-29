import collections
import requests
from settings import FLICKR_KEY, FLICKR_SEC
import hashlib


class ImgGrab:
    def __init__(self):
        pass

    def search(self, term):
        url = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={api_key}&text={term}&format=json&nojsoncallback=1&sort=relevance'.format(
            term=term,
            api_key=FLICKR_KEY,
        )
        response = requests.get(url).json()
        return self.get_url(response['photos']['photo'][0])

    def get_signature(self, args):
        # Sort your argument list into alphabetical order based on the parameter name.
        # e.g. foo=1, bar=2, baz=3 sorts to bar=2, baz=3, foo=1
        # concatenate the shared secret and argument name-value pairs
        # e.g. SECRETbar2baz3foo1
        # calculate the md5() hash of this string
        # append this value to the argument list with the name api_sig, in hexidecimal string form
        # e.g. api_sig=1f3870be274f6c49b3e31a0c6728957f
        args = collections.OrderedDict(sorted(args.items()))
        val = ''
        for kv in args:
            val  = val + kv + str(args[kv])
        val = FLICKR_SEC + val
        return hashlib.md5(val).hexdigest()

    def get_url(self, result):
        return 'https://farm{farm}.staticflickr.com/{server}/{id}_{secret}.jpg'.format(**result)
