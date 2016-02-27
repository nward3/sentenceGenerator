# Sentence Generator

This sentence generator is a python based program that works using the ideas of a
Markov model to predict the next character of the text based on the most recent
series of characters encountered. By utilizing the ideas behind a Markov model,
the program attempts to detect any patterns in the text and use such patterns
to generate new sentences that are similar to the model.


# Running

This sentence generator can be run from the command line by using the Python
interpreter with python version 2.7.10. The sentence generator utilizes the
random and collections modules. The program is accompanied by excerpts from
five classic novels that can be used as models for basing sentence generations.


# Using

The sentence generator can be used by running the command: python generator.py
from the command line. Once the program has been started, the user will
be prompted to specify the desired Markov model order using an integer
between 1 and 10, where 10 is the strongest and 1 is the weakest. While
a higher order produces a more accurate resemblance to real sentences,
it results in a longer runtime to produce the sentences. After an order
is selected, the user is prompted to choose 1 of 5 sample texts to use
as a model for text generation. After specifying a sample text, the
program will generate text until either 1000 characters are generated
or until the program does not have enough information from the model to
predict a new character in the sequence.
