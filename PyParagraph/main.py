import re
import os

# for each paragraph
for i in range(1, 3):
    # load in
    filename = os.path.join('raw_data', f'paragraph_{i}.txt')
    with open(filename, 'r') as fin:
        paragraph = fin.read()
    # split on newline and join to string
    new_paragraph = " ".join(paragraph.split('\n'))
    # capture sentences and put in list
    paragraph_list = re.split("(?<=[.!?]) +", new_paragraph)

    # initialize values
    num_words = 0
    num_sentences = len(paragraph_list)
    words_per_sentence = []
    letters_per_word = []

    # for each sentence
    for j in range(num_sentences):
        # split paragraph into words and append length to lists
        sentence = paragraph_list[j].split()
        words_per_sentence.append(len(sentence))
        num_words += len(sentence)
        # for each word in sentence
        for k in range(len(sentence)):
            # find length of word
            letters_per_word.append(len(sentence[k]))
        
    # find average words per sentence and average letters per word
    avg_words_per_sentence = sum(words_per_sentence) / len(words_per_sentence)
    avg_letters_per_word = sum(letters_per_word) / len(letters_per_word)
    
    print('Paragraph Analysis')
    print('-----------------')
    print(f'Approximate Word Count: {num_words}')
    print(f'Approximate Sentence Count: {num_sentences}')
    print(f'Average Letter Count: {avg_letters_per_word:.3f}')
    print(f'Average Sentence Length: {avg_words_per_sentence:.3f}')
    
    # write to file
    filename = os.path.join('assets', f'paragraph_analysis_{i}.txt')
    with open(filename, 'w') as fout:
        fout.write('Paragraph Analysis\n')
        fout.write('-----------------\n')
        fout.write(f'Approximate Word Count: {num_words}\n')
        fout.write(f'Approximate Sentence Count: {num_sentences}\n')
        fout.write(f'Average Letter Count: {avg_letters_per_word:.3f}\n')
        fout.write(f'Average Sentence Length: {avg_words_per_sentence:.3f}\n')
    