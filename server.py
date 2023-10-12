from dataclasses import dataclass
import json
import random

import httpx
import streamlit as st

import sites

URL_BASE: str = random.choice(
    [
        'https://www.alsscan.com',
        'https://www.domai.com',
        'https://www.eroticbeauty.com',
        'https://www.errotica-archives.com',
        'https://www.goddessnudes.com',
        'https://www.lovehairy.com',
        'https://www.metart.com',
        'https://www.metartx.com',
        'https://www.sexart.com',
        'https://www.straplez.com',
        'https://www.thelifeerotic.com',
        'https://www.vivthomas.com',
    ],
)

CDN_BASE = 'https://cdn.metartnetwork.com'
API_URL = f'{URL_BASE}/api/updates?tab=stream&page=1'
WIDTH = 540


@dataclass
class Content:
    model: str
    model_url: str
    image: str


def fetch() -> list[Content]:
    try:
        j = httpx.get(API_URL, follow_redirects=True).json()
    except json.decoder.JSONDecodeError:
        print(f'JSONDecodeError on fetching {URL_BASE}')

    contents: list[Content] = []
    for g in j.get('galleries'):
        img_src = f'{CDN_BASE}/{g["siteUUID"]}{g["coverCleanImagePath"]}'
        model_name = g['models'][0]['name']
        model_url = g['models'][0]['path']

        contents.append(
            Content(
                model=model_name,
                model_url=f'{URL_BASE}{model_url}',
                image=img_src,
            )
        )

    return contents


def render(contents: list[Content]) -> None:

    st.markdown(f'# metart network viewer [{URL_BASE}]({URL_BASE})')
    cols = st.columns(3)

    for i, c in enumerate(contents):

        with cols[i % 3]:
            st.image(image=c.image, width=WIDTH)
            st.link_button(f'Model: {c.model}', c.model_url)

            # hbox for site links
            buttons = st.columns(len(sites.SITES))
            for i, b in enumerate(buttons):
                b.link_button(sites.SITES[i][0], sites.SITES[i][1](c.model))


if __name__ == '__main__':
    st.set_page_config(
        page_title=f'boobs on {URL_BASE}',
        layout='wide',
    )
    render(fetch())
