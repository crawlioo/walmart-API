import os
import random

from projects.config import BaseConfig


# Helper for Rotate User Agent
def rotate_user_agent():
    path = (
        f"{os.path.join(BaseConfig.BASE_DIR, 'scraper/utils/resources/user_agent.txt')}"
    )
    with open(path, "r") as agent_file:
        files = agent_file.readlines()
        agent = random.choice(files)

        return agent.replace("\n", "")


# proxy rotating
def rotate_proxy():
    path = (
        f"{os.path.join(BaseConfig.BASE_DIR, 'scraper/utils/resources/proxies.txt')}"
    )
    with open(path, "r") as proxy_list:
        data_list: list = []
        proxies = proxy_list.readlines()
        for data in proxies:
            proxy = data.split(':')
            username = proxy[2]
            password = proxy[3].replace('\n', '')
            ip = proxy[0]
            port = proxy[1]
            data_proxy = {"http": f"http://{username}:{password}@{ip}:{port}"}
            data_list.append(data_proxy)

        random_proxy = random.choice(data_list)
        print(f'Using Proxy: {random_proxy}')
        return random_proxy