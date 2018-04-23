import environment as gym
import numpy as np
import random
import time
import logging
from pprint import pprint




logger = gym.logger.get_my_logger(__name__)

def timed_function(func):
    def decorated_func(*args, **kwargs):
        s = time.time()
        output = func(*args, **kwargs)
        e = time.time()
        logger.info("{} finished in {} seconds".format(func.__name__,e-s))
        return output
    return decorated_func


if __name__=="__main__":
    logging.disable(logging.DEBUG)
    nElevator = 3
    nFloor = 14
    spawnRates = [1/30]+[1/180]*(nFloor-1)
    avgWeight = 135
    weightLimit = 1200
    loadTime = 1
    

    env = gym.make(nElevator, nFloor, spawnRates, avgWeight, weightLimit, loadTime)
    s = env.reset()
    while True:
        decision_agents  = s["decision agents"]
        states           = s["states"]
        rewards          = s["rewards"]


        # A bunch of printing stuff for debugging

        logger.info("Rewards of decision elevators: {}".format(rewards))
        parsed_states = gym.Environment.parse_states(states[0], nFloor, nElevator)
        logger.info("  hall_calls_up: \n"+"".join([
            "{:8.3}".format(t) for t in parsed_states["hall_call_up_times"]
        ]))
        logger.info("  hall_calls_down: \n"+"".join([
            "{:8.3}".format(t) for t in parsed_states["hall_call_down_times"]
        ]))



        # Picking action here
        actions = [random.sample(env.legal_actions(agent), 1)[0] for agent in decision_agents]# 0 calls for the legal actions of the first elevator




        # Stone Age rendering ftw.
        s = timed_function(env.step)(actions)
        env.render(0.5
        time.sleep(1)
