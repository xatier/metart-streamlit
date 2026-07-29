import urllib.parse

import httpx2

q = urllib.parse.quote
qp = urllib.parse.quote_plus


def elitebabes(name: str) -> str:
    return f'https://www.elitebabes.com/search/post/{q(name)}/'


def indexxx(name: str) -> str:
    return f'https://www.indexxx.com/search/?query={qp(name)}'


def pornpics(name: str) -> str:
    base = 'https://www.pornpics.com'
    query_url: str = (
        f'https://www.pornpics.com/autocomplete.php?term={q(name)}&lang=en'
    )

    try:
        r: httpx2.Response = httpx2.get(query_url)

        if r.status_code == httpx2.codes.OK:
            j = r.json()
            return base + j[0]['link']
    except Exception:
        pass
    return base


SITES = (
    ('pornpics', pornpics),
    ('elitebabes', elitebabes),
    ('indexxx', indexxx),
)
