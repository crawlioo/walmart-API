# import os
# import random
# from projects.config import BaseConfig
#
# # Helper for Rotate User Agent
# def rotate_user_agent():
#     path = f"{os.path.join(BaseConfig.BASE_DIR, './resources/user_agent.txt')}"
#     with open(path, "r") as agent_file:
#         files = agent_file.readlines()
#         agent = random.choice(files)
#         print(path)
#
#         return agent