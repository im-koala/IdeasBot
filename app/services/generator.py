from aiohttp.client import ClientSession

from bs4 import BeautifulSoup


async def idea_generator(session: ClientSession) -> str:
    url = "https://thisideadoesnotexist.com/"
    async with session.get(url) as response:
        html = await response.text()
    soup = BeautifulSoup(html, "html.parser")
    return soup.find("h2").text.strip()
