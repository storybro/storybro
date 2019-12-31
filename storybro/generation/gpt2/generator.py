import json
import os
import warnings

import numpy as np

import tensorflow as tf

from storybro.generation.gpt2 import model, encoder, sample
from storybro.story.utils import cut_trailing_sentence, remove_profanity

warnings.filterwarnings("ignore")

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)


class GPT2Generator:
    def __init__(self, modelobj, generate_num=60, temperature=0.4, top_k=40, top_p=0.9, censor=True):
        self.generate_num = generate_num
        self.temp = temperature
        self.top_k = top_k

        self.top_p = top_p
        self.censor = censor

        self.model = modelobj

        self.batch_size = 1
        self.samples = 1

        self.enc = encoder.get_encoder(self.model.root_path)
        hparams = model.default_hparams()
        with open(os.path.join(self.model.root_path, "hparams.json")) as f:
            hparams.override_from_dict(json.load(f))
        seed = np.random.randint(0, 100000)

        config = tf.compat.v1.ConfigProto()
        config.gpu_options.allow_growth = True
        self.sess = tf.compat.v1.Session(config=config)

        self.context = tf.placeholder(tf.int32, [self.batch_size, None])
        # np.random.seed(seed)
        # tf.set_random_seed(seed)
        self.output = sample.sample_sequence(
            hparams=hparams,
            length=self.generate_num,
            context=self.context,
            batch_size=self.batch_size,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
        )

        saver = tf.train.Saver()
        ckpt = tf.train.latest_checkpoint(self.model.root_path)
        saver.restore(self.sess, ckpt)

    def prompt_replace(self, prompt):
        if len(prompt) > 0 and prompt[-1] == " ":
            prompt = prompt[:-1]

        return prompt

    def result_replace(self, result):
        result = cut_trailing_sentence(result)

        if len(result) == 0:
            return ""

        result = result.replace('."', '".')
        result = result.replace("#", "")
        result = result.replace("*", "")
        result = result.replace("\n\n", "\n")

        if self.censor:
            result = remove_profanity(result)

        return result

    def generate_raw(self, prompt):
        context_tokens = self.enc.encode(prompt)
        generated = 0
        for _ in range(self.samples // self.batch_size):
            out = self.sess.run(
                self.output,
                feed_dict={
                    self.context: [context_tokens for _ in range(self.batch_size)]
                },
            )[:, len(context_tokens) :]
            for i in range(self.batch_size):
                generated += 1
                text = self.enc.decode(out[i])
        return text

    def generate(self, prompt):

        debug_print = False
        filtered_prompt = self.prompt_replace(prompt)

        result = self.generate_raw(filtered_prompt)
        filtered_result = self.result_replace(result)

        if len(filtered_result) == 0:
            return self.generate(prompt)

        return filtered_result
