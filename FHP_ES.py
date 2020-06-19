import numpy as np

from DREAM_and_DeepCFR.TrainingProfile import TrainingProfile
from DREAM_and_DeepCFR.workers.driver.Driver import Driver
from HYPERS import *
from PokerRL.game.games import Flop3Holdem  # or any other game

if __name__ == '__main__':
    ctrl = Driver(t_prof=TrainingProfile(
        name="FHP_ESSDCFR_v001_SEED" + str(np.random.randint(1000000)),

        n_traversals_per_iter=(SDCFR_FHP_TRAVERSALS_ES / N_LA_FHP_CFR),
        sampler="es",

        game_cls=Flop3Holdem,
        n_batches_adv_training=SDCFR_FHP_BATCHES,
        n_learner_actor_workers=N_LA_FHP_CFR,
        mini_batch_size_adv=int(SDCFR_FHP_BATCH_SIZE / N_LA_FHP_CFR),
        max_buffer_size_adv=int(4e7 / N_LA_FHP_CFR),
        DISTRIBUTED=True,
        rlbr_args=DIST_RLBR_ARGS_games,

    ),
        eval_methods={"rlbr": RL_BR_FREQ_CFR})
    ctrl.run()
