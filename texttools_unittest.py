#!/usr/bin/env python3

# Copyright 2012 Bill Tyros
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from texttools import Sentence, Word


class TestTextTools(unittest.TestCase):

    def setUp(self):
        self.word = Word("")
        self.sentence = Sentence("")
        
        
    def tearDown(self):
        del self.word
        del self.sentence

    def test_init(self):
        """"Tests init correcting .text params"""
        self.word =  Word("Bill .,")
        self.sentence = Sentence(" Bill is cool. ")
        
        self.assertEqual(self.word.text, "Bill")
        self.assertEqual(self.sentence.text, "Bill is cool.")
        
    def test_Word_count_syllables(self):
        
        self.word.text = "Bill"
        self.assertTrue(self.word.countSyllables() == 1)
        
        self.word.text = "massive"
        self.assertTrue(self.word.countSyllables() == 2)
        
        self.word.text = 'gigantic'
        self.assertTrue(self.word.countSyllables() == 3)
        
        self.word.text = 'considerable'
        self.assertTrue(self.word.countSyllables() == 4)
        
    def test_Word_count(self):
        self.word.text = "Bill"
        
        self.assertTrue(self.word.count("B") == 1)
        self.assertTrue(self.word.count("i") == 1)
        self.assertTrue(self.word.count("l") == 2)
        self.assertTrue(self.word.count("ll") == 1)
        
    def test_Word_istitle(self):
        self.word.text = "Bob"
        self.assertTrue(self.word.iscapitalize())
        
        self.word.text = "apple"
        self.assertFalse(self.word.iscapitalize())
    
    def test_Word_eq(self):
        test_word = " Bill ., "
        self.word.text = test_word
        word2 = Word(test_word)
        
        self.assertEqual(self.word, word2)
        self.assertEqual(self.word.text, word2.text)
    
    def test_Sentence_eq(self):
        test_sentence = " Bill is cool. "
        self.sentence.text = test_sentence
        sentence2 = Sentence(test_sentence)
        
        self.assertEqual(self.sentence, sentence2)
        self.assertEqual(self.sentence.text, sentence2.text)
        
if __name__ == '__main__':
    unittest.main()