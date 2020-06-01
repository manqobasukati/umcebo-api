from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

incoming_resp = [
        {
            "description": "i love banana very much",
            "amount": 50
        },
        {
            "description": "banana",
            "amount": 20
        },
        {
            "description": "chips",
            "amount": 50
        }
    ]

def convert_obj_to_sent(incoming_object):
    arr_of_sentences = []
    for i in incoming_object:
        arr_of_sentences.append(i["description"])

    sentence = ' '.join(map(str, arr_of_sentences))

    return sentence


def get_word_freq_function(**kwargs):

    sentence  = convert_obj_to_sent(kwargs.get('incoming',None))

    tokenized_word = word_tokenize(sentence)

    stop_words = set(stopwords.words('english'))

    filtered_words = [w  for w in tokenized_word if not w in stop_words]

    fdist = FreqDist(filtered_words)

    return get_total_amount(fdist.most_common(5),kwargs.get('incoming',None))

def get_total_amount(tokens,obj):
    
    token_infos = []
    for token in tokens:
        token_info = {
            "token_name":token[0],
            "token_count":token[1],
            "token_action":"",
            "token_total_amount":0
        }
        for resp in obj:
           
            if token[0] in resp["description"]:
                token_info["token_total_amount"] = token_info["token_total_amount"]+  resp["amount"]
                token_info["token_action"] = resp["action"]
        token_infos.append(token_info)

    return token_infos



       





