import typing as typ
import json

import asyncio
from asyncio import Semaphore
from aiohttp import ClientSession

from information_processing import save_data
from query_build import build_post_json


async def create_requests(id_list: typ.List[str],
                          query_type: typ.Dict[str, bool],
                          result_path: str,
                          semaphore_count: int) -> None:
    tasks = []
    semaphore = Semaphore(semaphore_count)

    async with ClientSession() as session:
        for hotel_id in id_list:
            json_data = build_post_json(hotel_id, query_type)
            task = asyncio.ensure_future(bound_fetch(json_data, result_path, semaphore, session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses


async def bound_fetch(json_data: dict, result_path: str, semaphore: Semaphore, session: ClientSession) -> None:
    async with semaphore:
        data = await http_request(json_data, session)
        save_data(data, result_path)


async def http_request(json_data: dict, session: ClientSession) -> dict:
    url = "https://www.homeaway.com/serp/g"
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
         ' (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    content_type = 'application/json'
    headers = {'User-Agent': ua, 'Content-Type': content_type}

    async with session.post(url, headers=headers, json=json_data) as response:
        resp_data = await response.read()
        resp_json = json.loads(resp_data)
        return resp_json



